import json

#divide o texro em parte de 1500 caracteres (tamanho da entry da row)
def split_text_into_rows(text, row_length=1500):
    rows = []
    for i in range(0, len(text), row_length):
        rows.append(text[i:i+row_length])
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
    input_file = "Limpo2.txt"  #Mudar para o arquivo de entrada
    output_file = "output.json"  #Mudar para o arquivo de saida
    main(input_file, output_file)
