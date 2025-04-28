import unittest
import json
import os
import config

class TestConfig(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        pass
    
    def test_overwrite_from_args1(self):
        dict = {"thing":None}
        config.overwrite_from_args(dict)
        
if __name__ == "__main__":
    unittest.main()