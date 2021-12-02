from py.helper import input_as_list_of_strings

""" Advent of Code 2021 Day 2
Given a series of commands like `forward 1`, calculate final horizontal position and depth
Return product of horizontal pos and depth

Keep struct for position with properties horizontal, depth, aim
Parse command and apply logic to position struct
Repeat for each command and return product of position

"""


class Command:
    def __init__(self, direction, step_size):
        self.direction = direction
        self.step_size = step_size


class Position:
    def __init__(self):
        self.horizontal_pos = 0
        self.depth = 0
        self.aim = 0


def calculate_position(command_list: [str]) -> Position:
    position = Position()
    for command_str in command_list:
        execute_command(parse_command(command_str), position)
    return position


def execute_command(cmd: Command, pos: Position):
    if cmd.direction == "forward":
        pos.horizontal_pos += cmd.step_size
        pos.depth += pos.aim * cmd.step_size
    elif cmd.direction == "up":
        pos.aim -= cmd.step_size
    elif cmd.direction == "down":
        pos.aim += cmd.step_size


def parse_command(command_str: str) -> Command:
    command_contents = command_str.split(" ")
    return Command(direction=command_contents[0],
                   step_size=int(command_contents[1]))


if __name__ == "__main__":
    input_data = input_as_list_of_strings("input.txt")
    final_pos = calculate_position(input_data)
    print(final_pos.horizontal_pos * final_pos.depth)
