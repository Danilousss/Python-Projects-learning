## ----- conditiona expression -> do this -> "x" if condition else do this -> "y" 

# rain = False
# print ("Raining") if rain else print("not raining")

## string methods 
# -> len = len(name) (length of the string)
# name.find(" ") <- (first caractere)
# name.rfind(" ") <- (last caractere)
# name.capitalize() <- upper the first letter
# name.upeer() <- Upper all the letters 
# name.lower() <- lower all the letters 
# name.isdigit <- returns "true if your string has only digitis"
# name.isalpha() <- returns "true if your string has only alphabetics"
# name.count(" ") <- returns a especific numbers o f how many letters or numbers are equal what is between ""
# name.replace("", "-") <- replace what is inside the 1fst "" for whats is in the 2cnd


# condition = False
# while condition == False:
#     name = input("What is your name?")
# 
#     if(len(name) > 12 ):
#         print ("Your name shoud be shorter than 12 carctares")
#     elif (name.find(" ") == 1):
#         print ("your name can't contain spaces")
#     elif not (name.isalpha()):
#         print("your name can only contain letters")
#     else:
#         print (f"Your name is: {name}")
#         condition = True
 
## ----- indexing -> acessing elements of a sequence using []
#                     [start : end : step]
 
# credit_card = "1234-5678-8999-3784"
# last = credit_card[::-1]        
# print(last)
 
## ----- while loop
 
# food = input("What food do you like (press q to exit)")
# 
# while not food == "q":
#     print(f"you like {food}")
#     food = input("What eslse?(press q to exit)")
# print("bye")
 
# num = int(input("Type a number "))
# 
# while not num < 0 and num > 10: 
#     print("your number shoud be between 0 and 10 ")
#     num = int(input("Type a number "))
# print(f"your number is {num}")
 
# time = 0
# interest_rate = 0
# amount = 0
### --> a way that make more sense to do the while 
# while True: 
#     amount = float(input("What is the amout? "))
#     if amount <= 0:
#         print("the amount can't be less  or equal to 0")
#     else:
#         break
# while True: 
#     interest_rate = float(input("What is the interest_rate? "))
#     if interest_rate <= 0:
#         print("the interest_rate can't be less  or equal to 0")
#     else:
#         break
# while True: 
#     time = float(input("What is the time? "))
#     if time <= 0:
#         print("the time can't be less  or equal to 0")
#     else:
#         break
# result = amount * pow((1 + interest_rate/100),time)
# print(f"Your result is {result}")

## ------ for loop 
# for i in range(0, 10):
#     if(i == 8):
#         continue
#     else:
#         print(i)
    
# for i in reversed(range(0, 10)):
#     print(i)
# print("Happy new year")
 
#  Time ----- 
 
#  import time
#   
#  time.sleep(2)
#  print("hey")
 
# my_time = int(input(f"Enter the time in seconds "))
# 
# for i in reversed(range(1, my_time + 1)):
#     time.sleep(1)
#     seconds = int(i % 60) 
#     minutes = int((i / 60) % 60)
#     hours = int(i / 3600)
# 
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")

# ----- nasted loop 
# rows = int(input("give the numbers of rows "))
# coluns = int(input("give the numbers of coluns "))
# simble = (input("give the simble "))
# 
# for i in range(rows):
#     for j in range(coluns):
#       print(simble, end="")
#     print()

# --------- collection = single "variable" used to store multiple values 
# list = [] ordered and changeable. Duplicates ok
# set = {} unordered and immutable, but add/remove ok, no duplicates 
# Tuple = () ordered and unchangeable. duplicates ok. faster

# fruits = ["apple", "banana", "lemon"]

# fruits.append("coconuts")
# fruits.remove("apple")
# fruits.insert(0,"strawberry")
# fruits.sort()
# fruits.reverse()

# print(fruits[0])

# foods = []
# prices = []
# total = 0
# 
# while True:
#     food = input("What food do you whant to bye? (Press q to quit) ")
#     if(food.lower() == "q"):
#         break
#     else:
#         foods.append(food)
#         price = float(input("What is the price of this food "))
#         prices.append(price)
#     for i in foods:
#         print(i)
# 
# for i in foods:
#    print(i, end=", ")
# 
# for i in prices:
#     total += i
#     print(f"You Total was: {total}")

#-------------- exercices
# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9),
#            ("*",0,"#"))
# 
# for i in num_pad:
#     for j in i:
#         print(j, end=" ")
#     print()

# ---------- dictionary <- when you have a key to indicate something 
#                      dictionary = {"key" : "reference"}
# you just need to delete the key, the operations is done majority making changes in the key 


# has_contrys = {"Brasil": "Brasilia", 
#                "Japão": "Tóquio", 
#                "Russia": "Moscou",
#                "Itália": "Roma"}
# 
# print(has_contrys.get("Brasil"))

# menu = {"pizza": 3.5, "coffee": 1.5, "pie": 3.0, }
# orders = []
# total = 0
# 
# for i, j in menu.items(): 
#     print(f"{i}: {j}")
# 
# while True: 
#     food = input("Order you food or (press q to quit) ").lower()
#     if (food == "q"):
#         break
#     elif (menu.get(food) is not None):
#         orders.append(food)
# 
# for i in orders:
#     total += menu.get(i)
#     print(i, end=" ")
# print()
# print(f"your total was: ${total} ")

