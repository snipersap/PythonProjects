#Different loops in Python

#While loop in Python >>
#simple while loop, where does the while loop end
counter = 1
while counter <= 10:
    print("Print 1:",counter)
    counter += 1

    print("Print 2:",counter)   #part of while loop because of same indent

        #print("Print 3:",counter)   #syntax error:unexpected indentation


print("Print 4:",counter)   #outside while loop because of different indent

#print table of 2 with while loop
table_counter = 0
table_for = 2

while table_counter < 11:
    if table_counter == 0:
        print("Table of the number 2:")
    print(table_for," * ", table_counter, " = ", table_for*table_counter)
    table_counter += 1

#table with list and while
table_count = 0
table_for = 2
table_list = [0,2,4,6,8,10,12,14,16,18,20]
print("The list we have:", table_list)
print("Table for the number:", table_for)
while table_count < len(table_list):
    print(table_for," * ", table_count, " = ", table_list[table_count])
    table_count += 1


#For loops in Python
#For val in sequence
#   Body of For

#For with list
list_li = [1,2,4,"here", "i", "am"]
print("For with List:")
for list_item in list_li:
    print(list_item)

#Nested for loop with list
List_nest_1 = [1,2,3]
List_nest_2 = [4,5,6]
print("Nested for loop with list")
for list_item_1 in List_nest_1:
    for list_item_2 in List_nest_2:
        print("Parent list item:", list_item_1,"Child list item:",list_item_2)
