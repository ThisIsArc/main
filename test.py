import random 

print("Rock...\nPaper...\nScissors...")
print("--------------------")

win1 = 0 
win2 = 0 
WinScore = 4 

while win1 < WinScore and win2  < WinScore : 
    
    randommove = random.randint(1,3)
    if randommove == 1 :
        Almove = "paper"
    elif randommove == 2 : 
        Almove = "rock"
    elif randommove == 3 : 
        Almove = "scissors"
        
    player1 = input("Player 1 Please Make Your Move :")
    print(f"Player 2 Please Make Your Move : {Almove}")
    
    player2 = Almove
    if player1 == "rock" :
        if player2 == "paper" :
            print("player 2 Won!!!")
            win2 += 1 
        elif player2 == "scissors" : 
            print("player 1 Won!!!")
            win1 += 1 
    elif player1 == "paper" : 
         if player2 == "rock" :
            print("player 1 Won!!!")
            win1 += 1
         elif player2 == "scissors" : 
            print("player 2 Won!!!")
            win2 += 1 
    elif player1 == "scissors" : 
        if player2 == "paper" : 
            print("player 1 Won!!!")
            win1 += 1 
    elif player2 == "rock" : 
        print("player 2 Won!!!")
        win2 += 1
print("--------------------")
print(f"Player 1 Wins : {win1} | player 2 Wins : {win2}")