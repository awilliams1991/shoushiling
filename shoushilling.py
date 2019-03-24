import random

winner = ''
#start the basic setup for random function and defining winner
random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'
#using random.randint can randomly pick 0,1, or 2
    #assign value to each number for rock paper scissors

user_choice = ''
while (user_choice != 'rock' and
    user_choice != 'paper' and
    user_choice != 'scissors') :
  user_choice = input('rock, paper or scissors?  ' )
print('User chose' , user_choice)  
    
#give user a chance to input their choice

if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'
#define conditions of winning and make sure winner is corrected to display the
    #correct winner
if winner == 'Tie':
    print('We both chose' , computer_choice + ', play again.')

else:
    print(winner, 'won, I chose' , computer_choice + '.')


#announce the winner or it there was a tie along with what the computer chose

#could have simplified choices using:
    #choices = [ 'rock' , 'paper' , 'scissors']
    #computer_choice = random.choice(choices)
#instead of using if and elif
