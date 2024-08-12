# გამოიტანეთ რიცხვები 0-დან 20-ის ჩათვლით 
for i in range(21):
    print(i)


# 3)მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტეთ შემოტანილი რიცხვი ლუწია თუ არა თუ ლუწია დაუპრინტეთ "Number is even" 
num1 = int(input("Input a number, and we'll inform you whether it's even or odd:"))

if num1 % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd") 

# 4) დაპრინტეთ 20-მდე ლუწი რიცხვები
for i in range(11):
    print(i * 2)

# 5)50-იდან 100-ის ჩათვლით არსებული ყველა რიცხვი დააჯამეთ for ციკლის გამოყენებით. ეს ჯამი უნდა შეინახოს ცვლადში, ამიტომ ციკლის გარეთ შექმენით sum ცვლადი (sum-ჯამი)
total_sum = 0

for i in range(50, 101):
    total_sum = total_sum + i

print("The sum of numbers from 50 to 100 is:", total_sum)


# 6)დაწერეთ ალგორითმი რომელიც ბეჭდავს 5-ის ჯერად რიცხვებს (რიცხვები რომლებიც იყოფა 5-ზე) 1-დან 50-ის ჩათვლით
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# 7)მომხმარებელს input-ის გამოყენებით შემოატანინეთ ორი რიცხვი. შემდეგ შეამოწმეთ რომელია უდიდესი და გამოიყენეთ for ციკლი: უმცირესიდან უდიდესამდე დაპრინტეთ ყველა რიცხვი
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    min_num = num2
    max_num = num1
else:
    min_num = num1
    max_num = num2

for i in range(min_num, max_num + 1):
    print(i)

# 8) გადაიმეორეთ განვლილი მასალა და გააკეთეთ მაგალითები
result_addition = 5 + 3
result_subtraction = 10 - 7
result_multiplication = 4 * 6
result_division = 10 / 2
result_modulo = 10 % 3

# 9)დაწერეთ ალგორითმი, რომელიც დაბეჭდავს 5-იდან ათის ჩათვლით რიცხვების ნამრავლს for loop-ის გამოყენებით.
result = 1
for i in range(5, 11):
    result = result * i
print("Final Result:", result)

# 10)BOSS: For loop დახმარებით ეცადეთ, რომ სიტყვა დაპრინტოთ საპირისპირო მიმართულებით (შეიძლება არ გამოგივიდეთ მაგრამ სცადეთ)
word = "GOA is the best"
reversed_word = ""
for i in range(len(word)): #(ჩემით არ გამიკეთებია გუგლში მოვიძიე და იმის დამიხედვით გავაკეთე.)
    reversed_word = word[i] + reversed_word
print("Final Result:", reversed_word)