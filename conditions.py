#if-elif-else
big = 30
medium = 20
small = 10


#if conditions
if big > small:
    print(big, " is bigger than small.")
if small < big:
    print(small, " is smaller than big.")

#if-else
if big < small:
    print(big, " is less than small.")
else:
    print(small, " is less than big.")

#if-elif-else
if small > medium:
    print(small, " is greater than ", medium, ".")
elif medium > big:
    print(medium, " is greater than ", big,".")
else:
    print(big," is the greatest.")

#and and or conditions with if
if big > medium and medium > small:
    print(big,"is the biggest.")

if big > medium or big > small:
    print(big,"is greater than medium or small")

#conditions in tuple
tuple_1 = (1,2,3,4,5,6)
if 2 in tuple_1:
    print(2, "exists in", tuple_1)
if 7 in tuple_1:
    print(7, "exists in ", tuple_1)
else:
    print(7, "does not exist in ", tuple_1)

#conditions in list
list_1 = [1,2,3,4,5,6,7]
if list_1[1] == 2:
    list_1[1+1] = list_1[1+1]+100
    print("2 exists in ", list_1)
else:
    list_1[4] = list_1[1]+100
    print("Else condition calc:", list_1)

#conditions in dictionary
sample_dict = {"d1":1, "d2":2, "d3":3}
if sample_dict["d1"] == 2:
    print(sample_dict.values() ,"contains 2.")
elif 3 in sample_dict.values():
    print("3 exists in ", sample_dict)
else:
    print(sample_dict.items(), "does not contain 2.")

#conditions in set
num = 3
num_next = 6
set_sample = {1,2,4,5,6,"Hello"}
if num in set_sample:
    print(num, " exists in ", set_sample)
elif num_next in set_sample:
    print(num_next, "exists in ", set_sample)
