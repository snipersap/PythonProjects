## Dictionary in Python - an unordered collection of key-value pairs enclosed in {}
#Dictionary is mutable

dictionary_fruit = {"Mango":50, "apple":40, "guava":23, "peach":19}     #def
print("type(dictionary_fruit):",type(dictionary_fruit))                 #type
print("dictionary_fruit.keys():",dictionary_fruit.keys())               #extract keys
print("dictionary_fruit.values():",dictionary_fruit.values())           #extract values
print("dictionary_fruit.items():",dictionary_fruit.items())             #extract items

#Update elements
dictionary_fruit["Strawberry"]=30                                       #add a key pair
print("dictionary_fruit.items:",dictionary_fruit.items())
dictionary_fruit["Mango"] = 44                                          #update key-value
print("dictionary_fruit.items():",dictionary_fruit.items())

#Update dictionaries
shopping_dict = {"mango":10, "apple":20}
vegetables = {"beans":30, "chilli":50}
biscuit = {"biscotti":2, "kekse":5}
print("shopping list before:",(shopping_dict.items()))
shopping_dict.update(vegetables)                                        #update one dictionary with another
print("shopping list after:",shopping_dict.items())
print("added biscuits, result:", shopping_dict.update(biscuit),", list now:", shopping_dict.items())   #list updated before printing
print("popped mango:", shopping_dict.pop("mango"), ", list now:", shopping_dict.items())               #pop an element


##Set in Python >>
#A unique, unordered and unindexed collection of elements enclosed in {}
sample_set = {1, "Name", "age", 23, "place", "France", "pin", 23}
print("sample_set stores unique values only, each run displayes in different order:",sample_set)

#set operations
print("add element 46 to set, result:",sample_set.add(46), ", set now:", sample_set)        
print("update element with 'Updated', result:",sample_set.update(['Updated']),", set now:",sample_set)
print("update element with U,p,d,a,t,e,d, result:",sample_set.update("Updated"),", set now:",sample_set)
print("update multiple elements, result:",sample_set.update([11,22,33]),"set now:",sample_set)
print("remove place from sample_set, result:",sample_set.remove("place"),"set now:",sample_set)

#union and intersection
set_1 = {1,2,3,4,5,6}
set_2 = {2,3,4,6,7,8}
print("set_1.union(set_2):",set_1.union(set_2),"set_1:",set_1)  #union prints elements of both set_1 and set_2
print("set_1.intersection(set_2):",set_1.intersection(set_2),"set_2:",set_2)   #intersection prints common elements of set_1 and set_2





