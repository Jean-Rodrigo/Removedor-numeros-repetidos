"""Essa função serve para abrir odocumento de texto que vamos usar, serve para reciclar caso eu vá usar para
mais de uma atividade no programa"""


def ler_documento_texto():
    entrada = input("nome do arquivo de texto: ").strip()
    arquivo = open(f"{entrada}.txt", "r")
    texto = str(arquivo.read())
    arquivo.close()
    return texto


"""aqui vamos fazer a limpeza de números copiados"""


def limpar_telefone_repetidos(arquivo_telefone=ler_documento_texto()):
    lista_telefone = arquivo_telefone.split("\n")

    for linha in range(len(lista_telefone)):
        lista_telefone[linha] = lista_telefone[linha].strip("+").strip()

    set_telefone = set(lista_telefone)

    numero_copias = len(lista_telefone) - len(set_telefone)
    print(f"Foram retirados {numero_copias} números de telefone repetidos")

    telefone_final = ""
    for numero in set_telefone:
        telefone_final = telefone_final+f"{numero}\n"

    criar_documento_telefone(telefone_final)


"""agora vamos criar um arquivo de texto com os números sem cópia"""


def criar_documento_telefone(texto_atualizado):
    entrada = input("Nomeie o novo arquivo:")
    arquivo = open(f"{entrada}.txt", "w")
    arquivo.write(texto_atualizado)
    print(str(arquivo))
    arquivo.close()


limpar_telefone_repetidos()