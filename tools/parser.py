import sys
import argparse

def parse_args():
    # replace -h with help
    if '-h' in sys.argv or '--help' in sys.argv:
        sys.argv = [sys.argv[0], 'help']

    # parse arguments
    parser = argparse.ArgumentParser(description='Bot run or setup options.')
    
    # add setup/run subcommand
    parser.add_argument('mode', nargs='?', help='Mode :\n- setup: set the token and an optional password\n- run: run the bot\n- test: check if a password is correct\n- help: displays this message', choices=['setup', 'run', 'test', 'help'])

    # create category for run subcommands
    run_group = parser.add_argument_group('Run parameters')

    # add password flag for run (catch the first argument after the flag)
    run_group.add_argument('-p', '--password', type=str, help='Use a password (with or without providing in CL)', nargs=1)

    # add debug category
    debug_group = parser.add_argument_group('Debug parameters')

    # parse arguments
    args = parser.parse_args()

    if args.mode == 'help':
        parser.print_help()
        sys.exit(0)

    return args