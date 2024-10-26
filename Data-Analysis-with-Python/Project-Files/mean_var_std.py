"""
Name: Otite Idogun
Academy: FreeCodeCamp
Course: Data Analysis with Python
Project Title: Mean-Variance-Standard Deviation Calculator
"""

#Step 1: Import numpy library
import numpy as np

# Step 2: Create function
def calculate(*input_list):
    
    # Step 3: Check Input Validation
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Step 4: Convert to NumPy Array
    matrix = np.array(input_list).reshape(3, 3)
    
    # Step 5: Calculate Statistics
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()]
    sum_val = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    
    # Step 6: Store Results in a Dictionary
    result = {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': sum_val
    }
    
    # Step 7: Return the Dictionary
    return result


print(calculate(0,1,2,3,4,5,6,7,8))

