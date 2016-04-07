# FIXTestTask
Test task for FIX company. This python module simulates night club with visitors and songs. Visitors can dance
or can buhat'. This module simulates this process.

## Usage
In root repo directory run `python3 -m fix_task [-h] [-v VISITORS] [-s SONGS] [-d DURATION]`.

    optional arguments:
    -h, --help   show this help message and exit
    -v VISITORS  Number of visitors in club. Default 5
    -s SONGS     Number of songs in club. Default 5
    -d DURATION  Maximum duration of song in club. Default 3


## Tests
In root repo directory run `python3 -m unittest discover tests -v`.