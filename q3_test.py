import unittest

from q3 import group_advanced_anagrams  

class TestGroupAdvancedAnagrams(unittest.TestCase):

    def test_1(self):
        words = ["bat", "Tab", "tap!", "Pat", "cat", "dog", "g.od"]
        expected_dict = {
            ('a', 'b', 't'): ["Tab", "bat"],
            ('a', 'p', 't'): ["Pat", "tap!"],
            ('d', 'g', 'o'): ["dog", "g.od"]
        }
        expected_list = [
            ["Tab", "bat"],
            ["dog", "g.od"],
            ["Pat", "tap!"]
        ]
        result = group_advanced_anagrams(words)
        self.assertEqual(result[0], expected_dict) 
        self.assertCountEqual(result[1], expected_list)  

    def test_2(self):
        words = ["listen", "silent", "enlist", "banana", "abc", "cab", "bac", "xyz"]
        expected_dict = {
            ('e', 'i', 'l', 'n', 's', 't'): ["enlist", "listen", "silent"],
            ('a', 'b', 'c'): ["abc", "bac", "cab"]
        }
        expected_list = [
            ["enlist", "listen", "silent"],
            ["abc", "bac", "cab"]
        ]
        result = group_advanced_anagrams(words)
        self.assertEqual(result[0], expected_dict) 
        self.assertCountEqual(result[1], expected_list) 

    def test_3(self):
        words = ["D.o.g", "G-o-d", "God", "dog!"]
        expected_dict = {
            ('d', 'g', 'o'): ["D.o.g", "G-o-d", "God", "dog!"]
        }
        expected_list = [
            ["D.o.g", "G-o-d", "God", "dog!"]
        ]
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_4(self):
        words = ["apple", "banana", "carrot", "date"]
        expected_dict = {}
        expected_list = []
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_5(self):
        words = []
        expected_dict = {}
        expected_list = []
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_6(self):
        words = ["!!!", "@@@", "###", "!!!"]
        expected_dict = {}
        expected_list = []
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_7(self):
        words = ["Flow", "Wolf", "woLF", "flOw"]
        expected_dict = {
            ('f', 'l', 'o', 'w'): ["Flow", "Wolf", "flOw", "woLF"]
        }
        expected_list = [
            ["Flow", "Wolf", "flOw", "woLF"]
        ]
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_8(self):
        words = ["characteristics", "tscahriceirast", "scrahticsieta", "anotherword"]
        expected_dict = {}
        expected_list = []
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_9(self):
        words = ["abc", "cab", "bac", "bca", "acb", "cba"]
        expected_dict = {
            ('a', 'b', 'c'): ["abc", "acb", "bac", "bca", "cab", "cba"]
        }
        expected_list = [
            ["abc", "acb", "bac", "bca", "cab", "cba"]
        ]
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

    def test_10(self):
        words = ["abcd", "abc", "ab", "a", "abcde"]
        expected_dict = {}
        expected_list = []
        result = group_advanced_anagrams(words)
        self.assertEqual(result, (expected_dict, expected_list))

if __name__ == "__main__":
    unittest.main()
