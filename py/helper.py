def input_as_string(file: str) -> str:
    with open(file) as f:
        return f.read().rstrip("\n")


def input_as_list_of_strings(file: str) -> [str]:
    return input_as_string(file).split("\n")


def input_as_list_of_ints(file: str) -> [int]:
    return list(map(int, input_as_list_of_strings(file)))
