import os

# Diretório raiz onde estão as pastas com os arquivos .cnf
root_directory = "test/"

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

            # Lê a primeira linha do arquivo .cnf
            with open(cnf_file_path, 'r') as cnf_file:
                first_line = cnf_file.readline().strip()  # Remove espaços em branco
                # Renomeia a pasta com o conteúdo da primeira linha do arquivo .cnf
                os.rename(folder_path, os.path.join(
                    root_directory, first_line))
                print(f"A pasta {folder_name} foi renomeada para {first_line}")
        else:
            print(f"Nenhum arquivo .cnf encontrado na pasta {folder_name}")
