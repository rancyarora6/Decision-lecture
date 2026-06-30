# Taking age inputs from the user 
age_Ram = int(input("Enter the age of Ram:"))
age_Shyam = int(input("Enter the age of Shyam:"))
age_Mohan = int(input("Enter the age of Mohan:"))
# comparing the ages to find the eldest 
if age_Ram > age_Shyam and age_Ram > age_Mohan:
    print("Ram is the eldest.")
elif age_Shyam > age_Ram and age_Shyam > age_Mohan:
    print("Shyam is the eldest.")
elif age_Mohan > age_Ram and age_Mohan > age_Shyam:
    print("Mohan is the eldest.")
else:
    print("Two or more people share the maximum age.")

