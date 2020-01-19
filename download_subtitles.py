import argparse
import os
from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File


__author__ = "Hariom"

# Credentials
USERNAME = "XXXXXX"
PASSWORD = "XXXXXX"


# Video extensions
VIDEO_EXTENSIONS = ["mp4", "mkv", "3gp", "mpeg"]

# Argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--file",
                    default=None,
                    help="Pass the full path of the file whose subtitles you want to download")
parser.add_argument("--folder",
                    default=None,
                    help="Pass the full path of the folder whose subtitles you want to download")
args = parser.parse_args()


def download_file(ost_connection, download_file_path):
    file_extension = download_file_path.split('.')[-1]
    if file_extension not in VIDEO_EXTENSIONS:
        raise TypeError("Passed path -> %s is not a video file" % download_file_path)

    if not file_extension == "srt":
        _file = File(download_file_path)
        data  = ost_connection.search_subtitles(
            [
                {
                    'sublanguageid': 'en',
                    'moviehash'    : _file.get_hash(),
                    'moviebytesize': _file.size
                }
            ])

        id_subtitle_file = data[0].get('IDSubtitleFile')

        file_name  = download_file_path.split('/')[-1]
        output_dir = download_file_path.replace(file_name, '')

        ost_connection.download_subtitles([id_subtitle_file],
                                          output_directory=output_dir,
                                          extension='srt')
        downloaded_subtitle_path    = output_dir + "%s.srt" % id_subtitle_file

        new_file_name               = downloaded_subtitle_path.replace(str(id_subtitle_file),
                                                                       file_name.replace(".%s" % file_extension, ''))
        os.rename(downloaded_subtitle_path, new_file_name)
    else:
        pass


if __name__ == '__main__':
    # Login - make a connection with open-subtitles
    ost = OpenSubtitles()
    ost.login(USERNAME, PASSWORD)

    file_path   = args.file
    folder_path = args.folder

    if (file_path is None and folder_path is None) or (file_path is not None and folder_path is not None):
        raise AttributeError("Please pass either file path or folder path")

    passed_file   = False
    passed_folder = False

    if file_path:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Path -> %s doesn't exists" % file_path)
        passed_file = True

    if folder_path:
        if not os.path.isdir(folder_path):
            raise NotADirectoryError("Path -> %s doesn't exists" % folder_path)
        passed_folder = True

    if passed_file:
        download_file(ost_connection=ost, download_file_path=file_path)

    else:
        file_list = os.listdir(folder_path)

        for file in file_list:
            try:
                if not folder_path.endswith('/'):
                    folder_path += '/'

                full_file_path = folder_path + file
                download_file(ost_connection=ost, download_file_path=full_file_path)
            except TypeError as error:
                print(error)
                continue
