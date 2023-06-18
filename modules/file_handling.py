import json
import sys


def read_json_file(file: str):
    try:
        with open(file, 'r') as hFile:
            content = json.load(hFile)
        print(f'Successfully read from {file}!')
        return content
    except Exception as ex:
        print(f'Failed to read from {file}! Following Error occured:\n{ex}')
        sys.exit(1)


def write_file(file_name: str, file_content: list):
    with open(file_name + '.csv', 'w') as file:
        file.writelines(line + '\n' for line in file_content)
    print(f'Successfully created {file_name}.csv')
