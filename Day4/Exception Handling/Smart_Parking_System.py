class Vehicle:
    def __init__(self, license_plate, owner_name):
        self.__license_plate = license_plate  # private attribute
        self.__owner_name = owner_name        # private attribute

    # Getter and Setter for license_plate
    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, license_plate):
        self.__license_plate = license_plate

    # Getter and Setter for owner_name
    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, owner_name):
        self.__owner_name = owner_name

    def display(self):
        print(f"Vehicle License Plate: {self.__license_plate}")
        print(f"Owner: {self.__owner_name}")

    def calculate_parking_fee(self, hours):
        raise NotImplementedError("This method should be overridden in child classes")


class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, helmet_required):
        super().__init__(license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print("Bike Details:")
        super().display()
        print(f"Helmet Required: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours


class Car(Vehicle):
    def __init__(self, license_plate, owner_name, seats):
        super().__init__(license_plate, owner_name)
        self.seats = seats

    def display(self):
        print("Car Details:")
        super().display()
        print(f"Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours


class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, four_wheel_drive):
        super().__init__(license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print("SUV Details:")
        super().display()
        print(f"Four Wheel Drive: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours


class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, max_load_capacity):
        super().__init__(license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print("Truck Details:")
        print(f"License Plate: {self.get_license_plate()}")
        print(f"Owner: {self.get_owner_name()}")
        print(f"Max Load Capacity: {self.max_load_capacity}")

    def calculate_parking_fee(self, hours):
        return 100 * hours


class ParkingSpot:
    def __init__(self, spot_id, status="free"):
        self.__spot_id = spot_id        # private attribute
        self.__status = status          # private attribute like "free" or "occupied"

    def get_spot_id(self):
        return self.__spot_id

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status


class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def display_spots(self):
        print(f"Parking Lot: {self.name}")
        for spot in self.spots:
            print(f"Spot ID: {spot.get_spot_id()}, Status: {spot.get_status()}")


# Demonstration:
bike = Bike("BIKE123", "Alice", True)
car = Car("CAR456", "Bob", 4)
suv = SUV("SUV789", "Charlie", True)
truck = Truck("TRK012", "Dave", 10000)

vehicles = [bike, car, suv, truck]

# Trying to access private attribute directly (will fail)
# print(bike.__license_plate)  # AttributeError

# Accessing via getter works
print(bike.get_license_plate())

# Display each vehicle details and fee calculation demo
for vehicle in vehicles:
    vehicle.display()
    fee = vehicle.calculate_parking_fee(3)  # example 3 hours
    print(f"Parking fee for 3 hours: {fee}\n")

# Create parking spots and lot
spot1 = ParkingSpot("S1")
spot2 = ParkingSpot("S2", "occupied")

lot = ParkingLot("City Center Parking")
lot.add_spot(spot1)
lot.add_spot(spot2)
lot.display_spots()


