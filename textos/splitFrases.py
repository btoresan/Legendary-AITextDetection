with open('Limpo2.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total = (len(frases))

with open('Limpo1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total += (len(frases))

with open('Limpo2.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total += (len(frases))

print(total)