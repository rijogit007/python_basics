# fruits=['apple','banana','cherry','date','elderberry']

# fruits[1]='strawberry'
# print(fruits[1])


# slicing



fruits=['apple','banana','cherry','date','elderberry']

# print(fruits[1:4])


a=[1,2,3,4,5]
print(len(a))

while True:
    add=(input("enter a number "))

    if add=="stop":
        print("stopped")
        break
    a.append(add)

    print(a)

a.append(58)
print(a)

a.insert(2,100)
print(a)

a.remove(1)
print(a)

a.clear()
print(a)

a.pop(2)
print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)