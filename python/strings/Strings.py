# String length
x="Hello World"
print(len(x))

#Check String

description = "Iam a python Developer"
if "python" in description:
    print("python is present in description")

#
companyName = "Microsoft solutions"
if "Microsoft" in companyName:
    print("microsoft present in company name")

#
foodOrder = "Family pack biryani"
if "biryani" in foodOrder:
    print("Biryani is present in food order")

# Slicing
programmingLanguage = "Python"
print(programmingLanguage[0:3])

framework = "Django"
print(framework[1:4])

# Upper case
collageName = "Vaageswari"
print(collageName.upper())

#Lower case
lecturerName = "ABHINAY"
print(lecturerName.lower())

#Remove Whitespace

discription = "  offer letter  "       #using strip() method
print(discription.strip())

#Replace String
ticketBooking = "Bhahubali 2 The Conclution"
print(ticketBooking.replace("Bhahubali", "RRR"))

#Split String
bookSlot = "Booking ,Slot ,For ,Driving ,License"
print(bookSlot.split(","))

distance = "Hyderabad to , jangapally 150 kms"
print(distance.split(","))

