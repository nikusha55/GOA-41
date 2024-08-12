num1 = int(input("Pleace Enter Quantity Numbers Of How Many You Want To Enter: "))

numbers = []

for i in range(num1):
    num = int(input("Pleace Enter Number: " + str(i+1) +": "))

numbers.append(num)
print(numbers)

print(len(numbers))