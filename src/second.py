import models
from models.person import Person

def print_depth(data, level = 1):
    if(data == None or not (isinstance(data, dict) or isinstance(data, Person))):
        return
    
    if(isinstance(data, Person)):
        print("first_name {}".format(level))
        print("last_name {}".format(level))
        print("father {}".format(level))
        print_depth(data.father, level + 1)
    
    if(isinstance(data, dict)):
        for key in data:
            print("{} {}".format(key, level))
            print_depth(data[key], level + 1)