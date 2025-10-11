songs = input("Введіть назви пісень через крапку з комою")
songs_list = songs.split(';')
print(songs_list)
with open("playlist.txt", mode= 'a', encoding='utf-8') as file:
    for song in songs_list:
        file.write(f"{song.title()}\n")
with open("playlist.txt", mode= 'r') as file:
    file_content = file.read()
    print(file_content)