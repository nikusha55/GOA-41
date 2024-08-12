#task 1
def number(num1,num2):
    number = num1 + num2
    number2 = num1 - num2
    number3 = num1 * num2
    return number,number2,number3
       
num1 = 5
num2 = 7
print(number(num1,num2))





#task 2
def number(num):
    return sum(num)
print(number([2,3,4,5,6,1]))




#task 3
def check(number):
     if number % 2 == 0:
          return True
     elif number % 2 != 0:
          return False

print(check(22))


#task 4
def  manual_integer(int1):
    return  max(int1)

print(manual_integer([12, 45, 89, 100]))

#task 5
def list_sum(int35):
    return sum(int35)

print(list_sum([100, 67 ,200]))


#task 6
def stringss_reverce(string):
    return string[::-1]

print(stringss_reverce("girls"))




##task 7
def guess(word):
    max_word = ""
    for i in word:
        if len(i) > len(max_word):
            max_word += i
    return max_word

print(guess(["car", "money", "animals"]))


#task 8
def check(string):
    word = ""
    for i in string:
        if i.islower():
            word += i.upper()
        elif i.isupper():
            word += i.lower()
    return word

print(check("cars"))


#task 9
def vowel_count(word):
    vowel = "abd"
    count = 0
    for i in word:
        if i in vowel:
            count += 1
    return count

print(vowel_count("honey"))




#task 10
def even_kent(count):
    if count % 2 == 0:
        return True
    else:
        return False

#task 11
def sum_even_index(nums):
    sum_even = 0
    for i in range(0, len(nums), 2): 
        sum_even += nums[i]
    return sum_even

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_index(nums)
print(result)  



#task 12
def even_or_kent(numbers):
    for i in numbers:
        if i % 2 == 0:
            print("even")
        else:
            print("kent")
    return numbers

print(even_or_kent([12, 78]))
        

#task 13
def num(numbers1):
    if numbers1 % 1 == 0 and numbers1 % numbers1  == 0:
        return "simple"
    else:
        return "dificult"


print(num(2))





#task 14
word = "erekle"
print(word.capitalize())





#task 15
def num1(numbers10):
    lists = []
    for i in numbers10:
        if i % 2 == 0:
            lists.append(i / 2)
        elif i % 2 != 0:
            lists.append(i * 2)
    return lists

print(num1([2,3,5,6,7]))






#task 16
def string(word):
    word = word.upper()
    word = word [::-1]
    return word
print(string("honey"))




#task 17 
def string1(word1):
    odd = []
    even = []
    for i in word1:
        if len(i) % 2 == 0:
            even.append(i.upper())
        elif len(i) % 2 != 0:
            odd.append(i.upper())
    return odd,even

print(string1(["nika", "qeti", "gio"]))







#task 18
def stringss(string, char):
    index = string.find(char)

    if index % 2 == 0:
        return string.upper()
    else:
        return string.capitalize()
    
print(stringss("Hello world", "w"))
