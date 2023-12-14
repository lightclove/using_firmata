# Using Firmata

This project involves receiving and sending string data using the Firmata protocol between a host and an Arduino.

Firmata is a communication protocol for interfacing with microcontrollers like Arduino from software on a host computer. It enables bidirectional communication between the microcontroller and the host computer, allowing the computer to read inputs and control outputs on the microcontroller.

## Key Points about Firmata

### Bidirectional Communication
Firmata provides a standardized way for software on a host computer to communicate with a microcontroller (such as Arduino) over a serial connection. It allows the host to both send commands to the microcontroller and receive data from it.

### Protocol Overview
The Firmata protocol defines a set of commands that the host can send to the microcontroller to perform various actions. These commands cover a wide range of functionalities, including reading and writing digital and analog pins, configuring pins, reading and writing firmware version information, and more.

### Supported Platforms
Firmata is not limited to Arduino but is commonly associated with it. Firmata libraries and implementations are available for various platforms and microcontroller boards, making it versatile for different hardware configurations.

### Usage in Robotics and IoT
Firmata is often used in robotics and Internet of Things (IoT) projects where a microcontroller needs to be controlled and monitored by a host computer. It simplifies the communication process and allows developers to focus on building applications rather than dealing with low-level communication details.

### Firmata Libraries
There are Firmata libraries and implementations for different programming languages. For example, the "pyFirmata" library for Python allows developers to communicate with Arduino using Firmata.

### Customization and Extensions
While Firmata provides a standardized set of commands, it also allows for custom extensions. This means that developers can define their own commands for specific applications, providing flexibility for more advanced use cases.

## How to Use

1. Create a virtual environment:
    ```bash
    pyenv virtualenv 3.10.0 myenv
    pyenv activate myenv
    ```

2. Add these lines to your shell configuration file:
    ```bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"
    ```

3. Restart your shell:
    ```bash
    exec "$SHELL"
    ```

4. Activate the virtual environment:
    ```bash
    pyenv activate myenv
    ```

5. Install Python 3.10:
    ```bash
    pip install pyfirmata
    pip install --upgrade pyfirmata
    ```

6. Run the script:
    ```bash
    python3.10 firmata.py
    ```

7. Upload the sketch to your Arduino board.

## Troubleshooting

If you see symbols like "������������" instead of the expected data:

### Possible Solutions:

1. **Data Transfer Speed:**
   Make sure the data transfer speed in the port monitor matches the one set in your sketch (e.g., 57600 bits/s).

2. **Character Encoding:**
   Confirm that your port terminal or port monitor uses the correct character encoding (usually UTF-8). You can change the encoding in the Arduino IDE port monitor in the lower right corner.

3. **Incoming Data Processing:**
The Firmatacommunicator class has one responsibility - to provide communication with Arduino through Firmata Protocol.
The class can be expanded, for example, adding new methods for data processing without changing the existing code.
Inheritance is not used in this example.
The class with information (port and data transfer speed) is responsible for installing the connection.
High Cohesion: Class methods are due to the fact that all of them relate to interaction with Arduino.
