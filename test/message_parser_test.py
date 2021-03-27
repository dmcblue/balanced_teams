import unittest
import logging
from message_parser import MessageParser

class PlayerTest:
    def __init__(self, message: str, online: bool, known: bool):
        self.message = message
        self.known = known
        self.online = online

class BalanceTest:
    def __init__(self, message: str, skip: list[str], verify: bool):
        self.message = message
        self.skip = skip
        self.verify = verify

class TestMessageParser(unittest.TestCase):

    def test_players(self):
        parser = MessageParser()
        tests = [
            PlayerTest('!players', False, False),
            PlayerTest('!players --known', False, True),
            PlayerTest('!players --online', True, False),
            PlayerTest('!players --online --known', True, True)
        ]
        for test in tests:
            parsed = parser.parse(test.message)
            self.assertEqual('!players', parsed.command)
            self.assertEqual(test.known, parsed.known)
            self.assertEqual(test.online, parsed.online)

    def test_balance(self):
        parser = MessageParser()
        tests = [
            BalanceTest('!balance', None, False),
            BalanceTest('!balance --skip asterix,obelix', ['asterix', 'obelix'], False),
            BalanceTest('!balance --verify', None, True),
            BalanceTest('!balance --skip asterix,obelix --verify', ['asterix', 'obelix'], True)
        ]
        for test in tests:
            parsed = parser.parse(test.message)
            self.assertEqual('!balance', parsed.command)
            self.assertEqual(test.skip, parsed.skip)
            self.assertEqual(test.verify, parsed.verify)

if __name__ == '__main__':
    unittest.main()
