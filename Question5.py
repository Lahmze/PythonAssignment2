from abc import ABC, abstractmethod


class FileHandler(ABC):
    """
    Abstract base class for handling files.
    Every file handler must implement read() and write().
    """

    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        """Read and return the file contents."""
        pass

    @abstractmethod
    def write(self, data):
        """Write data to the file."""
        pass


class TextFileHandler(FileHandler):
    """Handler for text files."""

    def read(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            return file.read()

    def write(self, data):
        if not isinstance(data, str):
            raise TypeError("Text files require string data.")

        with open(self.filename, "w", encoding="utf-8") as file:
            file.write(data)


class BinaryFileHandler(FileHandler):
    """Handler for binary files."""

    def read(self):
        with open(self.filename, "rb") as file:
            return file.read()

    def write(self, data):
        if not isinstance(data, bytes):
            raise TypeError("Binary files require bytes data.")

        with open(self.filename, "wb") as file:
            file.write(data)


# Creating a text-file handler
text_handler = TextFileHandler("example.txt")
text_handler.write("Hello, this is a text file.")
print(text_handler.read())


# Creating a binary-file handler
binary_handler = BinaryFileHandler("example.bin")
binary_handler.write(b"\x00\x01\x02\x03")
print(binary_handler.read())