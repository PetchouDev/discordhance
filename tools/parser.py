import argparse

def parse_args():
    # parse arguments
    parser = argparse.ArgumentParser(description='Bot run or setup options.')
    
    # add setup subcommand
    parser.add_argument('-s', '--setup', action='store_true', help='Setup the bot.')

    # add run subcommand (default)
    parser.add_argument('-r', '--run', action='store_true', help='Run the bot.')

    # add password flag for run (catch the first argument after the flag)
    parser.add_argument('-p', '--password', type=str, help='Use a password (with or without providing in CL)', nargs=1)

    # add test subcommand
    parser.add_argument('-t', '--test', action='store_true', help='Test if password is correct.')

    # parse arguments
    args = parser.parse_args()

    return args