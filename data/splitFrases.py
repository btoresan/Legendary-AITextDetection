with open('textos/Limpo0.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total = (len(frases))
    letras = len(texto)

with open('textos/Limpo1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total += (len(frases))
    letras += len(texto)

with open('textos/Limpo2.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total += (len(frases))
    letras += len(texto)

with open('textos/Limpo3.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    frases = texto.split('.')
    frases = [frase for frase in frases if frase.strip()]
    total += (len(frases))
    letras += len(texto)

print(total)
print(letras)
print(letras // 15)