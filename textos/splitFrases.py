with open('Limpo0.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    print(len(frases))