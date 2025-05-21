import random
songs_duration = []
training_duration_mins = int(input("Enter the duration of your training session in minutes: "))
training_duration_secs = training_duration_mins * 60
training_duration = training_duration_secs
song_duration = int(input("Enter the duration of the song in seconds: "))
songs_duration.append(song_duration)
total_song_duration = sum(songs_duration)

while total_song_duration < training_duration:
    print("You can add another song.")
    print("You currently have", total_song_duration, "seconds of songs.")
    song_duration = int(input("Enter the duration of the song in minutes: "))
    songs_duration.append(song_duration)
    total_song_duration = sum(songs_duration)
print("The total duration of the songs is:", total_song_duration, "minutes.")

while total_song_duration > training_duration:
    print("You cannot add another song.")
    print("The total duration of the songs is:", total_song_duration, "minutes.")
    song_to_remove = int(input("Enter the duration of the song you want to remove: "))
    songs_duration.remove(song_to_remove)
    total_song_duration = sum(songs_duration)
    print("Song removed. Current total duration:", total_song_duration, "minutes.")
print("The total duration of the songs is:", total_song_duration, "minutes.")

fog_machine = input("Do you want to use a fog machine? (yes/no): ")
if fog_machine == "yes":
    print("Fog machine is on.")
random.choice (songs_duration)
print("The song is:", random.choice(songs_duration), "seconds.")

if fog_machine == "no":
    print("Fog machine is off.")


