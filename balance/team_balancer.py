import itertools
import logging

OFFLINE_STATUS = "offline"

def create_team_generator(player_names):
    team_combos = itertools.combinations(player_names, len(player_names)//2)
    existing_teams = []
    for team in team_combos:
        team = list(team)
        team.sort()
        opposing_team = get_opposing_team(player_names, team)
        opposing_team.sort()
        if team not in existing_teams and opposing_team not in existing_teams:
            existing_teams.append(team)
            existing_teams.append(opposing_team)
            yield team

def get_opposing_team(player_names, team):
    return list(filter(lambda name: name not in team, player_names)) 

def get_player_members(members, rankings):
    
    active_player_members = []

    for member in members:
        if member.raw_status != OFFLINE_STATUS:
            if member.name in rankings:
                active_player_members.append(member)

    return active_player_members

# Fetches a mapping of player names to their rank
# @param members Discord member objects
# @param rankings Map of player names to rank
# @return Map of player names to rank, filtered on presence online
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
    # team_combos = itertools.combinations(players, len(players)//2)
    # print(players, next(team_combos))
    team_combos = create_team_generator(players.keys())

    logging.info(f"Total ranking sum: {sum(player_rankings)}")
    logging.info(f"Target ranking for even teams: {team_ranking_target}")

    teams = {} # k=player_name, v=team_strength
    for combo in team_combos:
        team_strength = 0
        for player in combo:
            team_strength += players[player]
        # print(teams, team_strength) 
        teams.update({tuple(combo): team_strength})

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
