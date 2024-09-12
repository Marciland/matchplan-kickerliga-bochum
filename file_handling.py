import json
import sys
import csv

from plan_handler import create_plan


def read_json_file(file: str):
    try:
        with open(file, 'r', encoding='utf-8') as file_handle:
            content = json.load(file_handle)
        print(f'Successfully read from {file}!')
        return content
    except Exception as ex:
        print(f'Failed to read from {file}! Following Error occured:\n{ex}')
        sys.exit(1)


def create_csv(file, teams: list, matchday_dates: list, league: str):
    plan = create_plan(teams)
    if len(plan) != len(matchday_dates):
        print('Amount of matchday_dates is not equal ' +
              f'to the amount of matchdays in league: {league}!')
        print(f'Required amount of dates: {len(plan)}\n' +
              f'Provided amount of dates: {len(matchday_dates)}')
        sys.exit(1)

    writer = csv.writer(file)
    writer.writerow(['Date', 'Time', 'Venue', 'Home',
                     'Away'])

    for matchday in range(int((len(teams) * 2 - 2))):
        for match in range(int(len(teams)/2)):
            writer.writerow([f'{matchday_dates[matchday]}', '20:00:00',
                            f'{plan[matchday+1][match]["Spielort"]}',
                             f'{plan[matchday+1][match]["Gastgeber"]}',
                             f'{plan[matchday+1][match]["Gast"]}',
                             str(matchday+1)])
