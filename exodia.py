import os
import re

# Função para obter o nome a partir do arquivo .cnf
def get_name_from_cnf(file_path):
    with open(file_path, 'r') as cnf_file:
        # Lê a primeira linha do arquivo .cnf
        first_line = cnf_file.readline()
        # Use uma expressão regular para encontrar o nome
        match = re.search(r'Nome:\s*(\w+)', first_line)
        if match:
            return match.group(1)
    return None

# Diretório raiz onde estão as pastas com os arquivos .cnf
root_directory = "/caminho/do/seu/diretorio/raiz"

# Percorre todas as pastas no diretório raiz
for folder_name in os.listdir(root_directory):
    folder_path = os.path.join(root_directory, folder_name)
    
    # Verifica se é uma pasta
    if os.path.isdir(folder_path):
        # Encontra arquivos .cnf dentro da pasta
        cnf_files = [f for f in os.listdir(folder_path) if f.endswith('.cnf')]
        
        # Verifica se há pelo menos um arquivo .cnf na pasta
        if cnf_files:
            # Assume que estamos usando o primeiro arquivo .cnf encontrado
            cnf_file_path = os.path.join(folder_path, cnf_files[0])
            new_name = get_name_from_cnf(cnf_file_path)
            
            # Se um nome foi encontrado no arquivo .cnf, renomeia a pasta
            if new_name:
                new_folder_path = os.path.join(root_directory, new_name)
                os.rename(folder_path, new_folder_path)
                print(f"A pasta {folder_name} foi renomeada para {new_name}")
            else:
                print(f"Não foi possível encontrar um nome válido no arquivo .cnf da pasta {folder_name}")
        else:
            print(f"Nenhum arquivo .cnf encontrado na pasta {folder_name}")
