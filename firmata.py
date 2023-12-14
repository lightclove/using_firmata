import pyfirmata
import time

class FirmataCommunicator:
    def __init__(self, port, baud_rate=57600):
        self.port = port
        self.baud_rate = baud_rate
        self.board = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.disconnect()

    def connect(self):
        self.board = pyfirmata.Arduino(self.port, self.baud_rate)
        self.setup_board()

    def disconnect(self):
        if self.board:
            self.board.exit()

    def setup_board(self):
        # Additional setup if needed
        pass

    def send_data(self, data):
        # Implement data sending logic
        pass

    def receive_data(self):
        # Implement data receiving logic
        pass

def main():
    port = "/dev/ttyUSB0"  # Change this to the correct port for your system

    with FirmataCommunicator(port) as firmata_communicator:
        # Your logic using the FirmataCommunicator
        firmata_communicator.send_data("Hello, Arduino!")
        time.sleep(1)
        received_data = firmata_communicator.receive_data()
        print(f"Received data: {received_data}")

if __name__ == "__main__":
    main()

# # Укажите соответствующий порт, например, "/dev/ttyUSB0" в Linux или "COM3" в Windows
# arduino_port = "/dev/ttyUSB0"

# board = Arduino(arduino_port)

# # Ожидание завершения инициализации
# it = util.Iterator(board)
# it.start()

# # Назначение функции обработки данных для каждого аналогового пина
# for pin in board.analog:
#     pin.enable_reporting()

# try:
#     # Основной цикл, в котором ожидаются данные от Arduino
#     while True:
#         # Печать данных с аналоговых пинов
#         for pin in board.analog:
#             print(f"Pin {pin.pin_number}: {pin.read()}")
# except KeyboardInterrupt:
#     # Обработка прерывания с клавиатуры (Ctrl+C)
#     print("\nПрервано пользователем.")
# finally:
#     board.exit()
#     print("Соединение с Arduino завершено.")
