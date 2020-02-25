import os
from typing import List


class Crawler:
    """
    A Crawler designed to traverse a file tree and print the files contained in it.
    """

    def __init__(self, target: str, extension: str = '.*'):
        """
        Creates a new Crawler for the given target, of files with the given extension.

        target: the target directory.
        extension: the desired file extension (defaults to any extension)
        """

        self.target_directory: str = target
        self.files: List[str] = []
        self.file_extension: str = extension

    def find_root(self) -> bool:
        """
        Returns whether or not the target directory is a directory, and finds the absolute path
        """
        self.absolute_path_target: str = os.path.abspath(self.target_directory)
        return os.path.isdir(self.target_directory)

    def walk_tree(self) -> None:
        """
        Walks the given tree, and stores the individual file names encountered in the target directory
        """
        current_path: str = self.target_directory
        current_dir: str = self.target_directory

    def get_files(self) -> List[str]:
        """
        Returns a list of all the different files of the given file type
        """
        return self.files
