number = [10,20,30,20]
number.insert(1, 50)
print(number)

print(number.index(30))
print(number.count(20))
print(number.pop())
print(number.pop())
print(number)
number.remove(50)
print(number)

color = ['red', 'green', 'blue']
print(color)
del color
#print(color)


value = [10,20,30,40,"total",50];
value.reverse();
number.reverse();
print(value);
print(number);

number.sort();
print(number);

vehicle = ["bnw", "audi", "toyota", "honda"]
vehicle.sort(key=len);
print(vehicle);