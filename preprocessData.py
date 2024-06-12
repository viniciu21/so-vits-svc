from pydub import AudioSegment
import os

def split_audio(file_path, output_dir, chunk_length=10000, min_length=1000):
    # Carrega o áudio
    audio = AudioSegment.from_file(file_path)
    
    # Cria o diretório de saída se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Extrai o nome do arquivo sem extensão
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Calcula o número de pedaços
    total_length = len(audio)
    num_chunks = total_length // chunk_length
    
    for i in range(num_chunks + 1):
        start_time = i * chunk_length
        end_time = start_time + chunk_length
        
        # Extrai o pedaço
        chunk = audio[start_time:end_time]
        
        # Verifica se o pedaço é maior que o tamanho mínimo permitido
        if len(chunk) >= min_length:
            chunk_name = f"{output_dir}/{file_name}_chunk_{i + 1}.wav"
            chunk.export(chunk_name, format="wav")
            print(f"Exportado {chunk_name}")


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
input_folder = r"/home/viniods/Downloads/cml_tts_dataset_portuguese_v0.2/train/audio"
output_folder = r"/home/viniods/www/Projects/so-vits-svc/sliced_wavs"
process_folder_recursive(input_folder, output_folder)