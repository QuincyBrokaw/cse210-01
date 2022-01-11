"""
CSE 210
Week 02 Prove: Developer - Solo Code Submission.
Tic Tac Toe by Quincy Brokaw
Each player will be asked what number they want to replace with Either an X or O
"""
import colorama
from colorama import Fore, Style

class Game:   #This is where I set the global variables to be changed during game play
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5
        self.f = 6
        self.g = 7
        self.h = 8
        self.i = 9

    def draw(self):   #This creates the board
        print("{}|{}|{}".format(self.a, self.b, self.c))
        print("_+_+_")
        print("{}|{}|{}".format(self.d, self.e, self.f))
        print("_+_+_")
        print("{}|{}|{}".format(self.g, self.h, self.i))
        

    def x_turn(self):   #This is X's Turn
        num = input("X's turn to choose a square (1-9): ")
        if num == "1":
            self.a = "X"
             
        elif num == "2":
            self.b = "X"

        elif num == "3":
            self.c = "X"
            
        elif num == "4":
            self.d = "X"
            
        elif num == "5":
            self.e = "X"
        
        elif num == "6":
            self.f = "X"
            
        elif num == "7":
            self.g = "X"
            
        elif num == "8":
            self.h = "X"
            
        elif num == "9":
            self.i = "X"
            
    def y_turn(self):   #This is Y Turn
        num = input("Y's turn to choose a square (1-9): ")
        if num == "1":
            self.a = "Y"
             
        elif num == "2":
            self.b = "Y"

        elif num == "3":
            self.c = "Y"
            
        elif num == "4":
            self.d = "Y"
            
        elif num == "5":
            self.e = "Y"
        
        elif num == "6":
            self.f = "Y"
            
        elif num == "7":
            self.g = "Y"
            
        elif num == "8":
            self.h = "Y"
            
        elif num == "9":
            self.i = "Y"
    
    def check_win(self):    # This is to see if either player gets 3 across, 3 down, of 3 diaginoal.
        if self.a and self.b and self.c == "X":
            print("X wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.d and self.e and self.f == "X":
            print("X wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.g and self.h and self.i == "X":
            print("X wins!")    
            print("Good game. Thanks for playing!")
            quit()
        elif self.a and self.d and self.g == "X":
            print("X wins!")    
            print("Good game. Thanks for playing!")
            quit()
        elif self.b and self.e and self.h == "X":
            print("X wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.c and self.f and self.i == "X":
            print("X wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.a and self.e and self.i == "X":
            print("X wins!") 
            print("Good game. Thanks for playing!")
            quit()
        elif self.g and self.e and self.c == "X":
            print("X wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.a and self.b and self.c == "Y":
            print("Y wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.d and self.e and self.f == "Y":
            print("Y wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.g and self.h and self.i == "Y":
            print("Y wins!")    
            print("Good game. Thanks for playing!")
            quit()
        elif self.a and self.d and self.g == "Y":
            print("Y wins!")    
            print("Good game. Thanks for playing!")
            quit()
        elif self.b and self.e and self.h == "Y":
            print("Y wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.c and self.f and self.i == "Y":
            print("Y wins!")
            print("Good game. Thanks for playing!")
            quit()
        elif self.a and self.e and self.i == "Y":
            print("Y wins!") 
            print("Good game. Thanks for playing!")
            quit()
        elif self.g and self.e and self.c == "Y":
            print("Y wins!")
            print("Good game. Thanks for playing!")
            quit()  
                        
def main():  #This is the main, this is where we use a while to keep game play going.
    g = Game()
    g.draw()
    
    answer = ""
    while answer != "quit":
        answer = input("Who's turn: x or y?: ")
        if answer == "x":
            g.x_turn()
            g.draw()
            g.check_win()
        elif answer == "y":
            g.y_turn()
            g.draw()
            g.check_win()
         
    
if __name__ == "__main__":
    main()    