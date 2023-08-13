my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
# Browse all numbers from the source list.
for i in range(len(my_list)):
    if my_list[i] not in new_list:
    # If the number doesn't appear within the new list...
        new_list.append(my_list[i])
        # ...append it here.
# Make a copy of new_list.
my_list = new_list[:]
print("The list with unique elements only:")
print(my_list)
