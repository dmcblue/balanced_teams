import unittest
import logging
from balance.team_balancer import create_balance, \
                                  create_bros_balance, \
                                  create_teams_from_names, \
                                  get_balance_rank, \
                                  get_player_members, \
                                  get_player_names_rank, \
                                  get_team_rank, \
                                  rank_balances, \
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

    def test_get_balance_rank(self):
        rankings = {
            "Jeffrey Lebowski": 5,
            "Walter Sobchak": 3,
            "Donny Kerabatsos": 4,
            "Uli Kunkel": 4,
            "Franz": 3,
            "Dieter": 2,
            "Jesus Quintana": 5,
            "Liam O'Brien": 4
        }
        teams = [
            ["Jeffrey Lebowski", "Walter Sobchak", "Donny Kerabatsos"],
            ["Uli Kunkel", "Franz", "Dieter"],
            ["Jesus Quintana", "Liam O'Brien"]
        ]
        rank = get_balance_rank(teams, rankings)
        # total = 30
        # per team = 10
        # team 1 = 12
        # team 2 = 9
        # team 3 = 9
        self.assertEqual(4, rank)

    def test_get_team_rank(self):
        rankings = {
            "Jeffrey Lebowski": 5.1,
            "Walter Sobchak": 3.4,
            "Donny Kerabatsos": 4.8,
            "Uli Kunkel": 4.75,
            "Franz": 3.2,
            "Dieter": 2.8,
            "Jesus Quintana": 5.1,
            "Liam O'Brien": 3.3
        }
        ranking = get_team_rank(
            ["Jeffrey Lebowski", "Walter Sobchak", "Donny Kerabatsos"],
            rankings
        )
        self.assertEqual(13.3, ranking)

    def test_rank_balances(self):
        rankings = {
            "Jeffrey Lebowski": 5,
            "Walter Sobchak": 3,
            "Donny Kerabatsos": 4,
            "Uli Kunkel": 3,
            "Franz": 3,
            "Dieter": 2,
            "Jesus Quintana": 5,
            "Liam O'Brien": 4
        }
        balances = [
            [["Uli Kunkel", "Jeffrey Lebowski"],
                ["Franz", "Donny Kerabatsos"]],
            [["Jeffrey Lebowski", "Donny Kerabatsos"],
                ["Uli Kunkel", "Franz"]]
        ]
        ranks = rank_balances(balances, rankings)

        self.assertEqual(2, len(ranks))
        # results should be ordered by rank
        first_balance = ranks[0]
        self.assertEqual(2, len(first_balance[0])) # 2 teams
        self.assertEqual(3.0, first_balance[1]) # balance rank
        self.assertEqual(balances[1], first_balance[0]) # team composition
        second_balance = ranks[1]
        self.assertEqual(2, len(second_balance[0])) # 2 teams
        self.assertEqual(1.0, second_balance[1]) # balance rank
        self.assertEqual(balances[0], second_balance[0]) # team composition


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
