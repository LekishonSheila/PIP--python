# Reverse the list below
# list1=[100,200,300,400,500]
list1 = [100,200,300,400,500]
list1.reverse()
print(list1)

# How to concatenate two lists index-wise

# Write a program to add two lists index-wise. Create a new list 
# that contains the 0th index item from both the list, then the 1st index
# item, and so on till the last element.
# any leftover items will get added at the end of the new list.
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

# Given a list of numbers. write a program to turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
res = []
for i in numbers:
    res.append(i * i)
print(res)




