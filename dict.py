customers ={
    "name": "xyz",
    "age" : 45,
    "city" : "New york"
}
print(customers)
print(customers["name"])
print(customers.get("age"))
print(customers.get("state","Rajasthan"))
customers["state"]="England"
print(customers)

phone = input("Enter your phone number: ")
map1={
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
}
str=""
for item in phone:
    if item in map1:
        str+=map1[item]+' '

print(str)

