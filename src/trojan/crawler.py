import os
from typing import List


class Crawler:
    """
    A Crawler designed to traverse a file tree and print the files contained in it.
    """

    def __init__(self, target: str, extension: str = None, abs_path: bool = False):
        """
        Creates a new Crawler for the given target, of files with the given extension.

        Arguments:
            target: the target directory.
            extension: the desired file extension (defaults to any extension)
            abs_path: whether you want files to be the absolute or relative path, from the target
        """
        self.target_directory: str = target
        self.files: List[str] = []
        self.file_extension: str = extension
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
                if self.file_extension is None or self.file_extension in file_name:
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
