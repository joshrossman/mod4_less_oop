
#Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    def __init__(self, reg, type, owner):
        self.registration_number=reg
        self.type=type
        self.owner=owner

    def update_owner(self, new_owner):
        self.owner=new_owner
        print(f"Car with registration number {self.registration_number} has been updated. New owner is {new_owner}")
    
    def display_info(self):
        print(f"Registration number: {self.registration_number}\nVehicle Type: {self.type}\nOwner: {self.owner}\n")
    

vehicles=[]
def display_all_vehicles():
    for car in vehicles:
        car.display_info()

while True:
    my_choice=input("What would you like to do? [1]Register vehicle. [2] Change vehicle owner [3]Display all vehicles [4]Exit")
    if my_choice=="1":
        registration_number=input("What is the registration number?")
        type = input("What is the vehicle type")
        owner=input("What is the name of the owner?")
        can_update=True
        for car in vehicles:
            if car.registration_number==registration_number:
                print("Registration number already in use. Could not add new vehicle.")   
                can_update=False 
        if can_update:
            vehicles.append(Vehicle(registration_number,type,owner))
    elif my_choice=="2":
        registration_number=input("What is the car's registration number?")
        new_owner=input("What is the new owner's name?")
        car_updated=False
        for car in vehicles:
            if car.registration_number==registration_number:
                car.update_owner(new_owner)
                car_updated=True
        if not car_updated:
            print("Registration number not found. Was unable to update car owner.")
        
    elif my_choice=="3":
        display_all_vehicles()
    elif my_choice=="4":
        print("System closed! Have a great day!")
        break
    else:
        print("Not a valid input!")



