class CampusShuttle:
    def __init__(self, registration_number: str, initial_speed: float = 0.0):
        self.registration_number = registration_number 
        self.__speed = 0.0 
        
        self.set_speed(initial_speed)

    def get_speed(self) -> float:
        return self.__speed

    def set_speed(self, new_speed: float) -> None:
        if 0 <= new_speed <= 80:
            self.__speed = new_speed
        else:
            print(f"--> Rejection: {new_speed} km/h is invalid! (Allowed range: 0 - 80 km/h)")


if __name__ == "__main__":
    shuttle = CampusShuttle("UAG 979J", 40)
    print(f"Shuttle '{shuttle.registration_number}' created.")
    print(f"Initial Speed: {shuttle.get_speed()} km/h\n")

    print("--- Test 1: Setting speed to 60 km/h ---")
    shuttle.set_speed(60)
    print(f"Current Speed: {shuttle.get_speed()} km/h\n")

    print("--- Test 2: Setting speed to 100 km/h ---")
    shuttle.set_speed(100)
    print(f"Current Speed: {shuttle.get_speed()} km/h\n")

    print("--- Test 3: Setting speed to -20 km/h ---")
    shuttle.set_speed(-20)
    print(f"Current Speed: {shuttle.get_speed()} km/h")