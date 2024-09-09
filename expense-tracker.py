#!/usr/bin/env python
import argparse
import json
import os

# functions 
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


def write_object_to_json(fn,data):
    # check if file exists
    # if file does not exist
    file_path = '../expense-tracker/' + fn

    if os.path.isfile(file_path) == False or os.stat(fn).st_size == 0 :  # if file does not already exist, or file is empty 
        content = []
        content.append(data)
        with open(fn,'w') as outfile:
            json.dump(content,outfile)
    else: # file does exist
        file = open(fn)
        content = json.load(file)
        content.append(data)
        with open(fn, 'w') as outfile:
            json.dump(content,outfile)


def read_from_json(fn):
    file_path = '../expense-tracker/' + fn
    if os.path.isfile(file_path) == True:
        file = open(fn)
        data = json.load(file)
        return data
    else:
        return fn + " does not exist"



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

"""
[
    {
        "name":"lemon",
        "age":23
    },
    {
        "name":"Lyra",
        "age":21
    }
]

"""







