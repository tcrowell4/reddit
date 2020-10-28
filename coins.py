# Test Github change
# github change # 2
# github change # 3
# git
# github change # 4

"""
Store your bill values in a dictionary and increment the number needed as you are processing what you needed
Afterwards process the dict in reverse order to get out the values

Initial values for the dict
>>> bills = {50:0, 10:0, 5:0, 2:0, 1:0}

Increment
>>> bills[50] +=1
>>> bills[5] +=1

remember that you must sort the dict because they are not guaranteed to be in order

Examples of how to process the dict
>>> for bill in sorted(bills.keys()): print(bill, bills[bill])
...
1 0
2 0
5 1
10 0
50 1

Then determine how many bills for each bill value (key) in reverse order

>>> for bill in sorted(bills.keys(),reverse=True): print(bill, bills[bill])
...
50 1
10 0
5 1
2 0
1 0

Put it together
To get to your final format compile your final line in a list
>>> final= []
>>> for bill in sorted(bills.keys(),reverse=True): final.append(str(bills[bill]))
...
The resulting list
>>> final
['1', '0', '1', '0', '0']

>>> print(", ".join(final))
1, 0, 1, 0, 0
>>>

"""
