import os
import subprocess

def main():

    ACOUSTIC_DIR = '/home/shota/Projects/acoustics_analysis-with-hikaru-utada/acousitics_src'

    ALBUM_NAME = 'Fantome'
    MUSIC_NAME  = 'oreno-kanojyo'
    WAV_EXT = 'wav'
    music_file_name = MUSIC_NAME + '.' + WAV_EXT
    music_file_path = os.path.join(ACOUSTIC_DIR, ALBUM_NAME, music_file_name)

    cliped_music_file_name = 'orenihayumeganai' + '.' + WAV_EXT

    out_path = os.path.join(ACOUSTIC_DIR, ALBUM_NAME, 'CLIPPED', cliped_music_file_name)

    start = 192
    end = 204
    duration = end - start
    # out_path = '/home/shota/Projects/acoustics_analysis-with-hikaru-utada/acousitics_src/CLIPPED/orenihayumeganai.wav'
    command = f'ffmpeg -i "{music_file_path}" -ss {start} -t {duration} {out_path}'
    print(f'command: {command}')
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    main()