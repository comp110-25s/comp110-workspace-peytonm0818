"""Practice with dictionary functions"""

__author__: str = "730573512"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of a dictionary"""
    output: dict[str, str] = {}

    for key in input:
        if input[key] in output:
            raise KeyError("Duplicate key encountered")
        output[input[key]] = key

    print(output)
    return output


def count(count_list: list[str]) -> dict[str, int]:
    """Produces dictionary where keys are in list, values are # of times in list"""
    result: dict[str, int] = {}
    idx: int = 0

    while idx < len(count_list):
        if count_list[idx] in result:
            result[count_list[idx]] += 1
        else:
            result[count_list[idx]] = 1
        idx += 1

    print(result)
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the most frequent color"""
    color_count: dict[str, int] = {}
    top_color: str = ""
    stored_color: str = ""

    for key in favorites:
        if favorites[key] in color_count:
            color_count[favorites[key]] += 1
        else:
            color_count[favorites[key]] = 1

    for top_color in color_count:
        if stored_color == "":
            stored_color = top_color
        if color_count[top_color] > color_count[stored_color]:
            stored_color = top_color
    print(stored_color)
    return stored_color


def bin_len(input_list: list[str]) -> dict[int, set[str]]:
    """Sorts list of strings into sets based on the length of strings"""
    idx: int = 0
    output_dict: dict[int, set[str]] = {}

    while idx < len(input_list):
        int_key: int = len(input_list[idx])

        if int_key in output_dict:
            output_dict[int_key].add(input_list[idx])
        else:
            output_dict[int_key] = {input_list[idx]}
        idx += 1
    print(output_dict)
    return output_dict
