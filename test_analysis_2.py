import unittest
from unittest.mock import patch, call
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from typing import List
from data_loader import DataLoader
from model import Issue,State,Event
import config
from analysis_2 import IssueReopenRate

class TestAnalysis2(unittest.TestCase):
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

    @patch('matplotlib.pyplot.show')
    def test_plot_reopen_rate(self,mock_show):
        rows = []
        rows.append({"kind": "test", "reopened": 0})
        rows.append({"kind": "test2", "reopened": 1})
        rows.append({"kind": "test3", "reopened": 2})
        rows.append({"kind": "test2", "reopened": 2})
        rows.append({"kind": "test4", "reopened": 0})

        df = pd.DataFrame.from_records(rows)
        df['kind'] = df['kind'].astype(str)
        label_encoder = LabelEncoder()
        df['kind_encoded'] = label_encoder.fit_transform(df['kind'])
        kind_legend = dict(enumerate(label_encoder.classes_))
        new_df = df[['kind_encoded', 'reopened']]
        predictor = new_df[['kind_encoded']]
        target = new_df['reopened']
        X_train, X_test, y_train, y_test = train_test_split(
            predictor, target,test_size=1/2, random_state=3
        )
        RFmodel = RandomForestClassifier(random_state=6)
        self.a2._plot_reopen_rate(RFmodel,new_df,kind_legend,X_train, X_test, y_train, y_test)
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_run(self,mock_show):
        self.a2.run()
        self.assertEqual(mock_show.call_count, 2)

if __name__ == "__main__":
    unittest.main()