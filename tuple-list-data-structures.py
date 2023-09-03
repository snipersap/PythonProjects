#Different data structures in Python

##Tuple in Python >>
my_tuple = (1,2,True,5,False,7,"Sample",'b',9)
print("type(my_tuple):",type(my_tuple))

#tuples are immutable
#my_tuple[1] = "hello world"  #TypeError: 'tuple' object does not support item assignment

#tuple element extraction
print("extract elements:", my_tuple[1], my_tuple[3], my_tuple[-1], my_tuple[1:4])

print("len(my_tuple):",len(my_tuple)) #tuple length
print("concat tuples:", my_tuple+my_tuple) #concat tuples
print("repeat tuple: my_tuple*3:", my_tuple*3) 
print("repeat and concat tuples:", my_tuple*2+my_tuple)

#Create tuple only with numbers
my_numbered_tuple = (200,33,56,23,87,290) #Heterogeneous or complex tuples are not supported by min and max
print("minimum in tuple:", min(my_numbered_tuple))
print("maximum in tuple:", max(my_numbered_tuple))

my_string_tuple = ("First", "Third", "Second")          #min and max support strings
print("minimum in string tuple:", min(my_string_tuple))
print("maximum in string tuple:", max(my_string_tuple))

##List in Python >>
my_list = [200, 345, 872, False, 34, True, "You are great", "Du schaffst das", 10+1j]
print("type(my_list)", type(my_list))

#Extract elements
print("extract elements from my_list:", my_list[1], my_list[-1], my_list[2:6], my_list[4:len(my_list)])

#Modify elements
my_list[2] = 777                                #single element modification
print("my_list[2]:", my_list[2])

print("my_list[2:4] before:", my_list[2:4])
my_list[2:4] = [23,24]                          #multi element modification
print("my_list[2:4] after:", my_list[2:4])

#append
print("my_list:", my_list)
my_list.append("Appended")                      #single append
print("after append element, my_list:",my_list)
my_list.append(["First", 2, "Third"])                   #secondary list append
print("after secondary list append, my_list:", my_list)

#pop
popped = my_list.pop()                                  #pop last element
print("popped last element:",popped,"my_list:",my_list)
popped = None
print(popped)
popped = my_list.pop(3)                                  #pop specific index
print("popped index 3:", popped,"my_list:", my_list)

#reverse list
my_list.reverse()
print("reversed list", my_list)

#insert at specific index
my_list.insert(4,"Inserted")
my_list.insert(6,[1,2,3])
print("inserted 2 elements, my_list:",my_list)

#sort the list
my_numbered_list = [2,6,7,2,6,8,99,23,54]                       #sort does not support heterogeneous lists
my_numbered_list.sort()                                         #sort list ascending
print("sorted ascending (default), my_list:",my_numbered_list)
my_numbered_list.sort(reverse=True)                             #sort list descending
print("sort descending, my_list:",my_numbered_list)

#concatenate lists
my_first_list = [1,2,3]
my_second_list = [4,5,6]
print("concatenated lists = ", my_first_list+my_second_list)

#repeated lists
my_repeat_list = [11,22,33]
print("my_repeat_list*2:", my_repeat_list*2)




