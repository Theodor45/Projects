# The usual way
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = []
for f in numbers:
    new_num = f + 1
    new_numbers.append(new_num)
print(new_numbers)
# 6 lines!!

# With list comperhension
numbers = [1, 2, 3, 4, 5, 6]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)
# 3 lines!!

# Using list comperhension with range()
range_list = [item*2 for item in range(1, 5)]

# Looping through a list of strings
names = ['Alex', 'Beth', 'Dave', 'Carolinnie', 'dave', 'freddie']
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names]