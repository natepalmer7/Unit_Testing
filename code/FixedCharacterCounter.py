  #!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler, David Knox
# Summer 2014, 2022
# CSCI 3308
# Univerity of Colorado
# Tests for Character Counting Module

import unittest
from CharacterCounter import *

class CharCounterTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        
        # create an object that we will use in this testing
        p = CharacterCounter(text)
        
        # use the testing framework assertions to check results
        self.assertEqual(p.text, text, "'text' does not match input")
        
        # need to test that an exception is raised when given a bad parameter!
        # any other tests?
        
        

    # Add Your Test Cases Here...
    def test_constructor(self):
        test_str = "test: integer input"
        with self.assertRaises(CharacterCounter.CharacterCounterError, msg="Failed " + test_str):
            CharacterCounter(123)

        test_str = "test: list input"
        with self.assertRaises(CharacterCounter.CharacterCounterError, msg="Failed " + test_str):
            CharacterCounter([1, 2, 3])

        test_str = "test: dictionary input"
        with self.assertRaises(CharacterCounter.CharacterCounterError, msg="Failed " + test_str):
            CharacterCounter({"a": 1, "b": 2})


        
    def test_count(self):
        test_str = "test: empty string"
        counter = CharacterCounter("")
        expected_result = {}
        self.assertEqual(counter.count(), expected_result, "Failed " + test_str)

        test_str = "test: single character"
        counter = CharacterCounter("a")
        expected_result = {'a': 1}
        self.assertEqual(counter.count(), expected_result, "Failed " + test_str)

        test_str = "test: multiple characters"
        counter = CharacterCounter("hello world")
        expected_result = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        self.assertEqual(counter.count(), expected_result, "Failed " + test_str)
        
    def test_count_alphabetic(self):
        test_str = "test: empty string"
        counter = CharacterCounter("")
        expected_result = 0
        self.assertEqual(counter.count_alpha(), expected_result, "Failed " + test_str)

        test_str = "test: single alphabetic character"
        counter = CharacterCounter("a")
        expected_result = 1
        self.assertEqual(counter.count_alpha(), expected_result, "Failed " + test_str)

        test_str = "test: multiple characters with alphabetic and non-alphabetic"
        counter = CharacterCounter("hello world123")
        expected_result = 10
        self.assertEqual(counter.count_alpha(), expected_result, "Failed " + test_str)
        
    def test_count_numeric(self):
        test_str = "test: empty string"
        counter = CharacterCounter("")
        expected_result = 0 
        self.assertTrue(counter.count_numeric() == expected_result, "Failed " + test_str)

        test_str = "test: single numeric character"
        counter = CharacterCounter("1")
        expected_result = 1
        self.assertTrue(counter.count_numeric() == expected_result, "Failed " + test_str)

        test_str = "test: multiple characters with numerics and non-numerics"
        counter = CharacterCounter("hello world123")
        expected_result = 3
        self.assertTrue(counter.count_numeric() == expected_result, "Failed " + test_str)
        
    def test_count_vowels(self):
        test_str = "test: empty string"
        counter = CharacterCounter("")
        expected_result = 0
        self.assertTrue (counter.count_vowels() == expected_result, "Failed " + test_str)

        test_str = "test: single vowel character"
        counter = CharacterCounter("a")
        expected_result = 1
        self.assertTrue (counter.count_vowels() == expected_result, "Failed " + test_str)

        test_str = "test: multiple characters with vowels and non-vowels"
        counter = CharacterCounter("hello world123")
        expected_result = 3
        self.assertTrue (counter.count_vowels() == expected_result, "Failed " + test_str)
        
    def test_is_phonenumber(self):
        test_str = "test: empty string"
        counter = CharacterCounter("")
        expected_result = False
        self.assertEqual(counter.is_phonenumber(), expected_result, "Failed " + test_str)

        test_str = "test: invalid phone number"
        counter = CharacterCounter("1234567890")
        expected_result = False
        self.assertEqual(counter.is_phonenumber(), expected_result, "Failed " + test_str)

        test_str = "test: valid phone number"
        counter = CharacterCounter("(123) 456-7890")
        expected_result = False
        self.assertEqual(counter.is_phonenumber(), expected_result, "Failed " + test_str)
        
        
        
    
    
     
        

        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # here is an example way to write tests.  You can do it other ways as well.
    # THIS IS NOT A GOOD SET OF TESTS, JUST AN EXAMPLE
    #
    def test_alpha(self):
        # each element of the tests list is also a list which has [test string, expected value, message]
        tests = [
            ["aaaa",       4, "did not find all occurrences of single char"],
            ["a        b", 2, "did not find first and last character of string"],
            ["az",         2, "did not detect a and/or z"],
            ["(a1)",       1, "did not detect handle string with alpha, digit, paren" ],
            ["1239093",    0, "found alpha in digits only string"]
        ]
        
        for test in tests:
            # create a new object for each test
            my_obj = CharacterCounter(test[0])
            
            # check that the results are as expected
            self.assertEqual(my_obj.count_alpha(), test[1], test[2])
            
    # add methods for other functions that need to be tested ...
            
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
