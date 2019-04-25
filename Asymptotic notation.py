from stack import Stack
from Queue import Queue
def count(N):
    count = 0
    while N > 1:
        N = N // 2
        count += 1
    return count


num_iterations_1 = count(1)  # REPLACE
print("The while loop performs {0} iterations when N is 1".format(num_iterations_1))

num_iterations_2 = count(2)  # REPLACE
print("\nThe while loop performs {0} iterations when N is 2".format(num_iterations_2))

num_iterations_4 = count(4)  # REPLACE
print("\nThe while loop performs {0} iterations when N is 4".format(num_iterations_4))

num_iterations_32 = count(32)  # REPLACE
print("\nThe while loop performs {0} iterations when N is 32".format(num_iterations_32))

num_iterations_64 = count(64)  # REPLACE
print("\nThe while loop performs {0} iterations when N is 64".format(num_iterations_64))

runtime = "log N"
print("\nThe runtime for this function is O({0})".format(runtime))

N = 6

my_stack = Stack(N)
my_stack.push("Australia")
my_stack.push("India")
my_stack.push("Costa Rica")
my_stack.push("Peru")
my_stack.push("Ghana")
my_stack.push("Indonesia")

my_queue = Queue(N)
my_queue.enqueue("Australia")
my_queue.enqueue("India")
my_queue.enqueue("Costa Rica")
my_queue.enqueue("Peru")
my_queue.enqueue("Ghana")
my_queue.enqueue("Indonesia")

# Print the first values in the stack and queue
print("The top value in my stack is: {0}".format(my_stack.peek()))
print("The front value of my queue is: {0}".format(my_queue.peek()))

# Get First Value added to Queue
first_value_added_to_queue = my_queue.dequeue() # Checkpoint 2
print("\nThe first value enqueued to the queue was {0}".format(first_value_added_to_queue))
queue_runtime = "1" # Checkpoint 3
print("The runtime of getting the front of the queue is O({0})".format(queue_runtime))

# Get First Value added to Stack
# Write Code Here for #Checkpoint 4


while not my_stack.is_empty():
    first_value_added_to_stack = my_stack.pop()



print("\nThe first value pushed onto the stack was {0}".format(first_value_added_to_stack))
stack_runtime = "REPLACE" # Checkpoint 5
print("The runtime of getting the bottom of the stack is O({0})".format(stack_runtime))