def print_depth(data, level = 1):
    if(data == None or isinstance(data, dict) == False):
        return
    for key in data:
        print("{} {}".format(key, level))
        print_depth(data[key], level + 1)
