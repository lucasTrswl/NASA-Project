import json


def write_config_file(path_file, data):
    # data = [1, 2, 3, 4, 5]
    with open(path_file, "w") as f:
        json.dump(data, f)
