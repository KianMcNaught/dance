#KianMcNaught
#19/08/20
#Dance Program



GroupName = input ("What is the name of the group?")
NumberOfPupils = int(input("How many people are in the group?"))
while NumberOfPupils <2 or NumberOfPupils >10:
  print("Please enter an amount from 4 to 10")
  NumberOfPupils = int(input("How many people are in the group?"))

TotalPrices = []
PupilNames = []


for loop in range(NumberOfPupils):
  PupilName = input("Please enter the names of the people in the group")

  Photo = input("Would you like a photo?")
  while Photo != "Yes" and Photo != "No":
   print ("Please enter Yes or No")
   Photo = input("Would you like a photo?")

  if Photo == "Yes":
    TotalPrice = 4.99
  elif Photo == "No":
    TotalPrice = 3

  PupilNames.append(PupilName)
  TotalPrices.append(TotalPrice)



print ("Group Name:     " + GroupName)
print ("Number in group:    " , NumberOfPupils)
for loop in range(NumberOfPupils):
  print (PupilNames[loop] , TotalPrices[loop])