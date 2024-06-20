import os
import shutil
import uuid

def encontrar_pastas_com_arquivos(caminho):
    pastas_com_arquivos = []

    def verificar_pasta(pasta):
        contem_arquivos = False
        subpastas_vazias = True
        for item in os.listdir(pasta):
            item_caminho = os.path.join(pasta, item)
            if os.path.isfile(item_caminho):
                contem_arquivos = True
            elif os.path.isdir(item_caminho):
                subpastas_vazias = False
                if verificar_pasta(item_caminho):
                    pastas_com_arquivos.append(item_caminho)
        return contem_arquivos or not subpastas_vazias

    verificar_pasta(caminho)
    
    return pastas_com_arquivos

def mover_pastas(diretorio_origem, diretorio_destino, pastas_para_mover):
    for pasta in pastas_para_mover:
        pathToMove = pasta.split("/")[-1]
        destino_final = os.path.join(diretorio_destino, pathToMove)
        # Gera um identificador único se a pasta já existir no destino
        if os.path.exists(destino_final):
            novoNome = f"{pasta}_{uuid.uuid4()}"
            print(f"arquivo existe, renomeando {novoNome}")
            os.rename(pasta, novoNome)
            pasta = novoNome
        
        # Cria o caminho de destino se não existir
        #if not os.path.exists(os.path.dirname(destino_final)):
        #    os.makedirs(os.path.dirname(destino_final))
        
        shutil.move(pasta, diretorio_destino)
        print(f"Movido: {pasta} para {diretorio_destino}")
        # Move a pasta

# Define o diretório de origem e de destino
diretorio_origem = r"E:\www\Projects\so-vits-svc"
diretorio_destino = r"E:\www\Projects\so-vits-svc\dataset_raw"

pastas_com_arquivos = encontrar_pastas_com_arquivos(diretorio_origem)
#print(pastas_com_arquivos)
# Move as pastas que contêm arquivos para o diretório de destino
mover_pastas(diretorio_origem, diretorio_destino, pastas_com_arquivos)