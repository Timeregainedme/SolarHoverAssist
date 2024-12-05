class Printer:
    def __init__(self, port):
        self.port = port

    def start_print(self, file):
        print(f"Printing {file} on port {self.port}.")

if __name__ == "__main__":
    printer = Printer("/dev/ttyUSB0")
    printer.start_print("sliced_model.gcode")
