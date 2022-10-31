import pandas as pd
import os
import sys, getopt
import consts as CONSTS

class CSVCombiner():

    def __init__(self):
        self.files = []
        self.folder = ""
        self.output_file = ""
        self.is_print = True
        self.is_output_file = False
        self.file_chunks = []
        self.combined_csv = None

    def main(self,argv):
        self.validate_args(argv)
        self.process_csv_files()
        self.combine_csv()
        print(self.is_output_file)
        if not self.is_output_file:
            if not self.is_print:
                print(CONSTS.ENABLE_PRINT)
                sys.exit(2)
            self.print_csv()
        else:
            self.create_csv_file()
            if self.is_print:
                self.print_csv()
        return

    def process_csv_files(self):
        for file in self.files:
            file_name = os.path.basename(file)
            for chunk in pd.read_csv(file,chunksize=10**4):
                chunk["filename"] = file_name
                self.file_chunks.append(chunk)

    def print_csv(self):
        print(self.combined_csv.to_csv(index=False, header=True, chunksize=10**4, line_terminator='\n'), end='')

    def validate_args(self,argv):
        if len(argv) == 0:
            print("Enter csv files to be combined!")
            sys.exit(2)
        try:
            opts, args = getopt.getopt(argv,"o:",["folder=","output=","no-print"])
        except:
            print(CONSTS.ARG_ERROR_MESSAGE)
            sys.exit(2)
        
        files = args
        print("opts",opts)
        # parse all options:
        for opt in opts:
            opt_name = opt[0]
            opt_val = opt[1]
            if opt_name == "-o" or opt_name == "--output":
                self.is_output_file = True
                self.output_file = opt_val
            elif opt_name == "--folder":
                self.folder = opt_val
                if not os.path.exists(opt_val):
                    print(CONSTS.WRONG_FOLDER_MESSAGE)
                    sys.exit(2)
                csv_files = [f for f in os.listdir(self.folder) if f.endswith('.csv')]
                if len(csv_files) <= 0:
                    print(CONSTS.NO_FILE_ERROR)
                    sys.exit(2)
                for csv_file in csv_files:
                    if self.folder[-1] == '/':
                        file_path = self.folder + csv_file
                    else:
                        file_path = self.folder + "/" + csv_file
                    self.files.append(file_path)
            elif opt_name == "--no-print":
                self.is_print = True

        # check if files are present
        for file in files:
            if not os.path.exists(file):
                print(CONSTS.FILE_ERROR)
                sys.exit(2)
            self.files.append(file)
        
    def combine_csv(self):
        self.combined_csv = pd.concat(self.file_chunks)

    def create_csv_file(self):
        self.combined_csv.to_csv(self.output_file+".csv",index=False,header=True)

if __name__ == '__main__':
    obj = CSVCombiner()
    obj.main(sys.argv[1:])