def leapYear(lyear):
    if(lyear%400 == 0 and lyear % 100 == 0):
        print(lyear," is a leap year")
    elif(lyear % 4 == 0 and lyear % 100 != 0):
        print(lyear," is a leap year")
    else:
        print(lyear ," is not a leap year")

lyear = int(input("Enter the year :"))
leapYear(lyear)