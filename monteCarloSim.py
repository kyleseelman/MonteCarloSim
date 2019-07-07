import random as r
import matplotlib.pyplot as plt

def rolldice():
    dice = r.randint(1,100)

    if dice <= 51:
        return False
    else:
        return True

def play_game(total_funds, bet_size, num_rounds):

    game_num = []
    funds = []
    ending_amount = []

    round = 1

    while round < num_rounds:
        if rolldice():
            total_funds = total_funds + bet_size
            game_num.append(round)
            funds.append(total_funds)
        else:
            total_funds = total_funds - bet_size
            game_num.append(round)
            funds.append(total_funds)
    
        round = round + 1
    
    plt.plot(game_num,funds)
    ending_amount.append(funds[-1])
    return(ending_amount)

iter = 1
while iter < 101:
    ending_fund = play_game(10000,100,10000)
    iter=iter+1

plt.ylabel('Player Money in $')
plt.xlabel('Number of bets')
plt.show()

print("The player starts the game with $10,000 and ends with $" + str(sum(ending_fund)/len(ending_fund))) 
