import unittest
from typing import List
from data_loader import DataLoader
from model import Issue,State,Event
import config
from analysis_1 import EngagementResolutionAnalysis

class TestAnalysis1(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.a1 = EngagementResolutionAnalysis()
        self.issues:List[Issue] = DataLoader().get_issues()


    def test_get_comment_count1(self):
        blank_issue:Issue = Issue()
        self.assertEqual(self.a1._get_comment_count(blank_issue), 0)
    
    def test_get_comment_count2(self):     
        self.assertEqual(self.a1._get_comment_count(self.issues[0]), 1)

    def test_get_resolution_time1(self):
        blank_issue:Issue = Issue()
        self.assertEqual(self.a1._get_resolution_time(blank_issue), None)
    
    def test_get_resolution_time2(self):     
        self.assertEqual(self.a1._get_resolution_time(self.issues[0]), 0)

if __name__ == "__main__":
    unittest.main()