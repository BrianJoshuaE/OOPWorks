class CampusShuttle:
    def __init__(self, registration_number: str, initial_speed: float = 0.0):
        # The registration number is public and can be read directly.
        self.registration_number = registration_number
        # Keep speed private so it can only be changed through set_speed().
        self.__speed = 0.0
        # Use the setter so the starting speed follows the same validation rules.
        self.set_speed(initial_speed)

    def get_speed(self) -> float:
        # Return the current speed without changing it.
        return self.__speed

    def set_speed(self, new_speed: float) -> None:
        # Accept only speeds from 0 to 80 km/h, inclusive.
        if 0 <= new_speed <= 80:
            # Update the stored speed only after the value passes validation.
            self.__speed = new_speed
        else:
            # No assignment happens here, so the last valid speed is preserved.
            print(f"  [X] Rejected Invalid Speed Change: {new_speed} km/h (Must be between 0 and 80 km/h)")


if __name__ == "__main__":
    # Create a shuttle with a valid starting speed of 40 km/h.
    print("--- Creating Campus Shuttle ---")
    shuttle = CampusShuttle("UAG 979J", 40)
    print(f"Shuttle '{shuttle.registration_number}' initialized. Current Speed: {shuttle.get_speed()} km/h\n")

    print("--- Testing Speed Changes ---")

    # 60 is valid; 100 and -20 should be rejected.
    test_speeds = [60, 100, -20]

    for speed in test_speeds:
        print(f"Attempting to set speed to {speed} km/h...")
        shuttle.set_speed(speed)
        # Show the speed after every attempt, including rejected changes.
        print(f"Current Speed: {shuttle.get_speed()} km/h\n")