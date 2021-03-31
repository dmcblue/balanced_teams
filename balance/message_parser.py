import argparse

COMMAND_BALANCE = '!balance'
COMMAND_PLAYERS = '!players'

# https://stackoverflow.com/q/52132076/2329474
class SplitArgs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, values.split(','))

# create the top-level parser
parser = argparse.ArgumentParser(prog='PROG')

subparsers = parser.add_subparsers(help='sub-command help')

parser_players = subparsers.add_parser(
    COMMAND_PLAYERS,
    help='list players'
)
parser_players.add_argument(
    '--online',
    action='store_true',
    help='Limit responses to online players only'
)
parser_players.add_argument(
    '--known',
    action='store_true',
    help='Limit responses to players with known rankings'
)
parser_players.set_defaults(command=COMMAND_PLAYERS)

parser_balance = subparsers.add_parser(
    COMMAND_BALANCE,
    help='creates balanced teams'
)
parser_balance.add_argument(
    '--verify',
    action='store_true',
    help='System waits for emoji verification of the created teams'
)
parser_balance.add_argument(
    '--skip',
    action=SplitArgs,
    help='Comma separated Discord usernames to omit from the team calculation'
)
parser_balance.set_defaults(command=COMMAND_BALANCE)

class MessageParser:
    def __init__(self):
        self.parser = parser
    
    def parse(self, message):
        return self.parser.parse_args(message.split(' '))
