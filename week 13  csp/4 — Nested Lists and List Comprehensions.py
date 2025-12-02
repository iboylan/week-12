# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][2])    # 6

# # List comprehension
# first_col = [row[0] for row in matrix]
# print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.

alallaa = [
    [121321213,3243424,234243342234],
    [90654,5493,"m"],
    ["a","b","c"]
]

# Print the first list.

print(alallaa[0])

# Print the second item from the third list.

print(alallaa[2][1])

# Use a list comprehension to extract the last item from each sub-list.
y = -1
for x in alallaa:
    print(alallaa[y+1][2])
    y=y+1

# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.

