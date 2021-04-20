import unittest
import logging
from balance.team_balancer import create_balance, \
                                  create_bros_balance, \
                                  create_teams_from_names, \
                                  get_player_members, \
                                  get_player_names_rank, \
                                  sort_teams
import mocks
from test_utils import get_team_by_member, members_to_rankings

# Uncomment to show debug output
# logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

class TestTeamBalancer(unittest.TestCase):

    def test_create_balance(self):
        members = [
            mocks.Member("Pound", True, 1),
            mocks.Member("Bang", True, 2),
            mocks.Member("Bupkus", True, 3),
            mocks.Member("Blanko", True, 4),
            mocks.Member("Nawt", False, 5)
        ]
        rankings = members_to_rankings(members)
        teams = create_balance(members, rankings, 2)
        team1 = get_team_by_member(teams, "Pound")
        team2 = get_team_by_member(teams, "Bang")
        self.assertTrue("Blanko" in team1[0])
        self.assertTrue("Bupkus" in team2[0])
        self.assertEqual(5, team1[1])
        self.assertEqual(5, team2[1])

    def test_create_teams_from_names(self):
        names = [
            'Reggie Dunlop',
            'Ned Braden',
            'Jeff Hanson',
            'Steve Hanson',
            'Jack Hanson'
        ]
        teams = list(create_teams_from_names(names, 2))
        # It would be hard to test this with out a large
        # expected data set, so lets just check number of results
        # For 2 teams, with odd number of players (N),
        # the result set _should_ match "N choose 2".
        self.assertEqual(10, len(teams))

        # for 3 teams from 5 people, we get 15 teams
        # manually calced, not sure the forumula
        teams = list(create_teams_from_names(names, 3))
        self.assertEqual(15, len(teams))

        teams = list(create_teams_from_names(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2))
        self.assertEqual(35, len(teams))


    def test_sort_teams(self):
        teams = [
            ['z', 'f', 'g'],
            ['a', 'x', 'd'],
            ['c', 'b']
        ]
        expected = [
            ['a', 'd', 'x'],
            ['b', 'c'],
            ['f', 'g', 'z']
        ]
        actual = sort_teams(teams)
        self.assertEqual(len(expected), len(actual))
        for index in range(0, len(actual)):
            self.assertEqual(expected[index], actual[index])

if __name__ == '__main__':
    unittest.main()
