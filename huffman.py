# program to implement huffman encoding using greedy strategy.
# Time Complexity: O(n*Log(n))
# Space Complexity: O(n)

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(data):
    freq_map = {}
    unique_chars = set(data)    

    for char in unique_chars:
        count = data.count(char)
        freq_map[char] = count
    
    root = build_huffman_tree(freq_map)
    codes = build_codes(root)
    encoded_data = ''
    
    for char in data:
        encoded_char = codes[char]
        encoded_data += encoded_char
    
    return encoded_data, codes


def build_huffman_tree(freq_map):
    heap = []

    for char, freq in freq_map.items():
        node = Node(char, freq)
        heapq.heappush(heap, node)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq+right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node, current_path_code='', codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = current_path_code
        build_codes(node.left, current_path_code + '0', codes)
        build_codes(node.right, current_path_code + '1', codes)
    return codes


def main():
    data = 'BCCABBDDAECCBBAEDDCC'
    encoded_data, codes = huffman_encoding(data)
    print(f'Data: {data}')
    print(f'Encoded data: {encoded_data}')
    print(f'Codes: {codes}')


if __name__ == '__main__':
    main()