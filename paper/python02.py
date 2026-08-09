Stu_name = input("Enter student name: ")
Maths = int(input("Enter your Mathematics marks: "))

if Maths < 0 or Maths > 100:
    print("Invalid Mathematics marks")
else:
    Sci = int(input("Enter Science marks: "))

    if Sci < 0 or Sci > 100:
        print("Invalid Science marks")
    else:
        Ict = int(input("Enter ICT marks: "))

        if Ict < 0 or Ict > 100:
            print("Invalid ICT marks")
        else:
            Total = Maths + Sci + Ict
            Average = Total / 3

            if Average >= 90:
                Grade = "Distinction"
            elif Average >= 85:
                Grade = "Distinction"
            elif Average >= 75:
                Grade = "Merit"
            elif Average >= 65:
                Grade = "Credit"
            elif Average >= 55:
                Grade = "Pass"
            else:
                Grade = "Fail"

            Excellent = "Yes" if Average >= 90 else "No"
            Best_all_rounder = "Yes" if Average > 80 else "No"
            Improvement_notice = "Yes" if Average < 35 else "No"

            print("Student Name :", Stu_name)
            print("Entered Mathematics marks :", Maths)
            print("Entered Science marks :", Sci)
            print("Entered IT marks :", Ict)

            print("----------Student Performance Report----------")

            print("Student Name :", Stu_name)
            print("Total Marks :", Total)
            print("Average Marks :", Average)
            print("Grade :", Grade)
            print()
            print("Academic Excellent :", Excellent)
            print("Best All Rounder :", Best_all_rounder)
            print("Improvement Notice :", Improvement_notice)