number = {5,8,10,8,5}
print(type(number))
print(number)

print(len(number))
for x in number:
    print(x)

print(20 in number)

number.add(20)
print(number)

number.update([40,60])
print(number)

number.remove(5)
print(number)

number.discard(8)
print(number)   

x = number.pop()
print(x)

#number.clear()
print(number)

#del number

number2 = number.copy()
print(number2)