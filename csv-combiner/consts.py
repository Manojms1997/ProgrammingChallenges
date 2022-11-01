ENABLE_PRINT = "enable printing on terminal or to a file!"
ARG_ERROR_MESSAGE = "invalid input format!!\n\
The command should be any one of these formats:\n\
python csv-combiner.py file1.csv file2.csv ...\n\
python csv-combiner.py --folder csv_folder_path\n\
----------------------------------------\n\
optional arguments:\n\
Note: Give all optional params before giving file name arguments\n\
'-o' or '--output' for output csv file name\n\
'--no-print' for not printing combined csv on terminal(Note: use this only when you are printing the csv to a file)"
FILE_ERROR = "file path not exists. Please check if your input csv file path is correct\n\
Also please check if you are not giving valid optional parameters and any optional parameters after file names. The command format should be like:\n\
python csv-combiner.py -o op.csv file1.csv file2.csv ...\n\
valid options are: '-o','--output','--folder','--no-print'"
WRONG_FOLDER_MESSAGE = "Wrong folder path!!"
NO_FILE_ERROR = "No CSV files present in the folder specified!"
OUTPUT_FILE_NAME_ERROR = "Output file name not specified!!"