import unittest
from MOD_12_tests_12_2 import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        runner = Runner('Emily')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner2 = Runner('James')
        for _ in range(10):
            runner2.run()
        self.assertEqual(runner2.distance, 100)

    def test_challenge(self):
        runner3 = Runner('Lily')
        runner4 = Runner('Michael')
        for _ in range(10):
            runner3.run()
            runner4.walk()
        self.assertNotEqual(runner3.distance, runner4.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Usain', 10)
        self.andrey = Runner('Andrey', 9)
        self.nick = Runner('Nick', 3)

    @classmethod
    def tearDownClass(cls):
        for key, result in cls.all_results.items():
            finishers = list(result.values())
            finisher_names = {i + 1: str(finisher) for i, finisher in enumerate(finishers)}
            print(finisher_names)

    def test_race_usain_nick(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        tournament = Tournament(90, self.usain, self.nick)
        self.all_results[1] = tournament.start()
        self.assertTrue(list(self.all_results[1].values())[-1] == 'Nick')

    def test_race_andrey_nick(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        tournament = Tournament(90, self.andrey, self.nick)
        self.all_results[2] = tournament.start()
        self.assertTrue(list(self.all_results[2].values())[-1] == 'Nick')

    def test_race_usain_andrey_nick(self):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        self.all_results[3] = tournament.start()
        self.assertTrue(list(self.all_results[3].values())[-1] == 'Nick')

