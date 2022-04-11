import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, "r") as soubor:
        slovnik = json.load(soubor)

    return slovnik[field]

def linear_search(sequention, number):
    new_dictionary = {"positions": [],
                      "count": 0}
    index = 0
    while True:
        if len(sequention) - 1 == index:
            break
        elif sequention[index] == number:
            new_dictionary["positions"].append(index)
            index = index + 1
        else:
            continue
    new_dictionary["count"] = sequention.count(number)

    return new_dictionary


def main():
    print(linear_search(read_data("sequential.json", "ordered_numbers"), 14))
    pass


if __name__ == '__main__':
    main()