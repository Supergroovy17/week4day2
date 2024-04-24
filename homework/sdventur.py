# 1. Python Sets Adventure
# Objective:
# The aim of this assignment is to deepen your understanding and application of Python sets in various scenarios, 
#ranging from basic operations to advanced manipulations and best practices. You will correct given codes, use sets in everyday contexts, and tackle challenges that require creative 
#thinking 
#and problem-solving.

# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. 
#Write a Python program to find out:

# Destinations that both airlines fly to.
# Destinations unique to your airline.
# Whether there are any destinations that neither airline shares.
# Example Code:

#https://www.markdownguide.org/cheat-sheet/


our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def flights(our_routes, competitor_routes):
    settt = our_routes.intersection(competitor_routes)
    return settt
print(flights(our_routes, competitor_routes))

def flights_(our_routes, competitor_routes):
    sett = our_routes.difference(competitor_routes)
    return sett
print(flights_(our_routes, competitor_routes))


def flights__(our_routes, competitor_routes):
    sett = our_routes.symmetric_difference(competitor_routes)
    return sett
print(flights__(our_routes, competitor_routes))












