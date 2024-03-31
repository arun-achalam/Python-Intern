import os
import pygame
from tkinter import Tk, filedialog

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 50))
        pygame.display.set_caption("Music Player")
        self.clock = pygame.time.Clock()
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.load_music()

    def load_music(self):
        root = Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        if folder_path:
            for file in os.listdir(folder_path):
                if file.endswith(".mp3"):
                    self.playlist.append(os.path.join(folder_path, file))
            if self.playlist:
                pygame.mixer.music.load(self.playlist[self.current_index])

    def play(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            self.is_playing = True

    def pause(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_song(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.current_index])
        self.play()

    def prev_song(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        pygame.mixer.music.load(self.playlist[self.current_index])
        self.play()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pause()
                    elif event.key == pygame.K_s:
                        self.stop()
                    elif event.key == pygame.K_n:
                        self.next_song()
                    elif event.key == pygame.K_p:
                        self.prev_song()

            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()

