for i in range(0, 21):
     print(i)



for i in range(1, 11):
     print(i)


for i in range(1, 101):
    if i % 2 == 0:
         print(i)


num1 = int(input("Enter a random number:"))
if num1 < 0:
     print("Your number is not greater than 0")
if num1 == 0:
    print("Your number is equal to 0")
if num1 > 0:
     print("Your number is greater than 0")



age = int(input("Enter your age:"))
if age >= 18:
     if age < 18:print("You've never experienced the intimacy of love")


day_number = int(input("Enter a number (1-7) to get the day of the week: "))
if day_number == 1:
  print("Monday")
elif day_number == 2:
 print("Tuesday")
elif day_number == 3:
 print("Wednesday")
elif day_number == 4:
 print("Thursday")
elif day_number == 5:
 print("Friday")
elif day_number == 6:
 print("Saturday")
elif day_number == 7:
 print("Sunday")
else:print("Invalid number! Please enter a number between 1 and 7.")