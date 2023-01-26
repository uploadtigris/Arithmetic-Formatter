##################################################
#
# Author: Tigris Mendez
# Date: 1/24/23
# Program: Arithmetic Formatter
# Description: 
#   This is a simple Arithmetic Formatter and Calculator
#   that will perform simple calculations and will perform
#   and display simple arithmetic.
#
##################################################

#Sudo Code

#read the user input

#Error Cases
#if 5 or more errors occur, print ("Error: to many problem")
#throw error if operators are other than plus or minus
#throw error if the string contains anything other than DIGITS
#throw error if the string contains numbers over 4 digits

#repeat input if any Error thrown

#find a word before a space
#if a space appears, place that preceeding word into a dictionary
#skip space
#for every operator, store it in the dictionary
#a dictionary should have a 2 integers as strings and an operator BUT it should be allowed multiple.

#Printing
#a single space between the operator and the longest of the two operands
#the operator will be on the same line as the second operand
#the numbers should be right allinged
#There should be four spaces between each problem
#find length of longest num and write that many dashes at bottom of the problem

#-----------------------------------------------------
import numpy as np

first_ttl = 0
second_ttl = 0
len_first = []
len_third = []
first_arr = []
third_arr = []
problem_arr = []
calc_arr = []
prob_item_lengths = []
problem = []



def arithmetic_arranger(problems):
    for x in problems:
        #separate each item in problems into a number, operator, and number
        problem.append(str.split(x))

    #separating the items into different arrays
    for x in range(len(problem)):
        # 1st Operand, Operator, 2nd Operand
        np.array(first_arr.append(problem[x][0]))
        np.array(third_arr.append(problem[x][2]))

    #one array of all values given... for later
    problem_arr = np.concatenate((first_arr, third_arr))
        
    #measuring the length for each item in the first index of 'poblem' 
    for x in range(len(problem)):
        # 1st Operand, Operator, 2nd Operand
        np.array(len_first.append(len(problem[x][0])))      
        np.array(len_third.append(len(problem[x][2])))

    #one array to measure the length of all given values
    problem_item_lengths = np.concatenate((len_first, len_third))




   #Error handling

   # if any digit is larger than 4 digit -> error
    for i in problem_item_lengths:
        if problem_item_lengths[i] > 4:
            print('no digit length over 4 is allowed, please enter equations again')
            return
        else:
            continue

   # the operator must be a + or a -
   # why won't they register incorrect if I use a 'or' operator between the + and - ?
    for i in range(len(problem)):
        if problem[i][1] == '+':
            continue
        elif problem[i][1] == '-':
            continue
        else:
            print('only the operators + and - are allowed. Please enter equations again')
            return

   # the numbers must only be digits
    for i in range(len(problem_arr)):
        if (problem_arr[i].isnumeric):
            continue
        else:
            print('only numeric values of four whole digits are allowed. Please enter equations again')
            return



   #Return

   # single space between operator and bottom operand
   # numbers should be right aligned
   # four spaces between each problem
   # The dashes will elongate dynamically according to the length of the operands

    # return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

