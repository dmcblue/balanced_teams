import unittest
import logging
from balance.team_balancer import get_player_members, get_player_names_rank, create_balance, create_bros_balance, create_team_generator
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

    def test_create_team_generator(self):
        player_names = [
            "Arachneon",
            "Armo",
            "Growtreant",
            "Lazar",
            "Thorias",
            "Fry"
        ]
        team_generator = create_team_generator(player_names)
        count = 0
        for team in team_generator:
            print(team)
            count += 1
        # 6 choose 3 or 6! / (3! * (6 - 3)!)
        # then divide by 2
        expected_team_size = (720 / (6 * 6)) / 2
        self.assertEqual(expected_team_size, count)
        # print(team_generator.__next__())
        # print(team_generator.__next__())

    def test_player_names_rank(self):
        # get_player_names_rank(members, rankings):
        members = [
            mocks.Member("Pound", True, 1),
            mocks.Member("Bang", True, 2),
            mocks.Member("Bupkus", True, 3),
            mocks.Member("Blanko", True, 4),
            mocks.Member("Nawt", False, 5)
        ]
        rankings = members_to_rankings(members)
        rank_mapping = get_player_names_rank(members, rankings)
        self.assertEqual({"Pound": 1, "Bang": 2, "Bupkus": 3, "Blanko": 4}, rank_mapping)


if __name__ == '__main__':
    unittest.main()
