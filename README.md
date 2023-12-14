# using_firmata
Прием и передача строковых данных по протоколу firmata между хостом и Arduino 
Firmata is a communication protocol for interfacing with microcontrollers like Arduino from software on a host computer. It enables bidirectional communication between the microcontroller and the host computer, allowing the computer to read inputs and control outputs on the microcontroller.
Here are some key points about Firmata:

    Bidirectional Communication:
    Firmata provides a standardized way for software on a host computer to communicate with a microcontroller (such as Arduino) over a serial connection. It allows the host to both send commands to the microcontroller and receive data from it.

    Protocol Overview:
The Firmata protocol defines a set of commands that the host can send to the microcontroller to perform various actions. These commands cover a wide range of functionalities, including reading and writing digital and analog pins, configuring pins, reading and writing firmware version information, and more.

Supported Platforms:
    Firmata is not limited to Arduino but is commonly associated with it. Firmata libraries and implementations are available for various platforms and microcontroller boards, making it versatile for different hardware configurations.

    Usage in Robotics and IoT:
Firmata is often used in robotics and Internet of Things (IoT) projects where a microcontroller needs to be controlled and monitored by a host computer. It simplifies the communication process and allows developers to focus on building applications rather than dealing with low-level communication details.

Firmata Libraries:
There are Firmata libraries and implementations for different programming languages. For example, the "pyFirmata" library for Python allows developers to communicate with Arduino using Firmata.

Customization and Extensions:
While Firmata provides a standardized set of commands, it also allows for custom extensions. This means that developers can define their own commands for specific applications, providing flexibility for more advanced use cases.

To use Firmata, you typically upload a Firmata sketch to the microcontroller, and then you use a library or implementation of Firmata in your host software to communicate with the microcontroller over a serial connection. This allows you to control the microcontroller and read data from it in a standardized way.
