#!/usr/bin/env python
import argparse

def add_description(description) :
    print("the description", description)

def add_amount(amount):
    print("the amount added : ", int(amount))

def listing_expenses(args=None):
    print("listing item1 ")
    print("listing item1 ")

def summary_expense(arg=None):
   print("some expenses")
       
def summary_expense_by_month(args):
    if args.month == 0:
        print("there is no month input")
        print(args)
    else:
        print(args)
        print("this month is", args.month)

def update(args):
    print("update")
    print(args)

def delete(args):
    print("delete")
    print(args)


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
    add_parser.add_argument('--description', help='add the expense description', type=add_description, required=True)
    add_parser.add_argument('--amount', help='add amount', type=add_amount, required=True)

    # subparser: listing - view
    list_parser = subparsers.add_parser('list', help='listing all the expenses recorded')
    list_parser.set_defaults(func=listing_expenses)

    # subparser : summary
    summary_parser = subparsers.add_parser('summary', help = "give a summary of all the expenses ")
    # nargs='?' means 0 or 1 argument
    summary_parser.add_argument('--month', nargs='?', const = 0, type=int)
    summary_parser.set_defaults(func=summary_expense_by_month)

    # subparser: update 
    update_parser = subparsers.add_parser('update', help="update the expenses")
    update_parser.add_argument("--id",type=int, required=True)
    update_parser.add_argument("--description", type=str )
    update_parser.add_argument("--amount",type=float)
    update_parser.set_defaults(func=update)

    #subparser: delete 
    delete_parser = subparsers.add_parser("delete", help="delete an expense")
    delete_parser.add_argument("--id", type=int, required=True)
    delete_parser.set_defaults(func=delete)

    args = parser.parse_args(command_line)
    # print("*****")
    # print(args)
    # print("*****")

    if hasattr(args, 'func'):
        args.func(args)

if __name__ == '__main__':
    main()







