"""
pythia
"""
import sys
import argparse
try:
    from pythia.tables import evank  # noqa # pylint: disable=unused-import
except ImportError:
    from pythia.tables import badevank as evank  # noqa # pylint: disable=unused-import
from pythia import util  # noqa # pylint: disable=unused-import

###############################################################################
# Change "evank" from the line below to the name of your tables file
# from pythia.tables import template  # noqa # pylint: disable=unused-import
###############################################################################


# This is the part wher we start getting smexy
def create_argument_parser():
    """
    You should create an argument parser here.
    Copy the evank one and change only the dest variable to something else.
    """
    # Description
    parser = argparse.ArgumentParser(
        description='Pythia: Generate or roll things from TTRPG Tables')
    subparsers = parser.add_subparsers(dest='subcommand')

    # evank parser Beginning
    ###########################################################################
    if evank.AllBookTables:
        parser_evank = subparsers.add_parser('evank',
                                             help='Evank Tables')
        parser_evank.add_argument('-t',
                                  '--tables',
                                  metavar='TABLE',
                                  dest='evank_tables',
                                  nargs="*",
                                  help='Run generator on specified tables.  '
                                  + 'Prints all available tables by default.')
        parser_evank.add_argument('-p',
                                  '--preset',
                                  metavar='PRESET',
                                  dest='evank_preset',
                                  const="",
                                  nargs="?",
                                  help='Run specified preset. '
                                  + 'Prints all available presets by default.')
    ###########################################################################
    # evank parser End

    # Auto Print Help if no args passed
    if len(sys.argv) == 1:
        parser.print_help()  # Print help message if no arguments
        sys.exit(1)  # Exit the program with a non-zero status

    return parser


# Main Func
def main():
    """
    Here, you should copy the "evank" case. Change "evank" to what you chose
    your subcommand to be. Any reference to "evank" should be changed to your
    table
    """
    parser = create_argument_parser()
    args = parser.parse_args()

    match args.subcommand:
        #######################################################################
        # evank handler Beginning
        case "evank":
            # Tables arg handling
            if args.evank_tables is not None:
                print("=========")
                # Check if table provided, otherwise print all available
                # tables.
                if args.evank_tables == []:
                    print("AVAILABLE TABLES")
                    print("---------")
                    print("0: Print all tables")
                    util.print_table(evank.AllBookTables)
                    print("=========")
                else:
                    for table_name in args.evank_tables:
                        # If a table was provided check if it a request to
                        # generate from all available tables
                        if table_name in ("all", "0"):
                            util.print_random_all(evank.AllTables,
                                                  evank.AllBookTables)
                        # Otherwise
                        else:
                            util.print_random_pick(evank.AllTables,
                                                   evank.AllBookTables,
                                                   table_name)
            # Presets Handling
            if args.evank_preset is not None:
                if args.evank_preset == "":
                    print("=========")
                    print("AVAILABLE PRESETS")
                    print("---------")
                    util.print_table(evank.AllPresets)
                    print("=========")
                else:
                    util.print_random_pick(evank.AllTables,
                                            evank.AllPresets,
                                            args.evank_preset)
        #######################################################################
        # evank handler End


if __name__ == "__main__":
    main()
