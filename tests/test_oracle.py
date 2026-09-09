import importlib.util
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("runner",ROOT/"tools/conformance.py")
runner=importlib.util.module_from_spec(spec); spec.loader.exec_module(runner)

class OracleTests(unittest.TestCase):
    def test_smoke_sources_are_nonempty(self):
        self.assertTrue(all(c["text"] for c in runner.smoke_cases()))

    def test_json_structural_equivalence(self):
        self.assertEqual(runner.compare('{"a": [1, true]}','{ "a" : [ 1,true ] }')[0],"pass")

    def test_json_difference_is_visible(self):
        self.assertEqual(runner.compare('{"a":1}','{"a":2}')[0],"semantic-difference")

    def test_duplicate_keys_are_rejected(self):
        with self.assertRaises(ValueError): runner.json_value('{"a":1,"a":2}')
if __name__=="__main__": unittest.main()
