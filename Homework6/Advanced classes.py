# 1. Implement class iterator for Fibonacci numbers https://en.wikipedia.org/wiki/Fibonacci_number
# Iterator get numbers of first Fibonacci numbers.
print('Question 1.')
class fibonacci:

    def __init__(self, max):
        self.a, self.b = 0, 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max:
            raise StopIteration

        next_iter = self.a
        self.a, self.b = self.b, self.a + self.b

        return next_iter

for fibonacci_number in fibonacci(55):
    print(fibonacci_number)

# 2.* Implement generator for Fibonacci numbers.
print('Question 2.')

# Usage results in a concise code (generator):
# substitute any value instead of 'n'
n = 10
def fibonacci_gen(n):
    a, b = 0, 1
    for fibonacci_number in range(n):
        yield a
        a, b = b, a + b

print(*fibonacci_gen(n), sep = ", ")

# 3. Write generator expression that returns square numbers of integers from 0 to 10.
print('Question 3.')

squares = (n ** 2 for n in range(11))
for square in squares:
    print(square)

#4. Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
print('Question 4.')

from abc import abstractmethod, ABC
class Laptop (ABC):

    @abstractmethod
    def Screen(self):
        print("StartScreen")

    @abstractmethod
    def Keyboard(self):
        print(
            "Press Enter to move the cursor to the beginning of the next line. In a dialog box,press Enter to select the high lighted button.")

    @abstractmethod
    def Touchpad(self):
        print("The majority of touchpads work the same regard less of the laptop brand.")

    @abstractmethod
    def WebCam(self):
        print("Install the webcams software (if necessary)")

    @abstractmethod
    def Ports(self):
        print("You will find various types of ports, such as FireWire, Thunderbolt, HDMI, etc.")

    @abstractmethod
    def Dynamics(self):
        print("You must have a license to install the Dynamics 365 Guides PCapp. You can also signup for a free trial.")

class HPLaptop(Laptop):

    def Screen(self):
        print("StartScreen")

    def Keyboard(self):
        print(
            "Press Enter to move the cursor to the beginning of the next line. In a dialog box,press Enter to select the high lighted button.")

    def Touchpad(self):
        print("The majority of touchpads work the same regard less of the laptop brand.")

    def WebCam(self):
        print("Install the webcams software (if necessary)")

    def Ports(self):
        print("You will find various types of ports, such as FireWire, Thunderbolt, HDMI, etc.")

    def Dynamics(self):
        print("You must have a license to install the Dynamics 365 Guides PCapp. You can also signup for a free trial.")

HP = (HPLaptop())
HP.Ports()
HP.Screen()
HP.Keyboard()
HP.Touchpad()
HP.WebCam()
HP.Ports()
HP.Dynamics()

# 5. Create an abstract class for the Car with the next methods: drive, stop, open_door, close_door, turn_on_light,
# turn_off_light, enable_radio, disable_radio, where drive and stop will be predefined with some realization, all others
# should be abstract.
print('Question 5.')
class Car(ABC):

    def drive(self):
        print("Start the car")

    def stop(self):
        print("Stop the car")

    @abstractmethod
    def open_door(self):
        raise NotImplementedError

    @abstractmethod
    def close_door(self):
        raise NotImplementedError

    @abstractmethod
    def turn_on_light(self):
        raise NotImplementedError

    @abstractmethod
    def turn_off_light(self):
        raise NotImplementedError

    @abstractmethod
    def enable_radio(self):
        raise NotImplementedError

    @abstractmethod
    def disable_radio(self):
        raise NotImplementedError

class SUV(Car):
    def open_door(self):
        print("Opening the door")

    def close_door(self):
        print("Closing the door")

    def turn_on_light(self):
        print("Turning the lights on")

    def turn_off_light(self):
        print("Turning the lights off")

    def enable_radio(self):
        print("Enabling radio, play music")

    def disable_radio(self):
        print("Disabling radio, music off")

Volvo = (SUV())
Volvo.disable_radio()
Volvo.enable_radio()
Volvo.open_door()
Volvo.close_door()
Volvo.turn_on_light()
Volvo.turn_off_light()
