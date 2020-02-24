import unittest
from data7project.scripts.pull_scripts.pull_txt import PullTxt


class CsvTest(unittest.TestCase):

    def test_csv(self):
        try:
            x = PullTxt("data7-engineering-project")
            x = x.pull("SpartaDays", "Sparta Day 1 August 2019.txt")
            return x
        except Exception:
            raise AssertionError('Text file not found')


