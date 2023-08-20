import random

pictures = {
"R":"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",

"cR":"""
                                _______
                               (____   '---
                              (_____)
                              (_____)
                               (____)
                                (___)__.---
""",

"P":"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",

"cP": """
                                        _______
                                   ____(____   '---
                                  (______
                                  (_______
                                   (_______
                                     (_________.---
""",

"S":"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",

"cS":"""
                                      _______
                                 ____(____   '---
                                (______
                               (__________
                                     (____)
                                      (___)__.---
"""}
print("Want to play rock paper scissors, but no one else wants to? Well, you can play with me! But be warned, I'm not gonna go easy on you!")
print('')
score = 0
p = .40
r = .30
s = .30
whowon = 0 
win_move = None
lose_move = None

for game in range(6) :

	user = input("Type in R for rock, P for paper, and S for scissors!")

	computer = random.choices( ["P","R","S" ], [p,r,s], k=1 )
	computer = ''.join(computer) 
	
	if user== "R" and computer=="P":
		
		print( "\n Nice try! Computer played paper! \n")
		print("user move")
		print(pictures["R"], pictures["cP"])
		print("                                computer move")
		whowon = 1
		win_move = "P"

	elif user==computer:
		print("Tie!")
		whowon = 0
		win_move = None

	elif user== "P" and computer=="R":
		print("\n Good job! Computer played rock! \n")
		print("user move")

		print(pictures["P"], pictures["cR"])
		print("                                computer move")

		score += 1
		whowon = -1
		lose_move = "R"

	elif user== "S" and computer=="P":
		print("\n Good job! Computer played paper! \n")
		print("user move")

		print(pictures["S"], pictures["cP"])
		print("                                computer move")

		score += 1
		whowon = -1
		lose_move = "P"
		
	elif user== "P" and computer=="S":

		print("\n Nice try! Computer played scissors! \n")
		print("user move")

		print(pictures["P"],pictures["cS"])
		print("                                computer move")
		whowon = 1
		win_move = "S"
	

	elif user== "S" and computer=="R":
		print("\n Nice try! Computer played rock! \n")
		print("user move")

		print(pictures["S"],pictures["cR"])
		print("                                computer move")
		whowon = 1
		win_move = "R"
	
	elif user== "R" and computer=="S":

		print("\n Good job! Computer played scissors! \n")	
		print("user move")

		print(pictures["R"],pictures["cS"])
		print("                                computer move")

		score += 1
		whowon = -1
		lost_move = "S"


	if whowon==  1: #If computer wins, which means whowon = 1
		if win_move == "R":
			r = .25 
			p = .50
			s = .25
		elif win_move == "S":
			r = .50
			p = .25
			s = .25
		elif win_move == "P":
			r = .25
			p = .25
			s = .50
	else:
		if lose_move == "R":
			r = .25
			p = .25
			s = .50
		elif lose_move == "S":
			r = .25
			s = .25
			p = .50
		elif lose_move == "P":
			r = .50
			p = .25
			s = .25
	print("\n")		

print("Good game! You wore my hard drive out! Here is your score:", score, ". GOOD-BYE!")		