import sys

import modules.plan_handler as plan_handler


def create_csv_format(teams: list, matchday_dates: list, league: str):
    csv = []
    plan = plan_handler.create_plan(teams)
    if len(plan) != len(matchday_dates):
        print('Amount of matchday_dates is not equal ' +
              f'to the amount of matchdays in league: {league}!')
        print(f'Required amount of dates: {len(plan)}\n' +
              f'Provided amount of dates: {len(matchday_dates)}')
        sys.exit(1)
    # uncomment to write matchplan to json (useful in website backend? can replace csv)
    # with open(f'{league}_plan.json', 'w') as file:
    #     json.dump(plan, file, indent=4)
    match_counter = 0
    for matchday in range(int((len(teams) * 2 - 2))):
        for match in range(int(len(teams)/2)):
            csv.append(f'{matchday_dates[matchday]},' +
                       '20:00:00,' +
                       f'{plan[matchday+1][match]["Spielort"]},' +
                       f'{plan[matchday+1][match]["Gastgeber"]},' +
                       f'{plan[matchday+1][match]["Gast"]},' +
                       str(matchday+1))
            match_counter += 1
    return csv
