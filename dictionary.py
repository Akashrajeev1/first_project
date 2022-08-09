# dict={1:"me",2:"you",3:"he"}
# print(dict[1])
# print(dict[2])
# print(dict[3])
# #print(dict[4])
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get(1))
# print(dict.get(2))

# dict = {1: "me", 2: "you", 3: "he"}
# dict.update({4:"she"})#giving new keys in dict
# print(dict)
# dict["5"]="I"     #giving value I to the key 5
# print(dict)
# dict.pop(1)
# print(dict)
# dict.popitem()#pop last item in dict
# print(dict)
# del dict[2]
# print(dict)
# dict.clear()
# print(dict)

# dict={1:"he",2:"she",3:"I"}
# for i in dict:               #i only return key not values
#     print(i)

dict = {1: "he", 2: "she", 3: "I"}
for i in dict.items():          #dict.items returns keys and values
    print(i)
for i in dict.keys():
    print(i)
for i in dict.values():
    print(i)