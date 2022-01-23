import math
from typing import List, Union

def average(integers: List[List[int]]) -> float:
    """
    Return the average of of a list of list of integers 
    Input: a list of lists of integers
    Output: the average of all integers (rounded to 1 decimal)
    """
    count = 0
    sum = 0
    for list in integers:
        for i in list:
            count += 1
            sum += i
    average = round(sum / count, 1)
    return average


def standard_deviation(integers: List[List[int]]) -> float:
    """
    Return the standard deviation of a list of list of integers 
    Input: a list of lists of integers
    Output: the standard deviation of all integers (rounded to 1 decimal)
    """
    sum_squares = 0.0
    count = 0
    mean = average(integers)
    for list in integers:
        for i in list:
            sum_squares += (i - mean) ** 2
            count += 1
    std = round(math.sqrt(sum_squares / count), 1)
    return std


def covariance(integers: List[List[int]]) -> float:
    """
    Return the covariance of two list of integers 
    Input: two lists of integers
    Output: the covariance of the two lists (rounded to 0 decimal)
    """
    x, y = integers[0], integers[1]
    x_mu, y_mu = sum(x) / len(x), sum(y) / len(y)
    n = len(x)
    ex = [(i - x_mu) for i in x]
    ey = [(i - y_mu) for i in y]
    prod_deviation = [a * b for a, b in zip(ex, ey)]
    return round(sum(prod_deviation) / n, 0)


def correlation(integers: List[List[int]]) -> float:
    """
    Return the Pearson Correlation score for the two lists
    Input: two lists of integers
    Output: the Pearson Correlation score (rounded to 3 decimals)
    """
    x, y = integers[0], integers[1]
    x_mu, y_mu = sum(x) / len(x), sum(y) / len(y)
    # calculate product of deviation scores
    ex = [(i - x_mu) for i in x]
    ey = [(i - y_mu) for i in y]
    prod_deviation = [a * b for a, b in zip(ex, ey)]
    # calculate the standard deviation for both lists
    ss_x = [(i - x_mu) ** 2 for i in x]
    ss_y = [(i - y_mu) ** 2 for i in y]
    n = len(x)
    std_x, std_y = math.sqrt(sum(ss_x)), math.sqrt(sum(ss_y))
    return round(sum(prod_deviation) / (std_x * std_y), 3)


def get_data(path: str) -> List[List[int]]:
    list_list = []
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            list_int = []
            for i in line.split(" "):
                list_int.append(int(i.strip()))
            list_list.append(list_int)
    return list_list


def analyze_data(integers: List[List[int]], statistics: str)-> Union[float, str]:
    """
    Returns a floating point number
    Input: a list of lists of integers
    Output: a string option that can be one of the following:
        * "average" (of all the data together)
        * "standard deviation" (of all the data together)
        * "covariance" (between the two lists)
        * "correlation"
    """
    
    if statistics == "average":
        return average(integers)
    elif statistics == "standard deviation":
        return standard_deviation(integers)
    elif statistics == "covariance":
        return covariance(integers)
    elif statistics == "correlation":
        return correlation(integers)
    else:
        return "Not available"


# Code to test:
def main():
     integers = get_data("integers.txt")
     print(integers)
     print(analyze_data(integers, "average"))
     print(analyze_data(integers, "standard deviation"))
     print(analyze_data(integers, "covariance"))
     print(analyze_data(integers, "correlation"))


# if __name__ == "__main__":
#     main()
