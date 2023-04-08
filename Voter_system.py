Gender = input("Enter voter's Gender: ")
DOB = input("Please enter your birth year: ")
dob = int(DOB)
if (Gender=="male" and dob <= 2002):
 print("You're a eligible male voter!")
elif(Gender=="female" and dob <=2004):
 print("You're a eligible female voter!")
else:
    print("You're not eligible to vote!")