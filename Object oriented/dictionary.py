student = {
    "name": "Nimal",
    "age": 20,
    "city": "Colombo"
}

print(student["name"])


student["grade"] = "A"
print(student)

student["age"] = 21
print(student)

student.pop("city")
print(student)

student.popitem()
print(student)

#student.clear()
print(student)

len(student)

type(student)

print(sorted(student))

min(student)

max(student)

nw_std =dict(student)

