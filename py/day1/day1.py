from py.helper.input import input_as_list_of_ints

"""
Given a list of integers, calculate number of increases in values
Naive solution: 
    iterate over list, and compare current value with value at previous index
    O(N) time | O(1) space, where N is number of ints in list
Elegant solution: 
    create copy of array shifted by 1 index, iterate over main and compare both with zip(arr[:-1, arr[1:]
    O(N) time | O(N) space because of extra copy, where N is number of ints in list
"""


def calculate_increases(depths: [int]) -> int:
    increase_count = 0
    for idx in range(len(depths)):
        if idx == 0:
            continue
        increase_count += int(depths[idx] > depths[idx - 1])
    return increase_count


def calculate_window_increase(depths: [int], window_size: int) -> int:
    increase_count = 0
    start_idx = 1  # Skip index 0 as we cannot calculate increase
    while start_idx + window_size <= len(depths):
        prev_idx = start_idx - 1
        curr_sum = sum(depths[start_idx:start_idx + window_size])
        prev_sum = sum(depths[prev_idx:prev_idx + window_size])
        increase_count += int(curr_sum > prev_sum)
        start_idx += 1
    return increase_count


if __name__ == "__main__":
    input_data = input_as_list_of_ints("input.txt")
    print(calculate_increases(input_data))
    print(calculate_window_increase(input_data, 3))
