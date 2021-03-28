from balance.utils import list_intersection

class Application:
    def __init__(self, rankings):
        self.rankings = rankings
    
    def get_known_players(self):
        return list(self.rankings)
    
    def get_online_players(self, members):
        return list(map(lambda member: member.name, filter(lambda member: member.raw_status != "offline", members)))

    def get_member_list(self, members):
        return list(map(lambda member: member.name, members))

    # parsed_message: Namespace https://docs.python.org/3/library/argparse.html#argparse.Namespace
    def get_players(self, parsed_message, members):
        players = self.get_member_list(members)
        if parsed_message.known:
            players = list_intersection(players, self.get_known_players())

        if parsed_message.online:
            players = list_intersection(players, self.get_online_players(members))

        return players
