import random
import threading
import time


def perform_operations(starting_number, operations):

    operations_list = [
        lambda x: x / 2,
        lambda x: x + 3.5,
        lambda x: x + 2.55,
        lambda x: x - 2.55,
        lambda x: x + 2, 
        lambda x: x / 3.5
    ]
    
    while operations > 0:
        operation = random.choice(operations_list)
        starting_number = operation(starting_number) 
        operations -= 1

    return starting_number





starting_number = 1
operations = 60



ops = 1000000
arr = []
pointer = 0 

lock = threading.Lock()
def loop_with_operations():
    global pointer
    global arr
    for _ in range(ops):
        lock.acquire()
        pointer += 1
        lock.release()
        arr.append(perform_operations(starting_number, operations)) 


def Average(lst):
    return sum(lst) / len(lst)
def run_results(arr):
    print("results")
    print(Average(arr))

'''
while pointer < ops:
    pointer +=1
    arr.append(perform_operations(starting_number, operations))
'''
def print_pointer():
    while True:
        lock.acquire()
        current_pointer = pointer
        lock.release()
        print(f"{current_pointer} / {ops}")
        if(current_pointer == ops):
            run_results(arr)
            quit()
        time.sleep(10)



loop_thread = threading.Thread(target=loop_with_operations)
loop_thread.start()

progress_thread = threading.Thread(target=print_pointer)
progress_thread.start()


loop_thread.join()
progress_thread.join()
