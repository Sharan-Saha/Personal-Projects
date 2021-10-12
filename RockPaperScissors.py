import random
import time
throws = ['R', 'P', 'S']
print("Welcome to Rock Paper Scissors!")
win_counter = 0
loss_counter = 0
tie_counter = 0
keep_going = True
throws_list = []
def change_list():
    if len(throws_list) > 5:
        throws_list.pop(0)


def adapt():
    throws_dict = {
        "R" : 0,
        "P" : 0,
        "S" : 0
    }


    for element in throws_list:
        if element == 'R':
            throws_dict["R"] += 1
        if element == 'P':
            throws_dict["P"] += 1
        if element == 'S':
            throws_dict["S"] += 1

    most_thrown = max(throws_dict, key = throws_dict.get)
    if most_thrown == "R":
        return "P"
    if most_thrown == "P":
        return "S"
    if most_thrown == "S":
        return "R"


def game():
    global win_counter
    global loss_counter
    global tie_counter
    game_counter = (win_counter + loss_counter + tie_counter + 1)
    player_input = input("Enter 'R'(ock), 'P'(aper), or 'S'(cissors) or 'stop' if you want to stop ")
    player_input = player_input.upper()
    if game_counter < 12:
        computer = random.choice(throws)
    else:
        computer = adapt()
    
    if player_input.upper() == 'R' and computer == 'S':
        throws_list.append(player_input)
        print("You: " + player_input.upper() + ", computer: " + computer)
        print("You win")
        win_counter += 1
        change_list()
    elif player_input.upper() == 'P' and computer == 'R':
        throws_list.append(player_input)
        print("You: " + player_input.upper() + ", computer: " + computer)
        print("You win")
        win_counter += 1
        change_list()
    elif player_input.upper() == 'S' and computer == 'P':
        throws_list.append(player_input)
        print("You: " + player_input.upper() + ", computer: " + computer)
        print("You win")
        win_counter += 1
        change_list()
    elif player_input.upper() == computer:
        throws_list.append(player_input)
        print("You: " + player_input.upper() + ", computer: " + computer)
        print("Tie")
        tie_counter += 1
        change_list()
    else:
        throws_list.append(player_input)
        print("You: " + player_input.upper() + ", computer: " + computer)
        print("You lose")
        loss_counter += 1
        change_list()

while keep_going == True:
    print("Game " + str(win_counter + loss_counter + tie_counter + 1))
    game()
    print("Results")
    print("Wins: " + str(win_counter))
    print("Losses: " + str(loss_counter))
    print("Ties: " + str(tie_counter))
    print(throws_list)
    print("____________________________________________")

