def create_empty_plan(amount_of_teams: int):
    plan = {}
    for matchday in range(1, amount_of_teams * 2 - 1):
        plan[matchday] = []
        for _ in range(int(amount_of_teams / 2)):
            plan[matchday].append({'Spielort': '',
                                   'Gastgeber': '',
                                   'Gast': ''})
    return plan


def create_first_half(plan: dict, teams: list):
    matchdays = len(teams) - 1
    for matchday in range(1, len(teams)):
        home = len(teams)
        away = matchday

        if matchday % 2 != 0:
            temp = away
            away = home
            home = temp

        plan[matchday][0]['Spielort'] = teams[home-1]['Spielort']
        plan[matchday][0]['Gastgeber'] = teams[home-1]['Name']
        plan[matchday][0]['Gast'] = teams[away-1]['Name']

        for match in range(1, int(len(teams) / 2)):
            if matchday - match < 0:
                away = matchdays + (matchday - match)
            else:
                away = (matchday - match) % matchdays
                away = matchdays if away == 0 else away

            home = (matchday + match) % matchdays
            home = matchdays if home == 0 else home

            if match % 2 == 0:
                temp = away
                away = home
                home = temp

            plan[matchday][match]['Spielort'] = teams[home-1]['Spielort']
            plan[matchday][match]['Gastgeber'] = teams[home-1]['Name']
            plan[matchday][match]['Gast'] = teams[away-1]['Name']
    return plan


def create_second_half(plan: dict, teams: list):
    matchdays = len(teams) - 1
    for matchday in range(1, matchdays + 1):
        for match in range(int(len(teams) / 2)):
            plan[matchday+matchdays][match]['Gastgeber'] = plan[matchday][match]['Gast']
            plan[matchday+matchdays][match]['Gast'] = plan[matchday][match]['Gastgeber']
            location = 'If you read this in your csv message me with an error report containing both jsons!'
            for team in teams:
                if plan[matchday+matchdays][match]['Gastgeber'] is team['Name']:
                    location = team['Spielort']
            plan[matchday+matchdays][match]['Spielort'] = location
    return plan


def create_plan(teams: list):
    if len(teams) % 2 != 0:
        return create_odd_plan(teams)
    plan = create_empty_plan(len(teams))
    plan = create_first_half(plan, teams)
    plan = create_second_half(plan, teams)
    return plan


def create_odd_plan(teams: list):
    teams.append({'Name': 'Dummy', 'Spielort': 'Dummy'})
    return create_plan(teams)
