"""
Script  : devices.py
By      : Hesham Elhadad
ID      : L00177542
Date    : 22-Oct-22
Purpose : This script demonstrates a sample code to build various networking devices
          The code was given by John O'Raw as part of walkthrough_08

Tested  : Python 3.10 on Windows 10
Rev     : 0
IDE     : PyCharm CE ver 2022
"""


# In any complex application, create a base class which will never be instantiated.
class Device():
    # Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142

    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for base class")
        # Create attributes and set initial values
        self.debug = False

    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")

    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from base")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc


""" 
Child class Template by JOR 
"""


# Create child class which can access the methods and properties of the base class
class Firewall(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}")
        # Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""

    def configure_firewall(self):
        print("Configuring Firewall")

    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from child")
        # Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc


"""
    The following code is the student work as a solution of the exercise
"""


class Switch(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, switch_name, ports_number, layer) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {switch_name}")
        # Create attributes and set initial values
        self.switch_name = switch_name
        self.ports_number = ports_number
        self.layer = layer
        self.test_message = ""

    def configure_switch(self):
        print(f"Configuring switch {self.switch_name} of {self.ports_number} ports which run on layer {self.layer}")

    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from child")
        # Put real code in here, this is a dummy value for initial setup
        crc = 39384595984
        return crc


class LoadBalancer(Device):

    # Constructor, called whenever an instance of the class is created.
    # Use parameter1 as a tag to identify the object
    def __init__(self, lb_name, role, layer) -> None:
        # Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {lb_name}")
        # Create attributes and set initial values
        self.lb_name = lb_name
        self.layer = layer
        self.role = role
        self.test_message = ""

    def configure_loadbalancer(self):
        print(f"Configuring load balancer {self.lb_name} of role type {self.role} which run on layer {self.layer}")

    def calculate_crc(self, frame: str) -> int:
        print("Checking CRC from child")
        # Put real code in here, this is a dummy value for initial setup
        crc = 39384595984
        return crc
