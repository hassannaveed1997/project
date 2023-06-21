import random

# below is the game logic implemented as a function.
def game(seed = None):
    if seed: # set a random seed if one is provided
        random.seed(seed)
        
    A = 4
    B = 4
    pot = 2
    players = ['A', 'B']
    turn = 0 # the current turn. A is 0 and B is 1
    cycle = 0 # the current cycle

    while True:  # The game will continue until a player cannot complete a task
        roll = random.randint(1, 6)
        player = players[turn]
        cycle += (turn == 0) #increment the cycle whenever player A goes

        # All possibilities for player A
        if player == 'A':
            if roll == 1:
                pass  # do nothing
            elif roll == 2:
                A += pot
                pot = 0
            elif roll == 3:
                coins_taken = pot // 2
                A += coins_taken
                pot -= coins_taken
            else: # rolls 4, 5, 6
                if A == 0:  # Cannot complete the task
                    # print("Player B wins!")
                    return cycle, "B"
                else: # decement A's coins and increment the pot
                    A -= 1
                    pot += 1
        # All possibilities for player B
        else: 
            if roll == 1:
                pass  # do nothing
            elif roll == 2:
                B += pot
                pot = 0
            elif roll == 3:
                coins_taken = pot // 2
                B += coins_taken
                pot -= coins_taken
            else:
                if B == 0:  # Cannot complete the task
                    # print("Player A wins!")
                    return cycle, "A"
                else: # decement B's coins and increment the pot
                    B -= 1
                    pot += 1

        # update the turn
        turn += 1
        turn %= 2
