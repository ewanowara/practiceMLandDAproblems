'''
Generate random input from an array according to given probabilities
'''

import random 
from random import randrange

import numpy as np
def probable_names(names, probabs):

    # check if the input names and corresponding probabilities are the same length, else return error
    if len(names) != len(probabs):
        return -1 

    prob_sum = [None] * len(names)# sum list from given probabilities - holds sum of all probability[j] for 0 <= j <= i 
    # by adding the next probability value to the sum of the previous ones we eventually get to 100 %, 
    # the range between the indices can be used to select the right name, the more narrow the range, the less likely to be selected
    prob_sum[0] = probabs[0]

    for i in range(1, len(names)):

    # generate a random integer from 1 to 100 for the probability
    r = randrange(1, 100)

    # check where it lies in prob_sum
    # separately handle 0th index
    if r <= prob_sum[0]:
        return names[0]
    for i in range(1, len(names)):
        if prob_sum[i-1] < r <= prob_sum[i]:
            return names[i]
    
    # else return error
    return -1

if __name__ == "__main__":
    # Example   
    names = ['David', 'Anthony', 'Paul', 'Jessica', 'Robert']
    probabs = [80, 5, 5, 5, 5]

    for j in range(10):  # run 10 times to compare the probability of each output
        name = probable_names(names, probabs)

        print(name)