class SimpleApplication:
    def __init__(self, message="", author="untitled"):
        self.message = message

    def print_message(self):
        print(self.message)


if __name__ == "__main__":
    app = SimpleApplication("Hello world")
    app.print_message()