def print_two(*args):
    arg1, arg2 = args
    print(f"Arg 1: {arg1}, Arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"Arg1: {arg1}, Arg2: {arg2}")

def print_one(arg1):
    print(f"Arg1: {arg1}")

print_two("Chase","Dalton")
print_two_again("X","Y")
print_one("LMAO")