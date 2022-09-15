'''
Editor de video

'''

import shutil
from pathlib import Path
import os
import ffmpeg


def trim(in_file ,out_file, start, end):
    """ Funcion encargada de recortar video"""
    if os.path.exists(out_file):
        os.remove(out_file)

    input_stream = ffmpeg.input(in_file)

    pts = "PTS-STARTPTS"
    video = input_stream.trim(start = start,end = end).setpts(pts)
    audio = (input_stream
            .filter_("atrim", start = start, end = end)
            .filter_("asetpts",pts))  
    video_and_audio = ffmpeg.concat(video, audio, v=1, a=1)
    output = ffmpeg.output(video_and_audio, out_file, format='mp4')
    output.run()   
    shutil.move(out_file,get_path())    #Mueve el video a la carpeta con el archivo base 


def convert(in_file):
    """Convertidor de video"""   
    ffmpeg.input(in_file).output('hola.mp4').run()


def get_path():
    """ Funcion encargada de devolver path de nuestros archivos"""
    path = Path("D:\\Ingenieria en Computacion\\Proyectos personales\\Convertidor de Video\\Recortar video\\Videos")
    return path


def get_input(path):
    """Funcion que se encarga de devolver path del archivo de entrada y nombre del de salida"""
    ext = '.mkv'
    for file in os.listdir(path):
        if file.endswith(ext): 
            file_name = Path(file).stem      #tomamos el nombre del archivo sin extension
            return path.joinpath(file), file_name + '_out' + ext
    return

if __name__ == '__main__':

    in_name, out_name= get_input(get_path())
    start = int(input("Ingrese en que segundo empezara el video: "))
    end_trim = int(input("Ingrese en que segundo terminara el video: "))
    trim(in_name,out_name,start,end_trim)
