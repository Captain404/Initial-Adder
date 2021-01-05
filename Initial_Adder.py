import sys

file = 'lastnames.txt'
Initials = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

with open(file) as f:
    name_list = f.read().splitlines()

for letter in Initials:
    for name in name_list:
        prepended_names = letter + name
        print(prepended_names)
