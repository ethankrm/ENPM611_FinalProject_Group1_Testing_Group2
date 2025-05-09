import unittest
from unittest.mock import patch, call
import matplotlib.pyplot as plt
import pandas as pd

from typing import List
from data_loader import DataLoader
from model import Issue,State,Event,User
import config
from analysis_3 import Contributor
from analysis_3 import Analysis3

class TestAnalysis3(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.a3 = Analysis3()
        self.issues:List[Issue] = DataLoader().get_issues()

        self.User1:User = User()
        self.User1.name = "ethan"
        self.contributor1 = Contributor(self.User1)
        self.contributor1.record_event("reopened", self.issues[0].events[0].event_date)
        self.contributor1.record_event("reopened", self.issues[0].events[1].event_date)
        self.contributor1.record_event("closed", self.issues[0].events[1].event_date)

        self.User2:User = User()
        self.User2.name = "dimbleby"
        self.contributor2 = Contributor(self.User2)




    def test_record_event1(self):
        for entry in self.contributor1.frequency_activity:
            if entry ["event_type"] == "reopened":
                self.assertEqual(entry["count"], 2)

    def test_record_event2(self):
        for entry in self.contributor1.frequency_activity:
            if entry["event_type"] == "closed":
                self.assertEqual(entry["count"], 1)

    def test_record_event3(self):
        for entry in self.contributor1.frequency_activity:
            if entry["event_type"] == "labeled":
                self.assertEqual(entry["count"], 0)

    def test_record_event4(self):
        self.contributor1.record_event("changed", self.issues[0].events[0].event_date)
        self.assertIn({'event_type': 'changed', 'count': 1}, self.contributor1.frequency_activity)


    def test_get_first_date_str1(self):
        self.assertEqual(self.contributor1.get_first_date_str(), "2024-10-20")
    
    def test_get_first_date_str2(self):
        self.assertEqual(self.contributor2.get_first_date_str(), "N/A")    

    def test_get_last_date_str1(self):
        self.assertEqual(self.contributor1.get_last_date_str(), "2024-10-20")
    
    def test_get_last_date_str2(self):
        self.assertEqual(self.contributor2.get_last_date_str(), "N/A")    
    
    @patch('builtins.print')
    def test_show_contributor_by_name1(self,mock_call):
        self.a3.show_contributor_by_name("ethan")
        mock_call.assert_called_once_with("\nContributor 'ethan' not found.")

    @patch('builtins.print')
    def test_show_contributor_by_name2(self,mock_print):
        self.a3.show_contributor_by_name("dbrtly")
        self.assertEqual(mock_print.mock_calls, [call('\nContributor: dbrtly'),
                                                call('   Total Contributions: 4'),
                                                call('   First Contribution:  2024-10-20'),
                                                call('   Last Contribution:   2024-10-20'),
                                                call('   Active Duration:     0 days'),
                                                call('   Breakdown by event type:'),
                                                call('     - labeled: 2'),
                                                call('     - subscribed: 1'),
                                                call('     - mentioned: 1')])
        
    @patch('builtins.print')
    def test_show_contributor_by_name3(self,mock_print):
        self.a3.show_contributor_by_name("dbrtly")
        self.assertEqual(mock_print.mock_calls, [call('\nContributor: dbrtly'),
                                                call('   Total Contributions: 4'),
                                                call('   First Contribution:  2024-10-20'),
                                                call('   Last Contribution:   2024-10-20'),
                                                call('   Active Duration:     0 days'),
                                                call('   Breakdown by event type:'),
                                                call('     - labeled: 2'),
                                                call('     - subscribed: 1'),
                                                call('     - mentioned: 1')])   

    @patch('builtins.print')
    def test_show_top_contributors(self,mock_print):
        self.a3.contributors = {"ethan":self.contributor1}
        self.a3.show_top_contributors()
        mock_print.assert_called()

    @patch('matplotlib.pyplot.show')
    def test_run(self,mock_show):
        self.a3.run_all_analysis()
        mock_show.assert_called_once()


if __name__ == "__main__":
    unittest.main()