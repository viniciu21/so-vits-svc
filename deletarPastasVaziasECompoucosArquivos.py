from pydub import AudioSegment
import os
import shutil

def remove_empty_directories(path):
    # Remove diretórios vazios recursivamente
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path, topdown=False):
            print(dirpath, dirnames, filenames)
            if not dirnames and not filenames:
                os.rmdir(dirpath)
                print(f"Removido diretório vazio: {dirpath}")
            if len(filenames) < 100 and len(filenames) > 0: 
                shutil.rmtree(dirpath)
                print(f"Removido diretório por poucos arquivos: {dirpath}")
diretorio_destino = r"/home/viniods/www/Projects/so-vits-svc/dataset_raw"

                
remove_empty_directories(diretorio_destino)