from py.helper.input import input_as_list_of_strings
"""
Part 1:
Given a list of binary numbers, calculate most and least common bit column wise
Gamma obtained by iterating over columns and calculating most common bit, constructing the bitstring iteratively
Epsilon obtained by inverting the bits that make up gamma

Part 2:
Same as part 1, but recurse over numbers that match filter, narrowing down the search until one number remains
"""


def zero_pad(value: str, target_size: int) -> str:
    return value.rjust(target_size, "0")


def calculate_most_common_bit(bits: [int]) -> int:
    counts = {}
    highest_count = 0
    most_common_bit = 0
    for bit in bits:
        if bit not in counts:
            counts[bit] = 0
        counts[bit] += 1
        if counts[bit] > highest_count:
            highest_count = counts[bit]
            most_common_bit = bit
    if len(counts) == 2:
        if counts[0] == counts[1]:
            most_common_bit = 1
    return most_common_bit


def filter_numbers(target_bit: int, bit_idx: int, numbers: [int]) -> [int]:
    return [x for x in numbers if int(x[bit_idx]) == target_bit]


def calculate_power_consumption(diagnostics: [str]) -> (int, int):
    n_bits = len(diagnostics[0])

    def filter_bit(numbers, bit_idx, inverted=False):
        if len(numbers) == 1:
            return numbers[0]
        bits = [int(x[bit_idx]) for x in numbers]
        most_common_bit = calculate_most_common_bit(bits)
        if inverted:
            most_common_bit = abs(1 - most_common_bit)
        filtered_numbers = filter_numbers(most_common_bit, bit_idx, numbers)
        return filter_bit(filtered_numbers, bit_idx + 1, inverted)

    def calculate_gamma(numbers, bit_idx, n_bits, gamma_string):
        if len(gamma_string) == n_bits:
            return gamma_string
        bits = [int(x[bit_idx]) for x in numbers]
        most_common_bit = calculate_most_common_bit(bits)
        gamma_string += str(most_common_bit)
        return calculate_gamma(numbers, bit_idx + 1, n_bits, gamma_string)

    ox_rating = int(filter_bit(diagnostics, 0), 2)
    scrubber_rating = int(filter_bit(diagnostics, 0, inverted=True), 2)
    gamma = int(calculate_gamma(diagnostics, 0, n_bits, ""), 2)
    epsilon = 2 ** n_bits - 1 - gamma # Flip the bits, cannot use unary due to twos complement
    return gamma, epsilon, ox_rating, scrubber_rating


if __name__ == "__main__":
    input_data = input_as_list_of_strings("input.txt")
    gamma, epsilon, ox_rating, scrubber_rating = calculate_power_consumption(input_data)
    print(gamma * epsilon)
    print(ox_rating * scrubber_rating)
