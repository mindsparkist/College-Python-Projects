# define a list of tuples
myList = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), ()]
# remove empty tuples bruteforce

# for i in range(len(myList)):
#     if len(myList[i]) == 0:
#         myList.remove(myList[i])


# remove empty tuples filter method

# myList = filter(lambda param: len(param) != 0, myList)

# # it returens a generator object so we need to convert it to a list
# print(list(myList))

# remove empty tuples using list comprehension

myList = [cleanList for cleanList in myList if cleanList != ()]
print(myList)
