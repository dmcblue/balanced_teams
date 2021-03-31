import unittest
import logging
import mocks
# from balance import message_parser
from balance.message_parser import MessageParser
from balance.application import Application
from test_utils import get_team_by_member, members_to_rankings

class GetPlayersTest:
    def __init__(self, message, expected_players):
        self.message = message
        self.players = expected_players

class TestApplication(unittest.TestCase):

    def test_get_players(self):
        members = [
            mocks.Member("Daphne", True, 1),
            mocks.Member("Fred", True, 2),
            mocks.Member("Scooby", True, 3),
            mocks.Member("Shaggy", False, 4),
            mocks.Member("Vera", False, 5)
        ]
        rankings = members_to_rankings(members)
        del rankings["Scooby"]
        del rankings["Vera"]
        application = Application(rankings)
        parser = MessageParser()
        tests = [
            GetPlayersTest('!players', ["Daphne", "Fred", "Scooby", "Shaggy", "Vera"]),
            GetPlayersTest('!players --known', ["Daphne", "Fred", "Shaggy"]),
            GetPlayersTest('!players --online', ["Daphne", "Fred", "Scooby"]),
            GetPlayersTest('!players --known --online', ["Daphne", "Fred"])
        ]
        for test in tests:
            message = parser.parse(test.message)
            players = application.get_players(message, members)
            self.assertEqual(set(test.players), set(players), test.message)


if __name__ == '__main__':
    unittest.main()
