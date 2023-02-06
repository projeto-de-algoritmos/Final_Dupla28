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
    
    delimiter = ', '
    sf28_code = delimiter.join("{}: {}".format(key, value) for key, value in huff.items())
    
    encoded = encoded + " sl28code:" + sf28_code
    
    file = io.StringIO(encoded)
    
    return file.getvalue()