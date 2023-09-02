my_String = "My name is Drishna."
my_Single_Quote_String = 'my Home is in india.'
my_Multiline_String = """
I love travelling.
"""
print("myString[0]:", my_String[0])
print("myString[1]:", my_String[1])
print("myString[-1]:", my_String[-1])
print("myString[4]:", my_String[4])
print("myString[-8:20]:", my_String[-8:20]) #get substring with hardcoded index
print("myString[-8:len(myString)]:", my_String[-8:len(my_String)]) #get substring

print("len(mySingleQuoteString):", len(my_Single_Quote_String)) #length of string
print("mySingleQuoteString:",my_Single_Quote_String)
print("mySingleQuoteString.capitalize():",my_Single_Quote_String.capitalize()) #Capitalize first letter of first word

print("mySingleQuoteString.upper():",my_Single_Quote_String.upper()) #convert to upper
print("mySingleQuoteString.lower():",my_Single_Quote_String.lower()) #convert to lower
print("mySingleQuoteString.replace('m','a'):",my_Single_Quote_String.replace("m","a")) #replace m with a in the string

print("mySingleQuoteString.count('in'):",my_Single_Quote_String.count("in")) #count the number of non-overlapping substrings 
print("mySingleQuoteString.find('Home'):",my_Single_Quote_String.find('Home')) #Substring exists
print("mySingleQuoteString.find('home'):",my_Single_Quote_String.find('home')) #Substring does not exist

print("myString.split(" ")", my_String.split(" ")) #split string with space as delimiter

