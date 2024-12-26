from collections import Counter
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, current_code="", codes={}):
    # Рекурсивное построение кодов
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
    build_huffman_codes(node.left, current_code + "0", codes)
    build_huffman_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text):

    root = build_huffman_tree(text)


    codes = build_huffman_codes(root)


    encoded_text = "".join(codes[char] for char in text)


    print(len(codes), len(encoded_text))
    for char, code in sorted(codes.items()):
        print(f"'{char}': {code}")
    print(encoded_text)


text = "Errare humanum est."
huffman_encode(text)
