class multipleFunction():
    
    # Create a function, and list out the items in the list
    def Subfields(myList):
        print("Sub-fields in AI are:")
        for item in myList:
            print(item) 
            
    # Create a function that checks whether the given number is Odd or Even            
    def OddEven():
        num1 = int(input("Enter a number:"))
        if(num1%2 == 1):
            print(num1,"is Odd number")
            OddEven = num1,"is Odd number"
        else:
            print(num1,"is Even number")
            OddEven = num1,"is Even number"
        return OddEven 
    
    # Create a function that checks whether the given number is Odd or Even
    def OddEven():
        num1 = int(input("Enter a number:"))
        if(num1%2 == 1):
            print(num1,"is Odd number")
            OddEven = num1,"is Odd number"
        else:
            print(num1,"is Even number")
            OddEven = num1,"is Even number"
        return OddEven 
    
    # Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def Elegible():
        gender = input("Your Gender:")
        age = int(input("Your Age:"))
        print("Your Gender:",gender)
        print("Your Age:",age)
        if (gender == "Male" and age >=21): 
            print("Eligible")
            ElegiblityForMarriage = "Eligible"
        elif (gender == "Female" and age >=18):
            print("Eligible")
            ElegiblityForMarriage = "Eligible"
        else: 
            print("Not Eligible")
            ElegiblityForMarriage = "Not Eligible"
        return ElegiblityForMarriage
    
    # calculate the percentage of your 10th mark
    def percentage(Subject1,Subject2,Subject3,Subject4,Subject5):
        print("Subject1=", Subject1)
        print("Subject2=", Subject2)
        print("Subject3=", Subject3)
        print("Subject4=", Subject4)
        print("Subject5=", Subject5)
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        Percent = float(Total/5)
        print("Total:",Total)
        print("Percentage:",f"{Percent:.15f}")
        return Total,Percent

    #print area and perimeter of triangle using functions
    def triangle():
        height = int(input("Height:"))
        print("Height:",height)
        breadth = int(input("Breadth:"))
        print("Breadth:",breadth)
        print("Area formula: (Height*Breadth)/2")
        Areaoftriangle = (height*breadth)/2
        print("Area of Traingle:", Areaoftriangle)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth1 = int(input("Breadth:"))
        print("Height1:",height1)
        print("Height2:",height2)
        print("Breadth",breadth1)
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeteroftriangle = height1+height2+breadth1
        print("Perimeter of Traingle:", Perimeteroftriangle)
        return Areaoftriangle,Perimeteroftriangle   