import random
rock,paper,scissors="ROCK","PAPER","SCISSORS"
list1=[rock,paper,scissors]
print(list1)
we=input("What do you wantr to choose???\n ")
computer=random.choice(list1)
print("COMPUTER :::::",computer)
if computer=="ROCK":
  if we=="ROCK":
    print("DROW!!!!")
  elif we=="PAPER":
    print("You won!!!!")
  elif we=="SCISSORS":
    print("You Losse!!!")
  else:
    print("Please type valid answer")
elif computer=="PAPER":
  if we=="PAPER":
    print("DROW!!!")
  elif we=="ROCK":
    print("You Loose!!!")
  elif we=="SCISSORS":
    print("You Won!!!")
  else:
    print("Please type valid answer")
else:
  if we=="SCISSORS":
    print("DROW!!!")
  elif we=="ROCK":
    print("You Won!!!!")
  elif we=="PAPER":
    print("You Loose!!!")
  else:
    print("Please type valid answer")