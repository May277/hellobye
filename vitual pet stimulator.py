import time

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        print(f"{self.name} enjoyed the meal!")

    def play(self):
        self.happiness += 10
        self.hunger += 5
        print(f"{self.name} had fun playing!")

    def rest(self):
        self.hunger += 5
        self.happiness -= 5
        print(f"{self.name} is resting...")

    def status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}\n")

# --- Game Loop ---
pet_name = input("Name your virtual pet: ")
pet = VirtualPet(pet_name)

while True:
    pet.status()
    action = input("What do you want to do? (feed/play/rest/quit): ").lower()

    if action == "feed":
        pet.feed()
    elif action == "play":
        pet.play()
    elif action == "rest":
        pet.rest()
    elif action == "quit":
        print(f"Goodbye! {pet.name} will miss you.")
        break
    else:
        print("Invalid choice. Try again.")

    time.sleep(1)