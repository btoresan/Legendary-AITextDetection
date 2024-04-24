import json

#divide o texro em parte de (default)140 caracteres (tamanho da entry da row)
def split_text_into_rows(text, row_length=140):
    rows = []
    start_idx = 0
    
    #Passa por todo o texto
    while start_idx < len(text):
        #Estima que o final da row seja daqui a 1500 chars
        end_idx = min(start_idx + row_length, len(text))
        
        #Se o final da row nao for o final do texto e nao estivermeos em um espaco
        if end_idx < len(text):
            #Move o final da row pra tras até achar um espaço
            while end_idx > start_idx and text[end_idx] != ' ':
                end_idx -= 1
            #Se nao acharmos um espaço faz o split no fim do index
            if end_idx == start_idx:
                end_idx = min(start_idx + row_length, len(text))
        
        #Addiciona a nova row ao array
        rows.append(text[start_idx:end_idx])

        #Move o inicio da proxima row pro fim do atual + 1
        start_idx = end_idx + 1 if end_idx < len(text) else len(text)
    
    return rows


def main(input_file, output_file):
    #abre o arquivo
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    #carrega um array ja dividido nas rows
    rows = split_text_into_rows(text)

    #salva o que carregar no arquivo json no padrao do dataset da IMB usado pelo HuggingFace
    json_data = {
        "features": [
            {"feature_idx": 0, "name": "text", "type": {"dtype": "string", "_type": "Value"}},
            {"feature_idx": 1, "name": "label", "type": {"names": ["Hum", "IA"], "_type": "ClassLabel"}}
        ],
        "rows": [],
        "num_rows_total": len(rows),
        "num_rows_per_page": 100,
        "partial": False
    }

    #carrega no array rows do json cada uma das rows do texto
    for i, row_text in enumerate(rows):
        json_data["rows"].append({"row_idx": i, "row": {"text": row_text, "label": 0}, "truncated_cells": []})

    #finalmente lanca pro json o que foi carregado
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4)

if __name__ == "__main__":
    input_file = "textos/HUM.txt"  #Mudar para o arquivo de entrada
    output_file = "output.json"  #Mudar para o arquivo de saida
    main(input_file, output_file)
