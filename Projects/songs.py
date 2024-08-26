import pygame
import os
import threading
import time
from tabulate import tabulate
from colorama import init, Fore, Style  # Import colorama modules

class SongNode:
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None
        self.playback_thread = None

    def insert_at_tail(self, title):
        new_song = SongNode(title)
        if self.tail is None:
            self.head = self.tail = new_song
            self.current_song = new_song  # Set current_song for the first song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song

    def add_song(self, title):
        # Check if the song already exists in the playlist
        if any(node.title == title for node in self):
            print(f"{title}")
        else:
            # Add the new song to the end of the playlist
            self.insert_at_tail(title)
        
            if not self.current_song:
                self.current_song = self.head  # Set the current song if it's the first song in the list

    def display_playlist(self):
        print("\nCurrent Playlist:")
        song_list = [(current.title, "Playing" if current == self.current_song else "") for current in self]
        print(tabulate(song_list, headers=["Song Title", "Status"], tablefmt="grid"))

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def play_current_song(self):
        if self.current_song:
            file_path = os.path.abspath(os.path.join("C:\\Users\\Rohan\\Music\\my songs", f"{self.current_song.title}.mp3"))
            print(f"Playing: {file_path}")

            if self.playback_thread and self.playback_thread.is_alive():
                pygame.mixer.music.stop()
                self.playback_thread.join()

            self.playback_thread = threading.Thread(target=play_song, args=(file_path,))
            self.playback_thread.start()
        else:
            print("No current song selected.")

    def play_next_song(self):
        if self.current_song and self.current_song.next:
            self.current_song = self.current_song.next
            self.play_current_song()
        elif self.head:  # Play the first song if no next song
            self.current_song = self.head
            self.play_current_song()
        else:
            print("No next song in the playlist.")

    def play_prev_song(self):
        if self.current_song and self.current_song.prev:
            self.current_song = self.current_song.prev
            self.play_current_song()
        elif self.tail:  # Play the last song if no previous song
            self.current_song = self.tail
            self.play_current_song()
        else:
            print("No previous song in the playlist.")

    def pause_song(self):
        if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            print("Song paused.")
        else:
            print("No song is currently playing.")

def play_song(file_path):
    print(f"Now Playing: {os.path.splitext(os.path.basename(file_path))[0]}")

    pygame.mixer.init()
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait until the song is playing
            time.sleep(1)
    except pygame.error as e:
        print(f"Error: {e}")
    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    # Initialize pygame mixer
    pygame.mixer.init()

    # Initialize colorama
    init(autoreset=True)

    # Print the title in a box
    print(Fore.CYAN + Style.BRIGHT + "+-------------------------+")
    print("|   RONYS MUSIC PLAYER   |")
    print("+-------------------------+")


    playlist = Playlist()

    # Add songs to the playlist
    playlist.add_song("tere liye")
    playlist.add_song("kya muje")
    playlist.add_song("pehele bhi me")
    playlist.add_song("rang lageya")
    playlist.add_song("tere havale")

    while True:
        print("\nOptions:")
        print("1. Play current song")
        print("2. Play next song")
        print("3. Play previous song")
        print("4. Pause current song")
        print("5. Display playlist")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            playlist.play_current_song()
        elif choice == '2':
            playlist.play_next_song()
        elif choice == '3':
            playlist.play_prev_song()
        elif choice == '4':
            playlist.pause_song()
        elif choice == '5':
            playlist.display_playlist()
        elif choice == '6':
            print("Exiting the playlist.")
            if playlist.playback_thread and playlist.playback_thread.is_alive():
                pygame.mixer.music.stop()
                playlist.playback_thread.join()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
