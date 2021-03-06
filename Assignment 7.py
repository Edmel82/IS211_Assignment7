#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Edwards Meliton IS-211-Assignment 7


import random

class Dice:
    def __init__(self, seed):
        random.seed(seed)

    def roll(self):
        return random.randint(1, 6)


class Players:
    def __init__(self, name):
        self.name = name
        self.total = 0
        

    def __str__(self):
        return f"{self.name} has {self.total}points"


class MainGame:
    def __init__(self, name1, name2):
        self.players = [Players(name1), Players(name2)]
        self.turn_total = 0
        self.total = 0
        self.current_player = 0

    def next_player(self):
        if self.current_player + 1 == len(self.players):
            self.current_player = 0
        else:
            self.current_player += 1

    def play(self):
        turn_total = 0
        while self.players[0].total < 100 and self.players[1].total < 100:
            turn_input = input(f'{self.players[self.current_player].name}, do you want to roll or hold? ')
            if turn_input == 'r':
                dice_value = random.randint(1, 6)
                if dice_value == 1:
                    print(f"{self.players[self.current_player].name} you roll a 1. Your score for this round is 0")
                    turn_total = 0
                    self.next_player()
                    continue
                else:
                    print(f"{self.players[self.current_player].name} you roll a {dice_value}.")
                    turn_total += dice_value
                    if turn_total + self.players[self.current_player].total >= 100:
                        self.players[self.current_player].total += turn_total
                        print(f"{self.players[self.current_player].name} you are the WINNER.")
                        print(f"Your winning score is {self.players[self.current_player].total}")
                        continue

                    print(f"Your turn score is {turn_total}")
                    print(f"Your possible score if you hold is {turn_total + self.players[self.current_player].total}")
            elif turn_input == 'h':
                self.players[self.current_player].total += turn_total
                print(f"Your score is {self.players[self.current_player].total}. Turn is over")
                turn_total = 0
                self.next_player()
            else:
                print("Game is over!")


def main():
    my_game = Game("Player1", "Player2")
    my_game.play()

main()


# In[ ]:





# In[ ]:




