corr_pass = 1234

while True:
    password = int(input("Enter password : "))
    if corr_pass == password:
        print("correct")
        break
    else:
        print("incorrct password")