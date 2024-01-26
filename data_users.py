import json


def load_data(data_path):
    try:
        with open(data_path, "r", encoding="UTF-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    return data


def save_data(user_data, data_path):
    with open(data_path, "w", encoding="UTF-8") as f:
        json.dump(user_data, f)