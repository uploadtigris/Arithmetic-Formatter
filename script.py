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
problem_arr = []
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]


#define the arithmetic arranger function
def arithmetic_arranger(problems):
  for i in problems:
    print(print(problems[i]))
    i+=1
#   arranged_problems = 'num'+' '+'operator'+' '+'num'

#   return arranged_problems

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

