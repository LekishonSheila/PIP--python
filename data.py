
def sum(*nums):
       sum=0
       for num in nums:
        answer+=nums
        return(answer)
#    A function named concatenate_kwargs that takes any number
#  of string arguments in keyword arguments  format
#  and concatenates them into a single string #    
def concatenate_strings(*args):
    result = " "
    for arg in args:
        result += arg
    return result

def hello(name):
    print(f"Hello {name}")

def welcome(student,school):
    print(f"welcome to {school},{student}")