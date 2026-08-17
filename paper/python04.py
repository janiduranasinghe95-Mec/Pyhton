name = input("Enter customer name : ")
pre_meter = float(input("Enter previous electricity meter reading: "))
current_meeter = float(input("Enter current electricity meter reading: "))

if pre_meter < 0 or current_meeter < 0:
    print("-----------Elecrticity Bill-----------")
    print("Enter previous electricity meter reading:", pre_meter)
    print("Enter current electricity meter reading:", current_meeter)
    print()
    print("Entered reading is incorrect")

elif current_meeter < pre_meter:
    print("-----------Elecrticity Bill-----------")
    print("Enter previous electricity meter reading:", pre_meter)
    print("Enter current electricity meter reading:", current_meeter)
    print()
    print("Invalid entered: current reading must be greater than or equal to previous reading")
    
else:
    monthly_Srvice_charge = 500
    Unit_consumed = current_meeter - pre_meter

    if Unit_consumed <= 30:
        charge_per_unit = 25
        reward = "Energy Saver Reward"
        Envir_levy = 0

    elif Unit_consumed <= 60:
        charge_per_unit = 25
        Envir_levy = 0
        reward = "None"

    elif Unit_consumed <= 120:
        charge_per_unit = 35
        Envir_levy = 0
        reward = "None"

    elif Unit_consumed <= 150:
        charge_per_unit = 50
        Envir_levy = 0
        reward = "None"

    else:
        charge_per_unit = 50
        Envir_levy = 1000
        reward = "None"

    elec_charge = (Unit_consumed*charge_per_unit)
    Final_bill =  elec_charge + monthly_Srvice_charge + Envir_levy

    print("Enter customer name : ",name)
    print("My previous Reading : ",pre_meter)
    print("Enter Current Reading : ",current_meeter)
    print()

    print("-----------Elecrticity Bill-----------")
    print()

    print("Customer Name : ",name)
    print("Unit consumed : ",Unit_consumed)
    print("Electricity charge : Rs.",elec_charge)
    print("Service Charge : Rs.",monthly_Srvice_charge)
    print("Environmental Levy : Rs.",Envir_levy)
    print()

    print("Final bill : Rs.",Final_bill)
    print()

    print("Reward :",reward)

    