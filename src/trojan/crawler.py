import os
import sys
from typing import List


class Crawler:
    """
    A Crawler designed to traverse a file tree and print the files contained in it.
    """

    def __init__(self, target: str, extension_white_list: List[str] = [], abs_path: bool = False):
        """construct the File Crawler

        Arguments:
            target {str} -- the target directory for encryptioin

        Keyword Arguments:
            extension_white_list {List[str]} -- the list of file extensions to encrypt (default: {[]})
            abs_path {bool} -- whether or not to return the absolute path (default: {False})
        """

        self.target_directory: str = target
        self.files: List[str] = []
        self.file_extensions: str = extension_white_list
        self.abs_path: bool = abs_path

    def find_root(self) -> bool:
        """
        Returns whether or not the target directory is a directory, and finds the absolute path
        """
        return os.path.isdir(self.target_directory)

    def walk_tree(self) -> None:
        """
        Walks the given tree, and stores the individual file names encountered in the target directory
        """
        for root, subdirs, files in os.walk(self.target_directory):
            for file_name in files:
                for file_extension in self.file_extensions:
                    if file_name.endswith(file_extension):
                        if self.abs_path:
                            self.files.append(os.path.abspath(
                                root + os.sep + file_name))
                        else:
                            self.files.append(root + os.sep + file_name)

    def get_files(self) -> List[str]:
        """
        Get all the files that have been found by the Crawler

        Return:
            A list of strings, representing the file names of each file inside the target directory,
            with the given file extension.
        """
        return self.files
