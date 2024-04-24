# Objective: The aim of this assignment is to enhance your skills in using Python
#  sets for data analysis tasks. You will apply various set operations to
#  handle real-world data scenarios, focusing on their practical application and 
# efficiency.

# # Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, 
# some of which are duplicated. Write a Python function that takes in a list of 
# customer ID's, removes duplicates, prints each unique id, and returns a set of 
# the unique IDs

# Example Code:

# customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome: A set of unique customer IDs, ensuring no duplicates. 
#For instance, {'C001', 'C002', 'C003', 'C004'}.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]



def new_set(customer_ids):
        my_set= set(customer_ids)
        return my_set
print(new_set(customer_ids))