def members_to_rankings(members):
    rankings = {}
    for member in members:
        rankings[member.name] = member.ranking
    return rankings

def get_team_by_member(teams, member_name):
    for team in teams:
        if any(map(lambda member: member == member_name, team[0])):
            return team
