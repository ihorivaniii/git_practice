def power_set(my_list):
    # function return all possibility of combinations components of list
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    # return combination of the two
    return with_first + power_set_without_first


universities = ['MIT', 'UCLA', 'Stanford']
power_set_of_universities = power_set(universities)
print(power_set([1, 2, 3]))
for i in power_set_of_universities:
    print(i)


my_list = [1, 2, 3]
power_set = power_set(my_list[1:])
with_first = [[my_list[0]] + i for i in power_set]
print(with_first)
print("\n")
print(power_set)
