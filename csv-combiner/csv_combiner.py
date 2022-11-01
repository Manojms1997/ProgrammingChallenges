import pandas as pd
import os
import sys, getopt
import consts as CONSTS

##########################################################################################
# Class to combine CSV files into single CSV                                             #
# Properties:                                                                            #
# files, folder, output_file, is_print, is_file_output, file_chunks, combined_csv        #
# methods:                                                                               #
# validate_args, process_csv_files, combine_csv, output_csv, print_csv, create_csv_file  #
# validate_and_process_files, validate_and_process_command_options                       #
##########################################################################################
class CSVCombiner():

    def __init__(self):
        self.files = []
        self.folder = ""
        self.output_file = ""
        self.is_print = True
        self.is_file_output = False
        self.file_chunks = []
        self.combined_csv = None

    def main(self,argv):
        self.validate_args(argv)
        self.process_csv_files()
        self.combine_csv()
        self.output_csv()
        return

    ##########################################################################################
    # Function to handle output of combined CSV                                              #
    # By default console printing is enabled                                                 #
    ##########################################################################################
    def output_csv(self):
        if not self.is_file_output:
            if not self.is_print:
                print(CONSTS.ENABLE_PRINT)
                sys.exit(2)
            self.print_csv()
        else:
            self.create_csv_file()
            if self.is_print:
                self.print_csv()

    ##########################################################################################
    # function to read CSV files in chunk and add filename column to it                      #
    ##########################################################################################
    def process_csv_files(self):
        for file in self.files:
            file_name = os.path.basename(file)
            for chunk in pd.read_csv(file,chunksize=10**4):
                chunk["filename"] = file_name
                self.file_chunks.append(chunk)

    ##########################################################################################
    # Function to pring the combined CSV on terminal                                         #
    ########################################################################################## 
    def print_csv(self):
        print(self.combined_csv.to_csv(index=False, header=True, chunksize=10**4, line_terminator='\n'), end='')

    ##########################################################################################
    # Function to validate the arguments and options passed by user on terminal              #
    ##########################################################################################
    def validate_args(self,argv):
        if len(argv) == 0:
            print("Enter csv files to be combined!")
            sys.exit(2)
        try:
            opts, files = getopt.getopt(argv,"o:",["folder=","output=","no-print"])
        except:
            print(CONSTS.ARG_ERROR_MESSAGE)
            sys.exit(2)
        self.validate_and_process_command_options(opts)
        self.validate_and_process_files(files)
        return True
        
    ##########################################################################################
    # Function to validate the input CSV files                                               #
    ##########################################################################################
    def validate_and_process_files(self,files):
        for file in files:
            if not os.path.exists(file):
                print(CONSTS.FILE_ERROR)
                sys.exit(2)
            self.files.append(file)
    
    ##########################################################################################
    # Function to validate command line options given by user                                #
    ##########################################################################################
    def validate_and_process_command_options(self,opts):
        def output_option_handler(opt_val): # Function to handle '--folder' option
            if opt_val == "":
                print(CONSTS.OUTPUT_FILE_NAME_ERROR)
                sys.exit(2)
            self.is_file_output = True
            self.output_file = opt_val
        def folder_option_handler(opt_val): # Function to handle '-o' or '--output' option 
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
        def no_print_option_handler(): # Function to handle '--no-print' option
            self.is_print = False
        for opt in opts:
            opt_name = opt[0]
            opt_val = opt[1]
            if opt_name == "-o" or opt_name == "--output":
                output_option_handler(opt_val)
            elif opt_name == "--folder":
                folder_option_handler(opt_val)
            elif opt_name == "--no-print":
                no_print_option_handler()
    
    ##########################################################################################
    # Function to combine csv files                                                          #
    ##########################################################################################
    def combine_csv(self):
        self.combined_csv = pd.concat(self.file_chunks)

    ##########################################################################################
    # Function to create output csv file                                                     #
    ##########################################################################################
    def create_csv_file(self):
        self.combined_csv.to_csv(self.output_file+".csv",index=False,header=True)

if __name__ == '__main__':
    obj = CSVCombiner()
    obj.main(sys.argv[1:])