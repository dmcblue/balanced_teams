import itertools
import logging
from balance.utils import list_partition

# Typings
TeamNames = list[str]

# Constants
OFFLINE_STATUS = "offline"

def sort_teams(teams: list[TeamNames]) -> list[TeamNames]:
    teams = map(lambda team: sorted(team), teams)
    return sorted(teams, key=lambda team: team[0])

def create_teams_from_names(names:list[str], num_teams:int) -> list[TeamNames]:
    permutations = itertools.permutations(names)
    s = set()
    for permutation in permutations:
        teams = list_partition(permutation, num_teams)
        teams = sort_teams(teams)
        teams_hash = ';'.join(map(lambda team: ','.join(team), teams))
        if teams_hash not in s:
            s.add(teams_hash)
            yield teams

def get_player_members(members, rankings):
    
    active_player_members = []

    for member in members:
        if member.raw_status != OFFLINE_STATUS:
            if member.name in rankings:
                active_player_members.append(member)

    return active_player_members

def get_player_names_rank(members, rankings):
    
    active_players = {}

    for member in members:
        if member.raw_status != OFFLINE_STATUS:
            if member.name in rankings:
                active_players.update({member.name: rankings[member.name]})
    
    return active_players

# returns 2 part tuple, first is a list of member names,
#     second the total ranking of all those members
def create_balance(members, rankings, number_of_teams_to_return):

    players = get_player_names_rank(members, rankings)

    player_rankings = players.values()
    team_ranking_target = sum(player_rankings) // 2
    team_combos = itertools.combinations(players, len(players)//2)

    logging.info(f"Total ranking sum: {sum(player_rankings)}")
    logging.info(f"Target ranking for even teams: {team_ranking_target}")

    teams = {} # k=player_name, v=team_strength
    for combo in team_combos:
        team_strength = 0
        for player in combo:
            team_strength += players[player]
        
        teams.update({combo: team_strength})

    sorted_teams = sorted(teams.items(), key=lambda x: abs(x[1] - team_ranking_target), reverse=False)

    balanced_teams = sorted_teams[0:number_of_teams_to_return]

    for i in range(len(balanced_teams)):
        team = balanced_teams[i]
        logging.info(f"Team {i + 1}")
        logging.info(f"  Members: {', '.join(team[0])}")
        logging.info(f"  Rank:    {team[1]}")
        logging.info(f"  Error:   {abs(team[1] - team_ranking_target)}")

    return balanced_teams

def create_bros_balance():
    return
