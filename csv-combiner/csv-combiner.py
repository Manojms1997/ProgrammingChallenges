import pandas as pd
import os
import sys, getopt

# take command line input
class CSVCombiner():

    def __init__(self):
        self.files = []
        self.folder = ""
        self.output_file = ""
        self.is_print = True
        self.is_output_file = False

    def main(self,argv):
        #arguments validation
        self.validate_args(argv)

    def combine_csv(self):
        pass

    def print_csv():
        pass

    def validate_args(self,argv):
        if len(argv) == 0:
            print("Enter csv files to be combined!")
            sys.exit(2)
        try:
            opts, args = getopt.getopt(argv,"o:",["folder=","output=","no-print"])
        except:
            print("invalid input format!!")
            print("The command should be any one of these formats:")
            print("python csv-combiner.py file1.csv file2.csv ...")
            print("python csv-combiner.py --folder csv_folder_path")
            print("----------------------------------------")
            print("optional arguments:")
            print("Note: Give all optional params before giving file name arguments")
            print("'-o' or '--output' for output csv file name")
            print("'--no-print' for not printing combined csv on terminal(Note: use this only when you are printing the csv to a file)")
            sys.exit(2)
        
        files = args
        print("opts",opts)
        # parse all options:
        for opt in opts:
            opt_name = opt[0]
            opt_val = opt[1]
            if opt_name == "o" or opt_name == "--output":
                self.is_output_file = True
                self.output_file = opt_val
            elif opt_name == "--folder":
                self.folder = opt_val
                if not os.path.exists(opt_val):
                    print("Wrong folder path!!")
                    sys.exit(2)
                csv_files = [f for f in os.listdir(self.folder) if f.endswith('.csv')]
                if len(csv_files) <= 0:
                    print("No CSV files present in the folder specified!")
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
                print("file path not exists. Please check if your input csv file path is correct")
                print("Also please check if you are not giving valid optional parameters and any optional parameters after file names. The command format should be like:")
                print("python csv-combiner.py -o op.csv file1.csv file2.csv ...")
                print("valid options are: '-o','--output','--folder','--no-print'")
                sys.exit(2)
            self.files.append(file)
        
        
    def create_csv_file():
        pass



if __name__ == '__main__':
    obj = CSVCombiner()
    obj.main(sys.argv[1:])