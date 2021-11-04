import sys
import time

FILENAME = "eng_vocab.txt"


def timer(func):
    def timer_wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Execution time: {(end - start):.7f} seconds ({func.__name__})")
        return result
    return timer_wrapper


class MyFileContextManager():
    def __init__(self, filename, operation):
        self.file_name = filename
        self.operation = operation

    def __enter__(self):
        try:
            self._file = open(self.file_name, self.operation)
            return self._file

        except FileNotFoundError:
            print("File not found")
            exit()

    def __exit__(self, type, value, traceback):
        self._file.close()


def my_generator(file):
    for item in file:
        yield item


@timer
def read_generator():
    with MyFileContextManager(FILENAME, "r") as file:
        generator = my_generator(file)
        for line in generator:
            pass  # Iterate through all lines of the file
        return generator


@timer
def read_list():
    with MyFileContextManager(FILENAME, "r") as file:
        return file.read().splitlines()


def main():
    print("Executing...")

    text_list = read_list()
    text_generator = read_generator()

    print(sys.getsizeof(text_list), "Bytes are used by the list")
    print(sys.getsizeof(text_generator), "Bytes are used by the generator")


if __name__ == "__main__":
    main()
