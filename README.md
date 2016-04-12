# monty-hall
## monty_hall.py
This script proves the effectiveness of the switch strategy for the Monty Hall Problem. Written in Python 3.5.1, run it from the command line like so: python3 monty_hall.py (assuming monty_hall.py is in your working directory. Otherwise use an absolute path). By default the script runs 1000 trials of the simulation. If you wish to alter this behavior, alter the trials variable in main(), and run the script again.
>    def main():
>        trials = 1000
>       …

## monty_hall_test.py
This test suite tests several functions from monty_hall.py. Two functions that use random.shuffle are not tested, because mocking random.shuffle is difficult. Functions that use random.randint are successfully mocked.
