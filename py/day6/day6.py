from py.helper.input import input_as_ints


def calculate_fish(initial_state, n_days):
    fish_state = [0] * 9
    for fish_state_index in initial_state:
        fish_state[fish_state_index] += 1
    for days in range(n_days):
        fish_state.append(fish_state.pop(0))  # Rotate the "days" to the left, putting day 0 back at the end to day 8
        fish_state[6] += fish_state[8]  # Start maturing our fish that were on hold
    return sum(fish_state)


if __name__ == "__main__":
    initial_state = input_as_ints("input.txt")
    print(calculate_fish(initial_state, 256))