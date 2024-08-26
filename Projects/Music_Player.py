import pygame
import os
import threading
import time
import tkinter as tk
from tkinter import ttk
from tabulate import tabulate

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

class MusicPlayerGUI:
    def __init__(self, playlist):
        self.playlist = playlist
        self.root = tk.Tk()
        self.root.title("RONYS MUSIC PLAYER")
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", background="#add8e6")  # Light blue background for buttons
        self.create_widgets()

    def create_widgets(self):
        # Playlist display
        self.playlist_label = ttk.Label(self.root, text="Current Playlist:")
        self.playlist_label.grid(row=0, column=0, columnspan=3, pady=5)

        self.playlist_tree = ttk.Treeview(self.root, columns=("Song Title", "Status"), show="headings", height=5)
        self.playlist_tree.heading("Song Title", text="Song Title")
        self.playlist_tree.heading("Status", text="Status")
        self.playlist_tree.grid(row=1, column=0, columnspan=3, pady=5)

        # Control buttons
        # Previous button: Returns to the previous song in the playlist and plays it
        self.prev_button = ttk.Button(self.root, text="Previous", command=self.playlist.play_prev_song)
        self.prev_button.grid(row=2, column=0, pady=5)

        # Play button: Initiates playback of the currently selected song (centered)
        self.play_button = ttk.Button(self.root, text="Play", command=self.playlist.play_current_song)
        self.play_button.grid(row=2, column=1, pady=5)

        # Next button: Skips to the next song in the playlist and plays it
        self.next_button = ttk.Button(self.root, text="Next", command=self.playlist.play_next_song)
        self.next_button.grid(row=2, column=2, pady=5)

        # Pause button: Pauses the currently playing song
        self.pause_button = ttk.Button(self.root, text="Pause", command=self.playlist.pause_song)
        self.pause_button.grid(row=3, column=0, pady=5)

        # Display button: Updates and displays the current playlist in the GUI
        self.display_button = ttk.Button(self.root, text="Display Playlist", command=self.update_playlist_display)
        self.display_button.grid(row=3, column=1, pady=5)

        # Exit button: Exits the music player application
        self.exit_button = ttk.Button(self.root, text="Exit", command=self.exit_application)
        self.exit_button.grid(row=3, column=2, pady=5)

        # Configure column weights to center the Play button
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        self.root.grid_columnconfigure(2, weight=1)

        # Update the playlist display initially
        self.update_playlist_display()

    def update_playlist_display(self):
        # Clear previous items in the treeview
        for item in self.playlist_tree.get_children():
            self.playlist_tree.delete(item)

        # Insert current playlist data into the treeview
        for current in self.playlist:
            status = "Playing" if current == self.playlist.current_song else ""
            self.playlist_tree.insert("", "end", values=(current.title, status))

    def exit_application(self):
        print("Exiting the playlist.")
        if self.playlist.playback_thread and self.playlist.playback_thread.is_alive():
            pygame.mixer.music.stop()
            self.playlist.playback_thread.join()
        self.root.destroy()

    def run(self):
        # Start the GUI main loop
        self.root.mainloop()

if __name__ == "__main__":
    # Initialize pygame mixer
    pygame.mixer.init()

    # Create an instance of the Playlist class
    playlist = Playlist()

    # Add songs to the playlist
    playlist.add_song("tere liye")
    playlist.add_song("kya muje")
    playlist.add_song("pehele bhi me")
    playlist.add_song("rang lageya")
    playlist.add_song("tere havale")

    # Create an instance of the MusicPlayerGUI class and run the GUI
    gui = MusicPlayerGUI(playlist)
    gui.run()
