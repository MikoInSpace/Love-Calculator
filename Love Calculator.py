from random import randrange
import os

while True:

 name1 = input("Enter the first name: ")
 name2 = input("Enter the second name: ")
 os.system('cls' if os.name == 'nt' else 'clear')
 print("Is this correct?")
 print("First Name: ", name1)
 print("Second Name: ", name2)
 print("Y/N")
 yn = input("")
 if yn == "y":
  os.system('cls' if os.name == 'nt' else 'clear')
  print(randrange(100), "%")
 if yn == "n":
  break 
  