# import random as rd
# 
# player = []
# machine = []
# choices = ["rock", "papper", "scissors"]
# while True:
#     player_choice = int(input("Chose the number: 0 for rock, 1 for papper or 2 for scissors "))
#         
#     player = choices[player_choice]
#     machine_choice = rd.randint(1,100)
# 
#     if(machine_choice < 33):
#         machine = choices[0]
#         print(f"Máquina escolheu: {machine}")
#     elif(machine_choice< 66):
#         machine = choices[1]
#         print(f"Máquina escolheu: {machine}")
#     else:
#         machine = choices[2]
#         print(f"Máquina escolheu: {machine}")
#         
#     if(player == machine):
#         print("Empate")
#     elif(player == choices[0] and machine == choices[1]):
#         print("Você perdeu")
#     elif(player == choices[1] and machine == choices[2]):
#         print("Você perdeu")
#     elif(player == choices[2] and machine == choices[0]):
#         print("Você perdeu")
#     else:
#         print("Você ganhou")
#         break

# task = []
# while True:
#     tasks = input("Adicione uma tarefa:   (1 -> sair) (2 -> check tasks) (3 -> Ver tarefas) ").lower()
#     if(tasks == "1"):
#         break
#     elif(tasks == "2"):
#         for i in range(len(task)):
#             print(f"{i} {task[i]}")
#         if(task is not None):
#             aux = int(input("Qual tarefa deseja dar check? Digite o indice "))
#             try:
#                 task.remove(task[aux])
#                 print("Check!")
#             except Exception as e:
#                 print("O indicê dessa terefa não existe")     
#     elif(tasks == "3"):
#         print(task)
#     else:
#         task.append(f"{tasks}")
#         print("tarefa adicionada")

# -------------------

# email = input("Insert your email ")
# 
# if "@" in email and "." in email:
#     print(" Valid email")
# else:
#     print("Invalid email")

# ---------------- List comprehension 

# doubles = [ i*2 for i in range(1,11)]
# print(doubles)


#------ Slots in python 

# import random
# 
# def spin_row():
#     symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
#     #results = []
#     # for symbol in range(3):
#     #     results.append(random.choice(symbols)) 
#     return [random.choice(symbols) for _ in range(3)]
# 
# def chec_win_condition(row, bet):
#     if(row[0] == row[1] == row[2]):
#         if(row[0] == '🍒'):
#             return bet * 3
#         if(row[0] == '🍉'):
#             return bet * 5
#         if(row[0] == '🍋'):
#             return bet * 6
#         if(row[0] == '🔔'):
#             return bet * 10
#         if(row[0] == '⭐'):
#             return bet * 20
#     else:
#         return 0
#          
# 
# def print_row(row):
#     print(" | ".join(row))
# 
# def main(): 
#     current_amount = 100
#     
# 
#     print("------------------------")
#     print("Welcome to python slots")
#     print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
#     print("------------------------")
#     print(f"Your money: {current_amount}")
#     
# 
#     while current_amount > 0:
#          bet = int(input("How much you wanna bet? "))
#          if(current_amount < bet):
#             print("You dont have enough money for it")
#          else:
#             print("... Spinning")
#             row = spin_row()
#             print_row(row)
#             current_amount -= bet
#             payout = chec_win_condition(row, bet)
#             if(payout > 0):
#                 print(f"You won: ${payout}!")
#             else:
#                 print("Sorry you lose this time")
#                 print()
# 
#             current_amount += payout
#             print (f"your currence amout: {current_amount}")
# 
# 
# 
# if __name__ == '__main__':
#     main()
# ------------ encripeted message
# import string
# import random 
# 
# chars = string.punctuation + string.digits + string.ascii_letters + " "
# chars = list(chars)
# key = chars.copy()
# 
# random.shuffle(key)
# 
# print(f"Chars: {chars}")
# print()
# print(f"Key: {key}")
# 
# message = input("Type the message that you want to encrypt ")
# cipher_text = ""
# 
# for leters in message:
#     aux = chars.index(leters)
#     cipher_text += key[aux]
# 
# print(f"your message: {message}")
# print(f"your encripted text: {cipher_text}")

# import random 
# 
# fruits = ("apple", "banana", "coconuts")
# 
# fork_man = {0: ("   ",
#                 "   ",
#                 "   "),
#             1: (" o ",
#                 "   ",
#                 "   "),
#             2: (" o ",
#                 " |  ",
#                 "   "),
#             3: (" o ",
#                 "/| ",
#                 "   "),
#             4: (" o  ",
#                 "/|\\",
#                 "    "),
#             5: (" o ",
#                 "/|\\",
#                 "  \\"),
#             6: (" o ",
#                 "/|\\ ",
#                 "/ \\"),}      
# 
#   
# 
# def display_man(worng_guess):
#     print("----------------")
#     for line in fork_man[worng_guess]:
#         print(line)
#     print("----------------")
#       
# 
# def display_hint(hint):
#     print(" ".join(hint))
# 
# 
# def disply_answer(answer):
#     print(answer)
#     
# def main():
#     secret_word = random.choice(fruits)
#     hint = ["_"] * len(secret_word)
#     print(secret_word)
#     worng_guesses = 0
#     guessed_leter = set()
#     is_running = True
# 
#     while is_running:
#         display_man(worng_guesses)
#         display_hint(hint)
#         guess = input("Guess a letter: ").lower()
# 
#         if len(guess) != 1 or not guess.isalpha():
#             print("------Invalid input------")
#             continue
# 
#         if guess in guessed_leter:
#             print(f"{guess} -> is alredy guessed")
#             continue
# 
#         guessed_leter.add(guess)
# 
#         if guess in secret_word:
#             for i in range(len(secret_word)):
#                 if secret_word[i] == guess:
#                     hint[i] = guess 
#         else:
#             print("There is not this letter")
#             worng_guesses += 1
#            
#         if "_" not in hint:
#             display_man(worng_guesses)
#             disply_answer(secret_word)
#             print("YOU WIN")
#             is_running == False
# 
# 
# 
# if __name__ == "__main__":
#     main()
# 
