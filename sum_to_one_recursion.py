# Define sum_to_one() below...
def sum_to_one(n):
    if n == 1:
        return n
        print("A base case reached")
    else:
        return n + sum_to_one(n - 1)
        print("Recursing with input: {}".format(n))


# uncomment when you're ready to test
print(sum_to_one(7))