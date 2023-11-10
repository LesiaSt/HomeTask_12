class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.current_time = 0
        self.playing = False
        self.quality = "HD"

    def play(self,video_link,list):
        if video_link in self.list:
            print(f"Playing {self.name}")
            self.playing = True
        else:
            print(f"There is no {self.name} in link:{self.video_link}")
    def pause(self):
        if self.playing:
            print(f'Pause the {self.name} on {self.current_time}')
            self.playing = False
        else:
            print(f"{self.name} isn't currently playing")

    def change_quality(self,new_quality):
        if new_quality in ["HD","4K","SD"]:
            print(f"Change quality {self.name} from {self.quality} to {new_quality}")
            self.quality=new_quality
        else:
            print("Invalid quality")
youtube_player = Player("Youtube","https://www.youtube.com/watch?v=qI4suIO1qhk",200)
youtube_player.change_quality("HD")
