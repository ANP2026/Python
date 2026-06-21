class ArtGallery:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.art = []
    def add_art(self, art):
        self.art.append(art)
        print(f"'{art}' has been added to the gallery")
    def remove_art(self, art):
        if art in self.art:
            self.art.remove(art)
            print(f"'{art}' has been removed from the gallery")
        else:
            print(f"'{art}' was not found in the gallery")
    def display_art(self):
        print(self.art)
    def __del__(self):
        print("Closing the gallery")
gallery = ArtGallery("Local Art Gallery", "New Jersey")
while True:
    print("\n1. Add art \n2. Remove art \n3. View art \n4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the artwork name to add: ")
        gallery.add_art(name)

    elif choice == "2":
        nanme = input("Enter the artwork name to remove: ")
        gallery.remove_art(name)

    elif choice == "3":
        gallery.display_art()

    elif choice == "4":
        print("Exiting the Art Gallery Collection .")

        # Object Lifecycle: object deletion
        del gallery
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
