<!-- # CSV Combiner

Write a command line program that takes several CSV files as arguments. Each CSV
file (found in the `fixtures` directory of this repo) will have the same
columns. Your script should output a new CSV file to `stdout` that contains the
rows from each of the inputs along with an additional column that has the
filename from which the row came (only the file's basename, not the entire path).
Use `filename` as the header for the additional column.

##  Considerations
* You should use coding best practices. Your code should be re-usable and extensible.
* Your code should be testable by a CI/CD process. 
* Unit tests should be included.

## Example
This example is provided as one of the ways your code should run. It should also be
able to handle more than two inputs, inputs with different columns, and very large (> 2GB) 
files gracefully.

```
$ ./csv-combiner.php ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv
```

Given two input files named `clothing.csv` and `accessories.csv`.

|email_hash|category|
|----------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|

|email_hash|category|
|----------|--------|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|

Your script would output

|email_hash|category|filename|
|----------|--------|--------|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Shirts|clothing.csv|
|21d56b6a011f91f4163fcb13d416aa4e1a2c7d82115b3fd3d831241fd63|Pants|clothing.csv|
|166ca9b3a59edaf774d107533fba2c70ed309516376ce2693e92c777dd971c4b|Cardigans|clothing.csv|
|176146e4ae48e70df2e628b45dccfd53405c73f951c003fb8c9c09b3207e7aab|Wallets|accessories.csv|
|63d42170fa2d706101ab713de2313ad3f9a05aa0b1c875a56545cfd69f7101fe|Purses|accessories.csv|
 -->

 # CSV Combiner
    
This is a command line tool for combining multiple csv files. CSV files are combined based on the column names. If two CSVs are having different columns, this tool handles that as well. 

### Usage
There are several ways this command line tool can be used for combining CSV files.
1. File Inputs:
Several csv files can be given as a space separated string
```
python csv_combiner.py ./fixtures/clothing.csv ./fixtures/accessories.csv
```
2. Folder Input:
A single folder containing CSV files can be given as input. All CSV files under this folder is combined
```
python csv_combiner.py --folder ./fixtures
```
#### Note: By default, the combined csv string is printed on the terminal. If you want it to be added as a .csv file use '-o' or '--output' options. More about options given below.

### Options

1. Output
By using '-o' or '--output' option followed by output file name, the combined csv is saved in the form of a csv file
```
python csv_combiner.py -o output --folder ./fixtures
```
This will create a file called output.csv in the working directory whcih has the combined csv

2. No print
To not print the csv file on the terminal, use this option
```
python csv_combiner.py -o output --no-print --folder ./fixtures
```

#### Note: Add all options before providing space separated file paths


### Packages and Libraries used
1. Pandas
2. sys
3. os
4. getopt
5. io
6. unittest

