
import json
import os
from datetime import date

# functions 
def adding_expense(args=None):
    desc = args.description
    amount = args.amount
    current_data = read_from_json('data.json')
    
    # construct the data object
    id = len(current_data) + 1
    
    day = f"{date.today().year}/{date.today().month}/{date.today().day}"

    data_obj = {
        "id":id,
        "date":day,
        "description":desc,
        "amount":amount
    }

    write_object_to_json('data.json',data_obj )
    print("adding an expense",desc,amount)

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
    id = args.id
    desc = args.description
    amount = args.amount
    # make sure id is valid 
    
    data = read_from_json('data.json')
    if id <= 0 or id > len(data):
        print("please enter a valid id")
    else:
        for i in range(len(data)):
            if(id == data[i]["id"]):
                print("id and index is", id)
                print("data obj is", data[i])
                if desc != None:
                    data[i]["description"] = desc
                if amount != None:
                    data[i]["amount"] = amount
                with open('data.json','w') as outfile:
                    json.dump(data,outfile)
    
    print("id",id,"desc",desc,"amount",amount)

def delete(args):
    print("delete")
    data = read_from_json('data.json')
    if(len(data) == 0):
        print("it is already empty")
    else:
        # check if id is valid 
        id = args.id
        if(id <= 0 or id > len(data)):
            print("id is not valid")
        else:
            index = id - 1
        # case : remove item from middle or remove at the beginning 
            if(id != len(data)):
                data.pop(index)
                i = index 
                while i < len(data):
                    data[i]["id"] = i + 1
                    i += 1
            else: # removal at the end 
                data.pop()
            with open('data.json','w') as outfile:
                json.dump(data,outfile)
    #print(args)


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
        with open(fn, 'w') as outfile:
            json.dump([],outfile)
        file = open(fn)
        data = json.load(file)
        return data


"""
data structure 
{
"id"
"date"
"description"
"amount"
}
"""
