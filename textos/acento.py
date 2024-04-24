import unicodedata

def corrigir_acentos(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as entrada:
        texto = entrada.read()

    texto_corrigido = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')

    with open(arquivo_saida, 'w', encoding='utf-8') as saida:
        saida.write(texto_corrigido)

# Substitua 'arquivo_entrada.txt' pelo nome do seu arquivo de entrada
# e 'arquivo_saida.txt' pelo nome que deseja dar ao arquivo corrigido
corrigir_acentos('Fonte1.txt', 'arquivo_saida.txt')
