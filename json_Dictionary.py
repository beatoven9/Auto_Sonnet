import json


def encode_dict(word_dict, json_file):
    with open(json_file, 'w') as file:
        json.dump(word_dict, file, sort_keys=True, indent=4)


def decode_dict(json_file):
    try:
        with open(json_file, 'r') as file:
            return json.load(file)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        new_dictionary = {}
        return new_dictionary

