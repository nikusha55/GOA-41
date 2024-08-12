def inte_gerebi():
        number_list = [12,  34, 56, 89]
        for i in number_list:
               return i
        sum(number_list)
print(inte_gerebi())


#task 12
def vowel_count(string):
    vowels = "aeiou"
    vowel_len = 0

    for i in string:
        if i in vowels:
            vowel_len += 1

    return vowel_len

print(vowel_count("Hello everyone"))

#task 13
def double_number(integer):
     numbers = []
     for i in integer:
          numbers.append(i ** 2)
     return numbers

print(double_number([10, 34, 90]))

#task 14
def reverce_string(string):
     return string[:: -1]

print(reverce_string("good_boy"))

#task 15
def check(number):
     if number % 2 == 0:
          return True
     elif number % 2 != 0:
          return False

print(check(22))


#task 16





#task 17
def integer(number):
     return min(number)

print(integer([20, 56, 67, 89]))

#task 18
import math

def gcd(int1, int2):
     return math.gcd(int1, int2)


print(gcd(12, 56))


#task 19
def string(uppercase):
     text = "hello my best friend"
     uppercase = text.upper()
     return uppercase

print(string("hello my best friend"))



#task 20
def average_arithmetic(num1, num2, num3, num4):
     return num1 + num2 + num3 + num4 // 4

print(average_arithmetic(12, 3, 45))