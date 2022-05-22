import time
import random
from random_word import RandomWords

r = RandomWords()
ws = r.get_random_words()


name = input("ENTER YOUR NAME:  ")
print ("HELLO!!!, " + name," LET'S PLAY HANGMAN!!!")
print (" ")
turns = 10

choice= int(input("1.PLAY\n2.DIFFICULTY\n3.EXIT\nENTER YOUR CHOICE: "))
while choice!=3:
    if choice ==1:
        w = random.choice(ws)
        time.sleep(1)
        print ("CHANCES GIVEN: ",turns," CHANCES")
        print ("Start guessing...")
        time.sleep(0.5)

        guesses = ''

        while turns > 0:         
            failed = 0               
            for char in w:      
                if char in guesses:    
                    print (char, end=" ")    
                else:
                    print ("_" ,end=" ")    
                    failed += 1    

            if failed == 0:        
                print ("\nYOU WON !!!")  
                break              

            guess = input(" GUESS A CHARACTER: ") 
            guess = guess.lower()
            guesses += guess                    
            if guess not in w:  
                turns -= 1        
                print ("\nWrong !!!\n")    
                print ("You have", + turns, 'more guesses') 
                if turns == 0:           
                    print ("You Lose") 
                    print ("THE WORD WAS: ",w) 
                    print (" ")
        choice= int(input("1.PLAY\n2.DIFFICULTY\n3.EXIT\nENTER YOUR CHOICE: "))
    
    elif choice == 2:
        ch1 = int(input("SELECT THE DIFFICULTY LEVEL: \n1.HARD\n2.MEDIUM\n3.EASY\nENTER YOUR CHOICE: "))
        if ch1 == 1:
            turns = 3
        elif ch1 == 2:
            turns = 5
        else:
            turns = 10
        choice = 1
    
    elif choice == 3:
        exit(0)
    
    