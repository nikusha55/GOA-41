um = 5

# print(True and True) # True
# print(True and False) # False
# print(False and True) # False
# print(False and False) # False 

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

print("----------- AND -----------")

#ეს ხაზი იმიტომაა true რადგან ორივე შედარების ოპერატორი სწორედ წერია
print(num >= 1 and num <= 10) # True
#ეს ხაზი იმიტომაა false რადგან ერთი  შედარების ოპერატორი არასწორედ წერია
print(num >= 1 and num <= 4) # False
#ეს ხაზი იმიტომაა false რადგან ერთი შედარების ოპერატორი არასწორედ წერია
print(num > 5 and num <= 10) # False
#ეს ხაზი იმიტომაა false რადგან ორივე შედარების ოპერატორი არასწორედ წერია
print(num > 5 and num > 10) # False

print("----------- OR -----------")

#ეს ხაზი იმიტომაა true რადგან ორივე შედარების ოპერატორი სწორედ წერია
print(num >= 1 or num <= 10) # True
#ეს ხაზი იმიტომაა true რადგან ორივე შედარების ოპერატორი სწორედ წერია
print(num >= 1 or num <= 4) # True
#ეს ხაზი იმიტომაა true რადგან ერთი  შედარების ოპერატორი სწორედ წერია
print(num > 5 or num <= 10) # True
#ეს ხაზი იმიტომაა false რადგან ორივე შედარების ოპერატორი არასწორედ წერია
print(num > 5 or num > 10) # False


#and ეს ქართულად გადაითარგმნება როგორც და. ands როდესაც ვიყენებთ ორივე შედარების ოპერატორი სწორი უნდა იყოს თორემ შეცდომას დავუშვებთ და ტერმინალში გამოიტანს false
#or ქართულად გადაითარგმნება ან. ors როდესაც ვიყენებთ ერთერთი შედარების ოპერატორი სწორი უნდა იყოს რომ ტერმინალში true მივიღოთ თუ ორივე შედარების ოპერატორი არასწორე იქნება false გამოიტანს ტერმინალში 

num=10
print(num >= 5 and num < 20 )
print(num = 10 and num > 9)
print(num <= 30 and num < 25)
print(num > 2 and num >= 4)
print(num < 13 and num >= 10)

print(num <= 5 or num <= 10 )
print(num = 10 or num >= 30)
print(num <= 5 or num> 3)
print(num > 6 or num < 23)
print(num <= 1 or num <= 13)


print(1 < 3)
print(10 > 6 )
print(15 >= 15)
print(28 <= 35)
print(69 == 69)