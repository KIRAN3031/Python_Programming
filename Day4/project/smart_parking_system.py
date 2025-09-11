from abc import ABC, abstractmethod

# Task 1: Base and derived vehicle classes with encapsulation
class Vehicle:
    def __init__(self, vehicle_id, license_plate, owner_name):
        self.vehicle_id = vehicle_id
        self.__license_plate = license_plate  # private
        self.__owner_name = owner_name        # private

    # Getters and setters
    def get_license_plate(self):
        return self.__license_plate

    def set_license_plate(self, plate):
        self.__license_plate = plate

    def get_owner_name(self):
        return self.__owner_name

    def set_owner_name(self, owner):
        self.__owner_name = owner

    def display(self):
        print(f"Vehicle ID: {self.vehicle_id}, Plate: {self.__license_plate}, Owner: {self.__owner_name}")

    def calculate_parking_fee(self, hours):
        return 0

class Bike(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, helmet_required):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.helmet_required = helmet_required

    def display(self):
        print(f"Bike → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Helmet Required: {self.helmet_required}")

    def calculate_parking_fee(self, hours):
        return 20 * hours

class Car(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, seats):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.seats = seats

    def display(self):
        print(f"Car → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Seats: {self.seats}")

    def calculate_parking_fee(self, hours):
        return 50 * hours

class SUV(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, four_wheel_drive):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.four_wheel_drive = four_wheel_drive

    def display(self):
        print(f"SUV → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, 4WD: {self.four_wheel_drive}")

    def calculate_parking_fee(self, hours):
        return 70 * hours

class Truck(Vehicle):
    def __init__(self, vehicle_id, license_plate, owner_name, max_load_capacity):
        super().__init__(vehicle_id, license_plate, owner_name)
        self.max_load_capacity = max_load_capacity

    def display(self):
        print(f"Truck → ID: {self.vehicle_id}, Plate: {self.get_license_plate()}, Owner: {self.get_owner_name()}, Max Load: {self.max_load_capacity} tons")

    def calculate_parking_fee(self, hours):
        return 100 * hours

# Task 2: ParkingSpot class with encapsulation and size restrictions
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id
        self.size = size                # S, M, L, XL
        self.__status = "Empty"       # private
        self.__assigned_vehicle = None # private

    def get_status(self):
        return self.__status

    def get_assigned_vehicle(self):
        return self.__assigned_vehicle

    def assign_vehicle(self, vehicle):
        # Check spot size vs vehicle type
        if self.__assigned_vehicle is not None:
            print(f"Spot {self.spot_id} already occupied.")
            return False

        v_type = type(vehicle).__name__
        valid = False
        if v_type == "Bike" and self.size in ["S", "M", "L", "XL"]:
            valid = True
        elif v_type == "Car" and self.size in ["M", "L", "XL"]:
            valid = True
        elif v_type == "SUV" and self.size in ["L", "XL"]:
            valid = True
        elif v_type == "Truck" and self.size == "XL":
            valid = True

        if not valid:
            print(f"{v_type} cannot park in spot size {self.size} (Spot {self.spot_id}).")
            return False

        self.__assigned_vehicle = vehicle
        self.__status = "Occupied"
        print(f"{v_type} (Plate: {vehicle.get_license_plate()}) assigned to Spot {self.spot_id} ({self.size}).")
        return True

    def remove_vehicle(self):
        if self.__assigned_vehicle is None:
            print(f"Spot {self.spot_id} is already empty.")
            return None
        vehicle = self.__assigned_vehicle
        self.__assigned_vehicle = None
        self.__status = "Empty"
        print(f"Vehicle (Plate: {vehicle.get_license_plate()}) removed from Spot {self.spot_id}.")
        return vehicle

    def display_spot(self):
        if self.__status == "Occupied":
            v = self.__assigned_vehicle
            v_type = type(v).__name__
            print(f"Spot {self.spot_id} ({self.size}): Occupied → {v_type} ({v.get_license_plate()})")
        else:
            print(f"Spot {self.spot_id} ({self.size}): Empty")

# Task 3: ParkingLot class
class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)
        print(f"Spot {spot.spot_id} (Size {spot.size}) added to Parking Lot {self.name}.")

    def show_spots(self):
        print("Parking Status:")
        for spot in self.spots:
            spot.display_spot()

    def park_vehicle(self, vehicle):
        for spot in self.spots:
            if spot.get_status() == "Empty" and spot.assign_vehicle(vehicle):
                print(f"Parked vehicle {vehicle.get_license_plate()} in spot {spot.spot_id}.")
                return True
        print(f"No suitable spot available for vehicle {vehicle.get_license_plate()}.")
        return False

    def unpark_vehicle(self, vehicle, hours):
        for spot in self.spots:
            assigned_vehicle = spot.get_assigned_vehicle()
            if assigned_vehicle is not None and assigned_vehicle.get_license_plate() == vehicle.get_license_plate():
                # Remove vehicle, calculate fee
                spot.remove_vehicle()
                fee = vehicle.calculate_parking_fee(hours)
                print(f"Parking Fee = ₹{fee}")
                # Payment to be processed
                self.process_payment(fee)
                return fee
        print(f"Vehicle not found in any spot: {vehicle.get_license_plate()}")
        return None

    def process_payment(self, amount):
        print("Select Payment Method: 1. Cash 2. Card 3. UPI")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            payment = CashPayment()
        elif choice == '2':
            payment = CardPayment()
        elif choice == '3':
            payment = UPIPayment()
        else:
            print("Invalid choice. Defaulting to Cash Payment.")
            payment = CashPayment()
        payment.process_payment(amount)

# Task 4: Abstract Payment class and its children
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Cash")

class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} using Card")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount} via UPI")


# Task 5: Main program demonstration
if __name__ == "__main__":
    # Create Parking Lot and Spots
    lot = ParkingLot("CityMall Parking")
    lot.add_spot(ParkingSpot(1, "S"))
    lot.add_spot(ParkingSpot(2, "M"))
    lot.add_spot(ParkingSpot(3, "M"))
    lot.add_spot(ParkingSpot(4, "L"))
    lot.add_spot(ParkingSpot(5, "XL"))
    print(f"Parking Lot Created: {lot.name} Total Spots Added: {len(lot.spots)}\n")

    # Create Vehicles
    bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
    car1 = Car("C201", "TS05CD5678", "Priya", 5)
    suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
    truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)

    print("Vehicles Created:")
    bike1.display()
    car1.display()
    suv1.display()
    truck1.display()
    print()

    # Park Vehicles
    lot.park_vehicle(bike1)   # Should go to Spot 1 (S)
    lot.park_vehicle(car1)    # Should go to Spot 2 (M)
    lot.park_vehicle(suv1)    # Should go to Spot 4 (L)
    lot.park_vehicle(truck1)  # Should go to Spot 5 (XL)
    lot.show_spots()
    print()

    # Unpark a Vehicle + Payment
    lot.unpark_vehicle(car1, hours=3)  # Car stayed 3 hours
    print()

    # Final Status
    lot.show_spots()
