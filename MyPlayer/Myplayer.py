from moviepy.editor import VideoFileClip
from pydub import AudioSegment
import subprocess
import time
import os
import sys

# News Showing:
print('____________________________________________________')
print('Welcom to use MyPlayer by Jinwei Lin by YDOOK.COM')
print('Author ORCID: https://orcid.org/0000-0003-0558-6699')
print('====================================================')
print('Media Files List:')

dirs = os.listdir()
media_list = []

# search the files in now dir
for i in dirs:
    if i.endswith('.wav') or i.endswith('.mp3') or i.endswith('.wma') or i.endswith('.mp4') \
            or i.endswith('.flv') or i.endswith('.ogg') or i.endswith('.acc'):
        media_list.append(i)

# print the media files list
index = 0
for media in media_list:
    index += 1
    print(index, ' ', media)

print('====================================================')
print('Iuput [ok] to play on list:')
print('Press [P] Key to stop the playing:')
print('Iuput the [index] of one file to play it:')
print('Iuput [end] to exit:')
print('____________________________________________________\n')

option = input()


# get the type of the file
def get_endwith(file_name):
    if file_name.endswith('.wav'):
        return 'wav'
    elif file_name.endswith('.mp3'):
        return 'mp3'
    elif file_name.endswith('.wma'):
        return 'wma'
    elif file_name.endswith('.flv'):
        return 'flv'
    elif file_name.endswith('.ogg'):
        return 'ogg'
    elif file_name.endswith('.mp4'):
        return 'mp4'
    elif file_name.endswith('.aiff'):
        return 'acc'


# Function: Play the file
def playnow(i, t):
    # bind the key
    print('MyPlayer: lenght = ', int(t), 'seconds')
    for line in range(100):
        sys.stdout.write('_')
    print()

    # call th system player to play
    now_audio = subprocess.Popen(i, shell=True)

    # set buffer time /second
    buffer_time = 0
    seg_time = (t + buffer_time) / 100
    for i in range(100):
        time.sleep(seg_time)
        sys.stdout.write('>')
    now_audio.terminate()
    print()
    # print('now_audio = ', now_audio)


# Function: Play by the name and type
def play_by_name(file_name):
    if get_endwith(file_name) == 'wav':
        file_i = AudioSegment.from_wav(file_name)
        playnow(file_name, file_i.duration_seconds)

    elif get_endwith(file_name) == 'mp3':
        file_i = AudioSegment.from_mp3(file_name)
        playnow(file_name, file_i.duration_seconds)

    elif get_endwith(file_name) == 'flv':
        file_i = AudioSegment.from_flv(file_name)
        playnow(file_name, file_i.duration_seconds)

    elif get_endwith(file_name) == 'ogg':
        file_i = AudioSegment.from_ogg(file_name)
        playnow(file_name, file_i.duration_seconds)

    elif get_endwith(file_name) == 'mp4':
        file = VideoFileClip(file_name)
        # print('file.duration = ', file.duration)
        playnow(file_name, file.duration)


    elif get_endwith(file_name) == 'wma':
        file_i = AudioSegment.from_file(file_name, format='wma')
        playnow(file_name, file_i.duration_seconds)

    elif get_endwith(file_name) == 'acc':
        file_i = AudioSegment.from_file(file_name, format='acc')
        playnow(file_name, file_i.duration_seconds)

    print()


# Main player function:
def Myplayer():
    # reset the option
    global option
    while option != 'end':
        # optinon 1
        if option == 'ok':
            print("MyPlayer: Playing on list...")
            print('________________________________________')
            for i in media_list:
                print("Playing: ", i)
                play_by_name(i)

        # optinon number
        elif option.isdigit():
            # get int type of the index number
            id_file = int(option)
            # if the id_file is available
            if id_file <= len(media_list):
                print('MyPlayer: Playing: NO.', id_file, ' ', media_list[id_file - 1])
                print('________________________________________')
                play_by_name(media_list[id_file - 1])

        print('Please input:')
        option = input()

    # optinon end
    if option == 'end':
        print('MyPlayer is exiting...')


# Run MyPlayer
Myplayer()
