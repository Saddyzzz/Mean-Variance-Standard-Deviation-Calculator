import numpy as np

def calculate(lst):
    # Raise an error if the list doesn't contain 9 numbers
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    # Reshape the list into a 3x3 NumPy array
    matrix = np.array(lst).reshape(3, 3)

    # Calculate mean
    mean_axis1 = matrix.mean(axis=0).tolist()   # Mean along the columns
    mean_axis2 = matrix.mean(axis=1).tolist()   # Mean along the rows
    mean_flattened = matrix.mean().tolist()     # Mean of all elements

    # Calculate variance
    variance_axis1 = matrix.var(axis=0).tolist()
    variance_axis2 = matrix.var(axis=1).tolist()
    variance_flattened = matrix.var().tolist()

    # Calculate standard deviation
    std_axis1 = matrix.std(axis=0).tolist()
    std_axis2 = matrix.std(axis=1).tolist()
    std_flattened = matrix.std().tolist()

    # Calculate max
    max_axis1 = matrix.max(axis=0).tolist()
    max_axis2 = matrix.max(axis=1).tolist()
    max_flattened = matrix.max().tolist()

    # Calculate min
    min_axis1 = matrix.min(axis=0).tolist()
    min_axis2 = matrix.min(axis=1).tolist()
    min_flattened = matrix.min().tolist()

    # Calculate sum
    sum_axis1 = matrix.sum(axis=0).tolist()
    sum_axis2 = matrix.sum(axis=1).tolist()
    sum_flattened = matrix.sum().tolist()

    # Construct the dictionary with all results
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations


print(calculate([0,1,2,3,4,5,6,7,8]))
