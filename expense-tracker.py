#!/usr/bin/env python
import argparse
import helper_functions


# main function
def main(command_line=None):
    # instantiate a parser 
    parser = argparse.ArgumentParser(
        prog="expense-tracker",
        description="This CLI helps track your spending and expenses"
    )

    # subparsers for subcommands
    subparsers = parser.add_subparsers(dest="command",help="a list of commands")

    # subparser: add
    add_parser = subparsers.add_parser('add', help='add an expense to track')
    add_parser.add_argument('--description', help='add the expense description', type=str, required=True)
    add_parser.add_argument('--amount', help='add amount', type=float, required=True)
    add_parser.set_defaults(func=helper_functions.adding_expense)

    # subparser: listing - view
    list_parser = subparsers.add_parser('list', help='listing all the expenses recorded')
    list_parser.set_defaults(func=helper_functions.listing_expenses)

    # subparser : summary
    summary_parser = subparsers.add_parser('summary', help = "give a summary of all the expenses ")
    # nargs='?' means 0 or 1 argument
    summary_parser.add_argument('--month', nargs='?', const = 0, type=int)
    summary_parser.set_defaults(func=helper_functions.summary_expense)

    # subparser: update 
    update_parser = subparsers.add_parser('update', help="update the expenses")
    update_parser.add_argument("--id",type=int, required=True)
    update_parser.add_argument("--description", type=str )
    update_parser.add_argument("--amount",type=float)
    update_parser.set_defaults(func=helper_functions.update)

    #subparser: delete 
    delete_parser = subparsers.add_parser("delete", help="delete an expense")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=helper_functions.delete)

    args = parser.parse_args(command_line)
    

    if hasattr(args, 'func'):
        args.func(args)


if __name__ == '__main__':
    main()









