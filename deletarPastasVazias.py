from pydub import AudioSegment
import os
import shutil
import numpy

numberOfFilesPerFOlder = []

def remove_empty_directories(path):
    # Remove diretórios vazios recursivamente
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path, topdown=False):
            #if not dirnames and not filenames:
                #os.rmdir(dirpath)
            numberOfFilesPerFOlder.append(len(filenames))
            #print(f"diretorio: {dirpath} contem {len(filenames)}")
                
diretorio_destino = r"/home/viniods/www/Projects/so-vits-svc/dataset/44k"

                
remove_empty_directories(diretorio_destino)

print(numpy.array(numberOfFilesPerFOlder))