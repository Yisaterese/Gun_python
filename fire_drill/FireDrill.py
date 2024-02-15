

x = ("apple", "banana", "cherry")
y = list(x)
y[2] = "kiwi"
x = tuple(y)

print(x)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
thisset.add(x)

print(thisset)
print(""" 


""")
#workin with strings

name1 = 'abcd'
name2 =' bdce'
name3 = ('ABC'
         '')
a = name1 == name2
#print(ord(a))
print(name1 < name2)
print("d" in name1)
#7 spaces at the rigth
print(f'[{name1:7}]')
#7 spsces to left
print(f'[{name1:>7}]')
# 7 spaces to ritght
print(f'[{name1:<7}]')
#midlle
print(f'[{name1:^7}]')

print(name1 + name2)
print(f'{name1} {name2}')
print(name1 * 4,end="")
name3 =  "   muhamed  "

sentence = 'you are a boy'
print(len(name3.strip()))
print(name3)
print(len(name3))
print(name3.lower())
print(name1.upper())
print(name2.capitalize())
print(name3.casefold())
print(sentence.title())
print(sentence.count("e"))
print(sentence.rindex('e'))
print(sentence.index('e'))
'''name1 = input("Enter name: ").strip()
#it takes only strings but without spaces
if name1.isalpha():
    print("valid")
else:
    print("invalid")'''
# contains characters and numbers only
if name1.isalnum():
    print("valid")
else:
    print("invalid")


for char in name2:
    pass
else:
    print(char)

#collects digits only
if name1.isdigit():
    print("valid")
else:
    print("invalid")

#if you want to know what a method does
#print(help(name3.isprintable()))
#replace

print(help(sentence.replace("x","y")))
#python join method
names = ["olamide","aramide","ayomide","dayomide"]
print("-".join(names))