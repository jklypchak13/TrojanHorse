from flask import Blueprint, request
import json
import string
import random
from typing import Dict
import os
encrypt = Blueprint('encrypt', __name__, None)


@encrypt.route('/encrypt/get_key')
def get_encryption_key() -> Dict[str, int]:
    """
    A route to fetch the encryption key of an id address

    Return:
    a dictionary with a key of key, and the ip's corresonding encryption key
    """
    data: Dict[str, Dict[str, any]] = {}
    data_file: str = "data/id.json"
    if(os.path.exists(data_file)):
        with open(data_file, "r") as fp:
            data = json.load(fp)

    ip: str = request.remote_addr
    key: str = -1
    id_number: int = 0

    # If the ip already exists, return the resulting value.
    if ip in data.keys():
        key = data[ip]['key']
    else:
        # New access, generate an id and random encryption key
        if(len(data) > 0):
            id_number: int = max(data.values(), key=lambda x: x['id'])[
                'id'] + 1
        key = ''.join([random.choice(string.ascii_letters)
                       for i in range(16)])

        data[ip] = {'id': id_number, 'key': key}
        with open(data_file, "w+") as fp:
            json.dump(data, fp)

    return {'key': key}
