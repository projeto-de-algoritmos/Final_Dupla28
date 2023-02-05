import os
import heapq
from collections import defaultdict
import io

def compress(filename):
    # Lê o conteúdo do arquivo de texto
    with open(filename, 'r') as f:
        content = f.read()

    # Cria um dicionário com a frequência de cada caractere
    freq = defaultdict(int)
    for char in content:
        freq[char] += 1

    # Cria a árvore de Huffman
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Cria o código de Huffman para cada caractere
    huff = dict()
    for char, code in heap[0][1:]:
        huff[char] = code

    # Codifica o conteúdo usando o código de Huffman
    encoded = ''.join([huff[char] for char in content])

    file = io.StringIO(encoded)
    
    return file.getvalue()
    
    #filename = filename[:-4]
    
    # Escreve o conteúdo codificado em um arquivo com extensão .sl28
    #with open(filename + '.sl28', 'w') as f:
        #f.write(encoded)

def decompress(filename):
    # Lê o conteúdo codificado do arquivo .sl28
    with open(filename, 'r') as f:
        encoded = f.read()

    # Cria o dicionário de decodificação a partir do conteúdo codificado
    decoded = ""
    code = ""
    decoder = defaultdict(str)
    for char in encoded:
        code += char
        if code in decoder:
            decoded += decoder[code]
            code = ""
    decoder = {value: key for key, value in decoder.items()}

    # Decodifica o conteúdo
    i = 0
    while i < len(encoded):
        for j in range(i, len(encoded)):
            if decoder[encoded[i:j+1]] != '':
                decoded += decoder[encoded[i:j+1]]
                i = j
                break

    # Escreve o conteúdo decodificado em um arquivo de texto
    with open(os.path.splitext(filename)[0] + '.txt', 'w') as f:
        f.write(decoded)