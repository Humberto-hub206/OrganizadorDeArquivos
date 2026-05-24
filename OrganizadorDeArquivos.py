import os
#pastas: Word, Excel

def organizarArquivos(caminho, extensao):
    for arquivo in os.listdir(caminho):
        if arquivo.endswith(extensao):
            os.rename(caminho, destino)
    if not any(arquivo.endswith(extensao) for arquivo in os.listdir()):
        print(f"Nenhum arquivo com a extensão {extensao} encontrado.")
            
try:
    caminho = input("Digite o caminho para o diretório: ")
    os.chdir(caminho)

    while True:
        print("1 - .docx\n2 - .excel\n")
        escolha = int(input("Digite qual tipo de arquivo deseja listar: \n"))
        destino = input("Digite o destino (nome do diretório) para os arquivos: ")
        destino = f"{caminho}/{destino}"
        match escolha:
            case 1:
                extensao = ".docx"
                organizarArquivos(caminho, extensao)
            case 2:
                extensao = ".xlsx"
                organizarArquivos(caminho, extensao)
            case _:
                print("Opção inválida, tente novamente.")
except FileNotFoundError:
    print("Diretório não encontrado.")
except ValueError:
    print("Entrada inválida, por favor digite um número.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
