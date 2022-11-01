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
    accessories = "./fixtures/accessories.csv"
    clothing = "./fixtures/clothing.csv"
    household = "./fixtures/household_cleaners.csv"

    @classmethod
    def setUpClass(cls):
        generatefixtures.main()

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.accessories)
        os.remove(cls.clothing)
        os.remove(cls.household)
        os.rmdir("./fixtures")
    
    def test_no_arg(self):
        print("test_no_arg")
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as cm:
            self.csv_combiner.validate_args([])
        sys.stdout = sys.__stdout__ 
        self.assertIn("Enter csv files to be combined!", capturedOutput.getvalue())
        self.assertEqual(cm.exception.code, 2)

    def test_wrong_option(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as cm:
            self.csv_combiner.validate_args(['-p'])
        sys.stdout = sys.__stdout__ 
        self.assertIn(CONSTS.ARG_ERROR_MESSAGE, capturedOutput.getvalue())
        self.assertEqual(cm.exception.code, 2)

    def test_valid_output_file_properties(self):
        self.csv_combiner.validate_args(['-o', 'op', './fixtures/accessories.csv'])
        self.assertEqual(self.csv_combiner.is_file_output,True)
        self.assertEqual(self.csv_combiner.output_file,'op')

    def test_wrong_folder_path(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        with self.assertRaises(SystemExit) as cm:
            self.csv_combiner.validate_args(['--folder', './wrong-folder-path'])
        sys.stdout = sys.__stdout__ 
        self.assertIn(CONSTS.WRONG_FOLDER_MESSAGE, capturedOutput.getvalue())
        self.assertEqual(cm.exception.code, 2)

    def test_csv_in_folder(self):
        self.csv_combiner.validate_args(['--folder', './fixtures'])
        self.assertEqual(self.csv_combiner.files,['./fixtures/accessories.csv', './fixtures/clothing.csv', './fixtures/household_cleaners.csv'])

    def test_no_print_option(self):
        self.csv_combiner.validate_args(['./fixtures/clothing.csv'])
        self.assertEqual(self.csv_combiner.is_print,True)
    
    def test_print_option(self):
        self.csv_combiner.validate_args(['--no-print','-o','-op','./fixtures/clothing.csv'])
        self.assertEqual(self.csv_combiner.is_print,False)
    
    
unittest.main()