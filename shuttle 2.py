class CampusShuttle:
    def __init__(self, registration_number, initial_speed):
        self.registration_number = registration_number  # public
        self.__speed = 0  # private - controlled
        self.set_speed(initial_speed)  # use setter to validate initial speed

    def get_speed(self):
        return self.__speed

    def set_speed(self, new_speed):
        # Rules: 0 <= speed <= 80
        if 0 <= new_speed <= 80:
            self.__speed = new_speed
            print(f"Speed set to {self.__speed} km/h")
        else:
            print(f"Invalid speed {new_speed} km/h! Must be 0-80. Speed remains {self.__speed} km/h")

# Required test
print("--- Campus Shuttle Speed Control ---")
shuttle = CampusShuttle("UAX 123A", 40)
print(f"Initial speed: {shuttle.get_speed()} km/h\n")

# T
for test_speed in [60, 100, -20]:
    print(f"Attempting to set speed to {test_speed} km/h...")
    shuttle.set_speed(test_speed)
    print(f"Displayed speed after attempt: {shuttle.get_speed()} km/h\n")

print(f"Shuttle {shuttle.registration_number} final speed is {shuttle.get_speed()} km/h")