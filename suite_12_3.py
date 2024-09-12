import unittest
from MOD_12_tests_12_3 import RunnerTest, TournamentTest

loader = unittest.TestLoader()

test_s = unittest.TestSuite()
test_s.addTests(loader.loadTestsFromTestCase(RunnerTest))
test_s.addTests(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_s)