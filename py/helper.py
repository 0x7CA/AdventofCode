import re


def input_as_string(file: str) -> str:
    with open(file) as f:
        return f.read().rstrip("\n")


def input_as_list_of_strings(file: str) -> [str]:
    return input_as_string(file).split("\n")


def input_as_list_of_ints(file: str) -> [int]:
    return list(map(int, input_as_list_of_strings(file)))


def input_as_list_of_int_grids(file: str, board_size: int) -> [[int]]:
    contents = input_as_list_of_strings(file)
    metadata = [int(x) for x in contents[0].split(",")]
    idx = 1
    grids = []
    while idx < len(contents):
        if contents[idx] == "":
            idx += 1
            grid_str = contents[idx:idx + board_size]
            grid = list(map(parse_grid_row_string_as_int, grid_str))
            grids.append(grid)
            idx += board_size
            continue
    return grids, metadata


def parse_grid_row_string_as_int(row: str) -> [int]:
    return [int(x) for x in re.findall('\\d+', row)]
