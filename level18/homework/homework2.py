start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

numbers1 = []

for i in range(start, end):
       numbers1.append(i)

print(numbers1)


print(max(numbers1))
print(min(numbers1))
print(sum(numbers1))