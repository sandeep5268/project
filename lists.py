print()

fruits=["apple","banana","mango"]

print("The Initial items in fruits list:")

print(fruits)   #printing a given list of items

print()

for i in fruits: #printing items by using for loop
    print(i)

print()

if "apples" in fruits:  #checking an item is in list or not
    print("Yes it is in fruits")
else:
    print("No it is not in fruits")
    
    print()
    
fruits.append("lemon") #inserting item at last index
print(fruits)
    
print()

fruits.insert(0,"cherry") #inserting item at particular index
print(fruits)

print()

fruits.pop()  #removing lat item in list
print(fruits)

print()

fruits.remove("banana") #removing specific item in list
print(fruits)

print()

fruits.reverse()
print(fruits)

print()

fruits.sort()
print(fruits)

print()

fruits.clear()  #Removing all the items from the list making an empty
print(fruits)

print()

######################################################

numbers=[0]*3

numbers2=[2,4,3,6,5]

new = numbers + numbers2   #combining of two lists
print(new)

print()
#######################################################

number=[2,4,3,5,7,6,9,8]
print("The original list:",number)

a=number[3:7] #extracting list from original list
print(a)

print()

b=number[::2] #printing a list from the original list by taking skiping one number
print(b)

print()

c=number[::-1] #printing a reverse list from the original list
print(c)

print()

######################################################

list_org=["tomato","brinjal","carrot"]

list_cpy=list_org    #By this if we change list_cpy simultaneously list_org also changes both results same list
list_cpy.append("cauiliflower")

print(list_cpy)
print(list_org)

list_cpy=list_org[:2]  #We can do slicing the list_cpy changes according to slicing of list_org
print(list_cpy)

print()
######################################################

list=[2,3,4,5,7,9]
list2=[i*i for i in list] #with this we can square the value using loop
print(list)
print(list2)