#codigo para remover indicies de linha na conversao pdf -> .txt

def remove_numeracao_paginas(texto):
    linhas = texto.split('\n')
    texto_sem_paginas = []

    for linha in linhas:
        # Verifica se a linha contém um número de página e ignora essa linha
        if not linha.isdigit():
            texto_sem_paginas.append(linha)

    # Reconstroi o texto sem as linhas de números de página
    texto_final = '\n'.join(texto_sem_paginas)

    return texto_final

# Exemplo de uso
with open('Limpo3.txt', 'r', encoding='utf-8') as arquivo:
    texto_original = arquivo.read()

texto_sem_paginas = remove_numeracao_paginas(texto_original)

# Escreve o texto sem as páginas numeradas em um novo arquivo
with open('livro_sem_paginas.txt', 'w', encoding='utf-8') as arquivo_saida:
    arquivo_saida.write(texto_sem_paginas)

print("Páginas numeradas removidas e o texto foi salvo em 'livro_sem_paginas.txt'")
