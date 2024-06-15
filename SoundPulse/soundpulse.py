import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("SoundPulse")
        self.root.geometry("500x500")

        mixer.init()

        self.current_song = None

        self.label = tk.Label(self.root, text="No song loaded", width=35)
        self.label.pack(pady=10)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_song)
        self.load_button.pack(pady=5)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song, state=tk.DISABLED)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_song, state=tk.DISABLED)
        self.pause_button.pack(pady=5)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_song, state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.volume_label = tk.Label(self.root, text="Volume")
        self.volume_label.pack(pady=10)

        self.volume_scale = tk.Scale(self.root, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(50)  # Set initial volume to 50%
        self.volume_scale.pack(pady=10)
        
        self.made_by_label = tk.Label(self.root, text="Made by SkywalkerPZ", font=("Helvetica", 10))
        self.made_by_label.pack(side=tk.BOTTOM, pady=10)





    def load_song(self):
        self.current_song = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if self.current_song:
            song_name = os.path.basename(self.current_song)
            self.label.config(text=song_name)
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)

    def play_song(self):
        mixer.music.load(self.current_song)
        mixer.music.play()
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

    def pause_song(self):
        if mixer.music.get_busy():
            mixer.music.pause()
            self.pause_button.config(text="Resume", command=self.resume_song)
        else:
            mixer.music.unpause()
            self.pause_button.config(text="Pause", command=self.pause_song)

    def stop_song(self):
        mixer.music.stop()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED, text="Pause")

    def set_volume(self, val):
        volume = int(val) / 100 
        mixer.music.set_volume(volume)


    def resume_song(self):
        mixer.music.unpause()
        self.pause_button.config(text="Pause", command=self.pause_song)

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()