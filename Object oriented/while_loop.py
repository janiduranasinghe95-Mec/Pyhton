count = 1

while count <= 5:
    print(count)
    count += 1

count = 40

while count >= 20:
    if count % 2 == 1:
        print(count)
    count -= 1

password = int(input("Enter password : "))
corr_pass = 1234
while password != corr_pass:
    print("password is incorrect")
    password = int(input("Enter password : "))

print("correct")

