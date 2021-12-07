import sys

from py.helper.input import input_as_ints

""" Advent of Code 2021 Day 7
Given a list of int positions, calculate a final position with the least distance from the initial positions.
Part 1
# Efficient using median
Median is defined as the least distance in the set, so a very efficient solution would be to calculate the sum of 
distances to move every position to the median.
# Naive approximation
Try every position from range(min(a), max(a)) where a is the set of initial positions. Return the lowest sum

Part 2
Same as part 1, but with an increasing cost per distance, so median does not work anymore. Naive method allows for
the extra fuel cost to be taken into account. 
Can be improved by searching on and close to mean value, instead of searching every single position.

"""


def calculate_fuel_cost(initial_positions: [int]) -> int:
    lowest_cost = sys.maxsize
    for target_pos in range(min(initial_positions), max(initial_positions)):
        fuel_cost = sum([sum(range(abs(target_pos - crab) + 1)) for crab in initial_positions])
        if fuel_cost < lowest_cost:
            lowest_cost = fuel_cost
    return lowest_cost


if __name__ == "__main__":
    initial_state = input_as_ints("input.txt")
    print(calculate_fuel_cost(initial_state))
