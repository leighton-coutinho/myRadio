from pydub import AudioSegment
import os

def get_time(file):
    return (file.frame_count()/file.frame_rate) *1000

Pop_tracks =[]
RnB_tracks =[]
Country_tracks =[]
News_tracks =[]
Jokes_tracks = []
Voice_tracks = []
Riddles_tracks = []

i = 1
def toAudioSegment(genre):
    global i
    for filename in os.listdir(genre):
        globals()[f"track_{i}"] = AudioSegment.from_mp3(f"{genre}/{filename}") + AudioSegment.silent(2000)
        eval(f"{genre}_tracks").append(eval(f"track_{i}"))
        i+=1

toAudioSegment("Pop")
toAudioSegment("RnB")
toAudioSegment("Country")
toAudioSegment("News")

period = {"Pop" : Pop_tracks, "RnB" : RnB_tracks, "Country" : Country_tracks, "News" : News_tracks}

toAudioSegment("Jokes")
toAudioSegment("Voice")
toAudioSegment("Riddles")

frequent = {"Jokes" : Jokes_tracks, "Voice" : Voice_tracks, "Riddles" : Riddles_tracks}


