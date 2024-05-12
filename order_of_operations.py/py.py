import random


def perform_operations(starting_number, operations):

    operations_list = [
        lambda x: x / 2,
        lambda x: x * 3.5,
        lambda x: x + 2.55,
        lambda x: x - 2.55,
        lambda x: x * 2, 
        lambda x: x / 3.5
    ]
    
    while operations > 0:
        operation = random.choice(operations_list)
        starting_number = operation(starting_number) 
        operations -= 1

    return starting_number





starting_number = 1
operations = 60



ops = 100000000
arr = []
pointer = 0 
while pointer < ops:
    pointer +=1
    arr.append(perform_operations(starting_number, operations))

def Average(lst):
    return sum(lst) / len(lst)
print("results")
print(Average(arr))
