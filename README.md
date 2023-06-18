# Matchplan creation script for Kickerliga-Bochum
This script is used to create matchplans for the [Kickerliga-Bochum](https://kickerliga-bochum.de/).<br>
I decided to use python for this task purely out of convenience.<br>
I also avoided external libraries to ensure an easy use.<br>

I will provide a self-containing executable to allow execution without installation of python.

While implementing the desired features i was troubled with creating <br> a matchplan that ensures as little breaks as possible. <br>
(it is called a break if your team has to play at home or abroad twice in a row)

What helped me solve the problem: [the algorithm](https://docplayer.org/24818670-36-algorithmus-der-woche-turnier-und-sportligaplanung.html) (german)

## How to run the script:
Download this repository either by clicking <> Code and selecting Download ZIP <br>
or clone the repository with git.

If you decide to download the zip archive you need to extract the files before using the script.

Either install [python](https://www.python.org/downloads/) (tested in 3.11.4) and manually run the following command: <br>
- python [path/to/create_plan.py](create_plan.py)

or run the [create_plan.exe](create_plan.exe) <br>
_(since this is self-contained, there will be a tmp folder created at runtime. This should delete itself. If it stays, you can safely remove it after the script exited.)_

Before you can run the script properly you should modify the [matchday_dates.json](matchday_dates.json) and [teams.json](teams.json) accordingly.

- fill teams with Name and Spielort (location)
- fill matchday_dates with timestamps DD/MM/YYYY

The script will prompt you whether a matchplan for one or multiple leagues should be created.

Input 's' followed by a number to create just the specified league. <br>
- eg: -> s -> 3 => 3.Liga.csv created

Input 'm' followed by a number to create the specified amount of leagues. <br>
- eg: -> m -> 3 => 1.Liga.csv & 2.Liga.csv & 3.Liga.csv created

## How to build a modified executable:

If you want to make any changes to the script and rebuild the executable you need
- [python installation](https://www.python.org/downloads/) and [pyinstaller](https://pyinstaller.org/en/stable/index.html). <br>

_(at this point you realize that you do not need the exe because you installed python)_

- run pyinstaller --onefile --runtime-tmpdir . path\to\create_plan.py

## Troubleshooting:
Since we are a german Kickerliga some parts are in german to support those with not as much english knowledge. <br>
Therefore here are some translations:
- Liga = league
- Spielort = location of play
- Gastgeber = host
- Gast = visitor

Most information is logged to console by the script. <br>
Possible problems:
- bad format in a json <br>
==> stay true to the format provided here
- differences in matchday_dates amount and matchday_amount <br>
==> add/remove entries in matchday_dates or add/remove teams for the league
- creating a league without specifying it in the json before <br>
==> the script will read the jsons at given position. eg if you want to create 5 leagues you have to provide atleast 5 leagues in the json file

If you come across any errors that you cannot solve yourself <br>
please open an issue on github with as many information as possible.
