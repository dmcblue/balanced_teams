from balance.utils import list_intersection
from balance.team_balancer import create_balance, OFFLINE_STATUS

class Application:
    def __init__(self, rankings):
        self.rankings = rankings
    
    def get_known_players(self):
        return list(self.rankings)
    
    def get_online_players(self, members):
        return list(map(lambda member: member.name, filter(lambda member: member.raw_status != OFFLINE_STATUS, members)))

    def get_member_list(self, members):
        return list(map(lambda member: member.name, members))

    def is_valid_member(self, member):
        return member.raw_status != OFFLINE_STATUS and member.name in self.get_known_players()

    def get_valid_members(self, members):
        return filter(self.is_valid_member, members)

    # parsed_message: Namespace https://docs.python.org/3/library/argparse.html#argparse.Namespace
    def get_players(self, parsed_message, members):
        players = self.get_member_list(members)
        if parsed_message.known:
            players = list_intersection(players, self.get_known_players())

        if parsed_message.online:
            players = list_intersection(players, self.get_online_players(members))

        return players
