def __print_depth_recursively(data, level = 1):
    if(data == None or isinstance(data, dict) == False):
        return
    for key in data:
        print("{} {}".format(key, level))
        __print_depth_recursively(data[key], level + 1)

def print_depth(data):
    __print_depth_recursively(data)
