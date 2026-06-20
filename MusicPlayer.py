class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.song = []
        print(f"Playlist '{self.name}'({self.genre}) is ready!")

    def add_song(self, song):
        self.song.append(song)
        print(f"{song} added to {self.name}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed")
        else:
            print(f"'{song}' not found in playlist")

    def display(self):
        print(f"\n -- {self.name} ({self.genre}) --")
        if self.songs:
            for i, song in enumerate(self.song, 1):
                print(f"{i}.{song}")
        else:
            print("No songs here. Add some!")

    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")

myPlaylist = Playlist("Road trip Mix", "Pop")
while True:
    print("\n1. Add song \n2. Remove song \n3. View Playlist \n4. Delete and Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        song = input("Enter song name: ")
        myPlaylist.add_song(song)
    elif choice == "2":
        song = input("Enter song to remove: ")
        myPlaylist.remove_song(song)
    elif choice == "3":
        myPlaylist.display()
    elif choice == "4":
        del myPlaylist
        break
    else:
        print("Invalid Choice. Please enter 1, 2, 3, or 4")