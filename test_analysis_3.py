import unittest
from typing import List
from data_loader import DataLoader
from model import Issue,State,Event,User
import config
from analysis_3 import Contributor
from analysis_3 import Analysis3

class TestAnalysis1(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.a3 = Analysis3()
        self.issues:List[Issue] = DataLoader().get_issues()

        User1:User = User()
        User1.name = "ethan"
        self.contributor1 = Contributor(User1)
        self.contributor1.record_event("reopened", self.issues[0].events[0].event_date)
        self.contributor1.record_event("reopened", self.issues[0].events[1].event_date)
        self.contributor1.record_event("closed", self.issues[0].events[1].event_date)

        User2:User = User()
        User2.name = "dimbleby"
        self.contributor2 = Contributor(User2)




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
        self.assertEqual(self.contributor1.get_first_date_str(), "2024-10-20")
    
    def test_get_last_date_str2(self):
        self.assertEqual(self.contributor2.get_first_date_str(), "N/A")    
    


if __name__ == "__main__":
    unittest.main()