# Enter age of a person and check LIC eligibility as per following criteria , age is (18-45)
age=int(input("Enter an age:"))
if age >= 18:
    if age<= 45:
        print("you are eligible for LIC")
    else:
         print("you are not eligible")
else:
     print("you are not eligible for LIC")


