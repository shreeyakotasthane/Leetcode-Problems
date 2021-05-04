from itertools import groupby

s = input("Enter string")

for i,j in groupby(s):
    print(i, end="")
    print(len(list(j)),end="")

