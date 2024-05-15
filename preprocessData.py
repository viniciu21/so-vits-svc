from pydub import AudioSegment
import os

def split_audio(input_file, output_folder, chunk_length_ms=10000):
    # Carrega o arquivo de áudio
    audio = AudioSegment.from_wav(input_file)
    # Calcula o número total de pedaços
    num_chunks = len(audio) // chunk_length_ms
    
    # Cria o diretório de saída, se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    print(file_name)
    # Se houver um restante, adiciona mais um chunk para incluir o restante
    if len(audio) % chunk_length_ms != 0:
        num_chunks += 1

    print(num_chunks)

    # Corta e salva cada pedaço
    for i in range(num_chunks):
        start_time = i * chunk_length_ms
        end_time = (i + 1) * chunk_length_ms
        chunk = audio[start_time:end_time]
        chunk.export(os.path.join(output_folder, f"{file_name}_{i}.wav"), format="wav")


def process_folder(input_folder, output_folder):
    # Percorre todos os arquivos na pasta de entrada
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".wav"):  # Verifica se o arquivo é um arquivo .wav
            input_file_path = os.path.join(input_folder, file_name)
            # Chama a função split_audio para dividir o arquivo de áudio
            split_audio(input_file_path, output_folder)

# Função para processar todos os arquivos .wav em uma pasta e subpastas
def process_folder_recursive(input_folder, output_folder):
    # Percorre todos os itens (pastas e arquivos) na pasta de entrada
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        output_item_path = os.path.join(output_folder, item)
        if os.path.isdir(item_path):  # Verifica se é uma pasta
            # Se for uma pasta, cria a pasta correspondente na pasta de saída
            if not os.path.exists(output_item_path):
                os.makedirs(output_item_path)
            # Chama recursivamente a função para processar esta subpasta
            process_folder_recursive(item_path, output_item_path)
        elif item.endswith(".wav"):  # Se for um arquivo .wav
            # Chama a função split_audio para dividir o arquivo de áudio
            split_audio(item_path, output_folder)

# Exemplo de uso
input_folder = r"/Users/viniciusoliveira/Downloads/cml_tts_dataset_portuguese_v0.2/train/audio"
output_folder = r"/Users/viniciusoliveira/www/Projects/so-vits-svc/sliced_wavs"
process_folder_recursive(input_folder, output_folder)