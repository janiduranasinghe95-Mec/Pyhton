day = 2

match day:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case _:
        print("invalid day")



grade  = "A"

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("invalid grade")


fruit = "apple"

match fruit:
    case "apple"|"mango":
        print("sweet fruit")
    case "lemon":
        print("sour fruit")
    case _:
        print("unknown fruit")

age_1 = 20

match age_1:
    case x if x >= 18:
        print("adult")
    case _:
        print("minor")

