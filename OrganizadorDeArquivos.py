import os

def gerarNomeUnico(destino): #Essa função evita sobrescrever arquivos que possuem o mesmo nome
    if not os.path.exists(destino): 
        return destino
    
    pasta = os.path.dirname(destino)
    nome = os.path.basename(destino)
    nomeBase, extensao = os.path.splitext(nome)

    contador = 1
    while True:
        novoNome = f"{nomeBase}_{contador}{extensao}" #Se eu tiver um arquivo.txt que foi organizado e depois eu tentar organizar outro arquivo.txt, ele vai criar um arquivo chamado arquivo_1.txt para evitar sobrescrever o arquivo original
        novoCaminho = os.path.join(pasta, novoNome)

        if not os.path.exists(novoCaminho):
            return novoCaminho
        contador +=1

def organizarArquivos(caminho):
    if not os.path.exists(caminho):
        raise FileNotFoundError("O diretório especificado não existe.") #dispara um erro caso o diretório não exista
    
    arquivos = os.listdir(caminho)

    if not arquivos:
        print("Nenhum arquivo encontrado para organizar.")
        return
    
    movidos = 0

    for arquivo in arquivos:
        origem = os.path.join(caminho, arquivo)
        
        if not os.path.isfile(origem): #ignora pastas
            continue

        nome, extensao = os.path.splitext(arquivo)

        if not extensao: #ignora arquivos sem extensão
            continue

        extensao = extensao[1:].lower()  # Remove o ponto da extensão e padroniza nome de pastas evitando problemas como "pdf" e "PDF"
        pastaDestino = os.path.join(caminho, extensao)

        os.makedirs(pastaDestino, exist_ok=True) #cria a pasta de destino se ela não existir, caso contrário, continua
        destino = os.path.join(pastaDestino, arquivo)
        destino = gerarNomeUnico(destino)
        os.rename(origem, destino)
        movidos += 1

    print(f"Arquivos organizados com sucesso. Total de arquivos movidos: {movidos}")

try:
    caminho = input("Digite o caminho para o diretório: ")
    organizarArquivos(caminho)        
except FileNotFoundError:
    print("Diretório não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
