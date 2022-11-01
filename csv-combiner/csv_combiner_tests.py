import unittest
import pandas as pd
import sys
from io import StringIO
import os
from csv_combiner import CSVCombiner
import consts as CONSTS
import generatefixtures
class CSVTest(unittest.TestCase):

    csv_combiner = CSVCombiner()
    ACCESSORIES = "./fixtures/accessories.csv"
    CLOTHING = "./fixtures/clothing.csv"
    HOUSEHOLD = "./fixtures/household_cleaners.csv"
    OP = "./op.csv"

    @classmethod
    def setUpClass(cls):
        generatefixtures.main()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.ACCESSORIES)
        os.remove(cls.CLOTHING)
        os.remove(cls.HOUSEHOLD)
        # os.remove(cls.op)
        os.rmdir("./fixtures")
    
    def tearDown(self):
        if os.path.exists(self.OP):
            os.remove(self.OP)

    def test_no_arg(self):
        print("test to check when no arguments are passed to the command line")
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as cm:
            self.csv_combiner.validate_args([])
        sys.stdout = sys.__stdout__ 
        self.assertIn("Enter csv files to be combined!", capturedOutput.getvalue())
        self.assertEqual(cm.exception.code, 2)

    def test_wrong_option(self):
        print("test to check the handling of wrong option")
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as cm:
            self.csv_combiner.validate_args(['-p'])
        sys.stdout = sys.__stdout__ 
        self.assertIn(CONSTS.ARG_ERROR_MESSAGE, capturedOutput.getvalue())
        self.assertEqual(cm.exception.code, 2)

    def test_valid_output_file_properties(self):
        print("test to check the values of class properties when output file writing is enabled")
        self.csv_combiner.validate_args(['-o', 'op', './fixtures/accessories.csv'])
        self.assertEqual(self.csv_combiner.is_file_output,True)
        self.assertEqual(self.csv_combiner.output_file,'op')
    
    def test_combine_two_csv_length(self):
        print("test to check the length of combined csv for two input csv")
        self.csv_combiner.main(['-o', 'op', '--no-print', self.ACCESSORIES, self.CLOTHING])
        op_df = pd.read_csv("./op.csv")
        op_rows = op_df.shape[0]
        accessories_df = pd.read_csv(self.ACCESSORIES)
        accessories_rows = accessories_df.shape[0]
        clothing_df = pd.read_csv(self.CLOTHING)
        clothing_rows = clothing_df.shape[0]
        self.assertEqual(op_rows,accessories_rows+clothing_rows,"output csv rows doesn't match")
    
    def test_new_col_added(self):
        print("test to check if a new column is added to the combined csv")
        self.csv_combiner.main(['-o', 'op', '--no-print', self.ACCESSORIES, self.CLOTHING])
        op_df = pd.read_csv("./op.csv")
        op_cols = op_df.shape[1]
        accessories_df = pd.read_csv(self.ACCESSORIES)
        accessories_cols = accessories_df.shape[1]
        self.assertEqual(op_cols,accessories_cols+1,"output csv cols doesn't match")

    def test_folder_files(self):
        print("test to check if all csv files in a folder are added when --folder option is enabled")
        csv_comb = CSVCombiner()
        csv_comb.main(['-o', 'op', '--no-print', '--folder', './fixtures'])
        op_df = pd.read_csv("./op.csv")
        op_rows = op_df.shape[0]
        accessories_df = pd.read_csv(self.ACCESSORIES)
        accessories_rows = accessories_df.shape[0]
        clothing_df = pd.read_csv(self.CLOTHING)
        clothing_rows = clothing_df.shape[0]
        household_df = pd.read_csv(self.HOUSEHOLD)
        household_rows = household_df.shape[0]
        self.assertEqual(op_rows,accessories_rows+clothing_rows+household_rows,"output csv cols doesn't match")

    def test_combine_three_csv_length(self):
        print("test to check if three csv files are combined")
        csv_comb = CSVCombiner()
        csv_comb.main(['-o', 'op', '--no-print', self.HOUSEHOLD,self.ACCESSORIES,self.CLOTHING])
        op_df = pd.read_csv("./op.csv")
        op_rows = op_df.shape[0]
        accessories_df = pd.read_csv(self.ACCESSORIES)
        accessories_rows = accessories_df.shape[0]
        clothing_df = pd.read_csv(self.CLOTHING)
        clothing_rows = clothing_df.shape[0]
        household_df = pd.read_csv(self.HOUSEHOLD)
        household_rows = household_df.shape[0]
        self.assertEqual(op_rows,accessories_rows+clothing_rows+household_rows,"output csv cols doesn't match")

    def test_csv_files_combine_value(self):
        print("test to check if combined csv has same contents as combining two input csvs and adding a column")
        csv_comb = CSVCombiner()
        csv_comb.main(['-o', 'op', '--no-print', self.HOUSEHOLD,self.ACCESSORIES])
        op_df = pd.read_csv("./op.csv")
        household_df = pd.read_csv(self.HOUSEHOLD)
        household_df['filename'] = 'household_cleaners.csv'
        accessories_df = pd.read_csv(self.ACCESSORIES)
        accessories_df['filename'] = 'accessories.csv'
        combined_df = pd.concat([household_df,accessories_df])
        self.assertEqual(op_df.values.tolist(),combined_df.values.tolist())

    def test_wrong_folder_path(self):
        print("test to check the handling of wrong folder path input")
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as cm:
            self.csv_combiner.validate_args(['--folder', './wrong-folder-path'])
        sys.stdout = sys.__stdout__ 
        self.assertIn(CONSTS.WRONG_FOLDER_MESSAGE, capturedOutput.getvalue())
        self.assertEqual(cm.exception.code, 2)
    
    def test_print_option(self):
        print("test to check the handling of --no-print option")
        self.csv_combiner.validate_args(['--no-print','-o','-op','./fixtures/clothing.csv'])
        self.assertEqual(self.csv_combiner.is_print,False)

unittest.main()