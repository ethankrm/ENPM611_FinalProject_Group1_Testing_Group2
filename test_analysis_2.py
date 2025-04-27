import unittest
from typing import List
from data_loader import DataLoader
from model import Issue,State,Event
import config
from analysis_2 import IssueReopenRate

class TestAnalysis1(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.a2 = IssueReopenRate()
        self.issues:List[Issue] = DataLoader().get_issues()

    def test_extract_kind1(self):
        blank_issue:Issue = Issue()
        self.assertEqual(self.a2._extract_kind(blank_issue.labels), 'unknown')

    def test_extract_kind2(self):
        self.assertEqual(self.a2._extract_kind(self.issues[0].labels), 'bug')

    def test_extract_kind3(self):
        self.assertEqual(self.a2._extract_kind(self.issues[1].labels), 'unknown')

    def test_check_reopened1(self):
        blank_issue:Issue = Issue()
        self.assertEqual(self.a2._check_reopened(blank_issue), 0)
    
    def test_check_reopened2(self):     
        self.assertEqual(self.a2._check_reopened(self.issues[0]), 0)

    def test_check_reopened3(self):  
        for issue in self.issues:
            if 9721 == issue.number:
                test_issue = issue
        self.assertEqual(self.a2._check_reopened(test_issue), 1)


if __name__ == "__main__":
    unittest.main()