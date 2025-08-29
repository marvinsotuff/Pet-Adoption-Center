from db import initialize_db
from models.shelter import Shelter
from models.pet import Pet

def shelter_menu():
    while True:
        print("\n--- Shelter Menu ---")
        print("1. Add Shelter")
        print("2. View All Shelters")
        print("3. Find Shelter by ID")
        print("4. Delete Shelter")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter shelter name: ")
            location = input("Enter shelter location: ")
            Shelter.create(name, location)
            print(" Shelter added successfully!")

        elif choice == "2":
            shelters = Shelter.get_all()
            if shelters:
                for s in shelters:
                    print(f"ID: {s[0]} | Name: {s[1]} | Location: {s[2]}")
            else:
                print(" No shelters found.")

        elif choice == "3":
            try:
                shelter_id = int(input("Enter shelter ID: "))
                shelter = Shelter.find_by_id(shelter_id)
                if shelter:
                    print(f" Found Shelter: ID={shelter[0]}, Name={shelter[1]}, Location={shelter[2]}")
                    pets = Pet.get_by_shelter(shelter_id)
                    if pets:
                        print("   Pets in this shelter:")
                        for p in pets:
                            print(f"   - {p[1]} ({p[2]}, {p[3]} years old)")
                    else:
                        print("   No pets in this shelter.")
                else:
                    print(" Shelter not found.")
            except ValueError:
                print(" Invalid input. Please enter a valid ID.")

        elif choice == "4":
            try:
                shelter_id = int(input("Enter shelter ID to delete: "))
                Shelter.delete(shelter_id)
                print(" Shelter deleted (and pets removed).")
            except ValueError:
                print(" Invalid input.")

        elif choice == "5":
            break
        else:
            print(" Invalid choice, try again.")


def pet_menu():
    while True:
        print("\n--- Pet Menu ---")
        print("1. Add Pet")
        print("2. View All Pets")
        print("3. Find Pet by ID")
        print("4. Delete Pet")
        print("5. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter species: ")
            try:
                age = int(input("Enter age: "))
                shelter_id = int(input("Enter shelter ID: "))
                Pet.create(name, species, age, shelter_id)
                print(" Pet added successfully!")
            except ValueError:
                print(" Invalid input. Age and Shelter ID must be numbers.")

        elif choice == "2":
            pets = Pet.get_all()
            if pets:
                for p in pets:
                    print(f"ID: {p[0]} | Name: {p[1]} | Species: {p[2]} | Age: {p[3]} | Shelter ID: {p[4]}")
            else:
                print(" No pets found.")

        elif choice == "3":
            try:
                pet_id = int(input("Enter pet ID: "))
                pet = Pet.find_by_id(pet_id)
                if pet:
                    print(f"Found Pet: ID={pet[0]}, Name={pet[1]}, Species={pet[2]}, Age={pet[3]}, Shelter ID={pet[4]}")
                else:
                    print(" Pet not found.")
            except ValueError:
                print(" Invalid input.")

        elif choice == "4":
            try:
                pet_id = int(input("Enter pet ID to delete: "))
                Pet.delete(pet_id)
                print(" Pet deleted.")
            except ValueError:
                print(" Invalid input.")

        elif choice == "5":
            break
        else:
            print(" Invalid choice, try again.")


def main_menu():
    initialize_db()  # ensure database & tables exist
    while True:
        print("\n=== Pet Adoption Center ===")
        print("1. Manage Shelters")
        print("2. Manage Pets")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            shelter_menu()
        elif choice == "2":
            pet_menu()
        elif choice == "3":
            print(" Goodbye!")
            break
        else:
            print(" Invalid choice, try again.")


if __name__ == "__main__":
    main_menu()


