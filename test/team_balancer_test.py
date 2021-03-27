import unittest
import logging
from team_balancer import get_player_members, get_player_names_rank, create_balance, create_bros_balance
import mocks
from utils import get_team_by_member, members_to_rankings

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


if __name__ == '__main__':
    unittest.main()
