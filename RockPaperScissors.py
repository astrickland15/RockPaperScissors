import random



p1_score=0
p2_score=0

def main():
    lets_play()


def lets_play():

    global p1_score
    global p2_score

    input("Player 1: press enter to choose now! ")
    input("Player 2: press enter to choose now! ")

    choices=["rock", "paper", "scissors"]
    
    p1=random.choice(choices)
    p2=random.choice(choices)
    
    print("Player 1 selected " + p1)
    print("Player 2 selected " + p2)
    

    if p1=="rock" and p2=="scissors" or p1=="scissors" and p2=="paper" or p1=="paper" and p2=="rock":
        print("Congratulations, Player1.  You win")
        p1_score=p1_score+1
        player_scores()
        
        

    elif p2=="rock" and p1=="scissors" or p2=="scissors" and p1=="paper" or p2=="paper" and p1=="rock":
        print("Congratulations, Player 2.  You win")
        p2_score=p2_score+1
        player_scores()
       
        

    else:
        print("What a strange game.  The only way to win is not to play")
        player_scores()

def player_scores():

    print("Player 1 score: %d " % (p1_score))
    print("Player 2 score: %d " % (p2_score))



    try_again()

def try_again():


    play=input("Would you like to play again? ")
    

    

    if play=="y":
        
        lets_play()

    elif play=="n":
        print("Goodbye!")

    else:
        print("What, try again")
        try_again()
        
            

    
        


    
  

    
    


    
    
    
    
    
 
   
    

if __name__ == "__main__":
     main()