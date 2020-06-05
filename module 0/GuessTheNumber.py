import numpy as np
import random
count = 0                            # the attempt counter
number = np.random.randint(1,100)    # made a number from 1 to 100
print ("A number from 1 to 99 is hidden")

def game_core_v3(number):
    '''Start with min = 1, max = 99, predict = 50
    if predict is less than the number - use predict as maximum, 
    if predict is greater than the number - use predict as minimum,
    define a new predict by determining the half sum of the minimum and maximum'''
    count = 0
    min = 1
    max = 99
    predict = 50
    while number != predict:
        count+=1
        if number > predict: 
            min = predict
        elif number < predict: 
            max = predict
        predict = (max + min) // 2 
    return(count) # return the number of attempts


def score_game(game_core_v3):
    '''Run the game 1000 times to find out how fast the game guesses the number'''
    count_ls = []
    np.random.seed(1)  # fixing RANDOM SEED so that your experiment is reproducible!
    random_array = np.random.randint(100, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the hidden number of {score} attempts")
    return(score)



score_game(game_core_v3)