fruits=("apple","banana","cherry","guava","mango","pineapple")
a,b,*c=fruits
print(a)
print(b)
print(c)

ttuple=(1,2,3,4)
ttuple=list(ttuple)
ttuple.append(5)
ttuple=tuple(ttuple)
print(ttuple)