import time
import random   


file = open('english_words_1.txt', 'r')
english_words = set(file.read())
file.close()

def registration(player_base):
    for i in range(1, 3):
        print(i, ' player:')
        player_name = input().strip().capitalize()
        player_base[player_name] = 1

def check_word_exist(word):
    return word in english_words

def play_game():
    previous_word = 'a'
    player_base = {}
    running = True
    move_time = 10
    word = ''

    registration(player_base)
    print('first word starts with a')
    while running:
        for i in player_base:
            losers = []
            player_base[i] = 0
            start_time = time.time() # starting timer
            print(i, "'s turn")

            while (time.time() - start_time) < move_time:
                word = input('Enter word: ').strip().lower()
                if check_word_exist(word) and word[0] == previous_word[-1]:
                    previous_word = word
                    player_base[i] = 1
                    break
                elif not check_word_exist(word):
                    print('Enter real word')
                elif word[0] != previous_word[-1]:
                    print("Your word first letter should be: ", previous_word[-1])
            
            if player_base[i] == 0:
                losers.append(i)

        for i in losers:
            del player_base[i]

        if len(player_base) <= 1:
            winner = list(player_base.keys())
            print(winner[0], ' Won!')
            return 0

play_game()