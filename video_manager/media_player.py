class MediaPlayer:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.current_time = 0
        self.playing = False
        self.quality = "HD"

    def play(self):
        if not self.playing:
            print(f"Playing {self.name} - {self.video_link}")
            self.playing = True
        else:
            print(f"{self.name} is already playing")
    def pause(self):
        if self.playing:
            print(f"Pausing {self.name} at {self.current_time} seconds")
            self.playing = False
        else:
            print(f"{self.name} is not currently playing")

    def save_last_time(self):
        if self.playing:
            print(f"Saving last played time for {self.name}: {self.current_time} seconds")
        else:
            print(f"{self.name} is not currently playing")

    def change_quality(self, new_quality):
        if new_quality in ["HD", "SD", "4K"]:
            print(f"Changing {self.name} quality from {self.quality} to {new_quality}")
            self.quality = new_quality
        else:
            print("Invalid quality option")

if __name__ == "__main__":
    my_media_player = MediaPlayer(name="Sample Video", video_link="example.com/video", duration=120)
    my_media_player.play()
    my_media_player.pause()
    my_media_player.save_last_time()
    my_media_player.change_quality("4K")