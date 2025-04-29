<<<<<<< HEAD
# Write a program to fill in letter template given below with name and date

name = "Akash"
date = "29-04-2025"
letter = f'''Dear {name}, \n You are selected! \n {date}'''
print(letter)

let = '''Dear <|Name|> 
        You are selected! 
            <|Date|>'''

print(let.replace("<|Name|>","Akash").replace("<|Date|>", "29-04-2025"))
=======
# Write a program to find remainder when a number is divided by z

a = 4
b = 2
c = a%b
print(c)
>>>>>>> origin/master
