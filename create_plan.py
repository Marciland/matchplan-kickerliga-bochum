from file_handling import read_json_file, create_csv


def create_multiple_leagues(amount_of_leagues: int):
    teams = read_json_file('teams.json')
    matchday_dates = read_json_file('matchday_dates.json')
    for league in range(1, int(amount_of_leagues) + 1):
        league_name = str(league) + '.Liga'
        try:
            with open(league_name + '.csv', 'w', newline='',  encoding='utf-8') as file:
                create_csv(file, teams[league_name],
                           matchday_dates[league_name],
                           league_name)
            print(f'Successfully created {league_name}.csv')
        except Exception as ex:
            print(f'Failed to create: {ex}')
            raise ex


def create_single_league(league: int):
    teams = read_json_file('teams.json')
    matchday_dates = read_json_file('matchday_dates.json')
    league_name = str(league) + '.Liga'
    try:
        with open(league_name + '.csv', 'w', newline='',  encoding='utf-8') as file:
            create_csv(file, teams[league_name],
                       matchday_dates[league_name],
                       league_name)
        print(f'Successfully created {league_name}.csv')
    except Exception as ex:
        print(f'Failed to create: {ex}')
        raise ex


if __name__ == '__main__':
    while True:
        mode = input('Do you wish to create multiple leagues' +
                     ' (m) or just a specific one (s) \n' +
                     '>>> ')
        if mode != 'm' and mode != 's':
            print('Bad input')
            continue
        break
    if mode == 'm':
        while True:
            amount_of_leagues = input('Amount of leagues: \n' +
                                      '>>> ')
            try:
                amount_of_leagues = int(amount_of_leagues)
            except:
                print('Please provide a whole number')
                continue
            break
        try:
            create_multiple_leagues(amount_of_leagues)
        except:
            while True:
                inp = input('Press any key to continue')
                if inp is not None:
                    break
    elif mode == 's':
        while True:
            league = input(
                'Which league should be created? Provide a whole number: \n' +
                '>>> ')
            try:
                league = int(league)
            except:
                print('Please provide a whole number')
                continue
            break
        try:
            create_single_league(league)
        except:
            while True:
                inp = input('Press any key to continue')
                if inp is not None:
                    break
