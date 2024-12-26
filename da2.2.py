def huffman_decode(codes, encoded_text):
    reverse_codes = {v: k for k, v in codes.items()}
    decoded_text = ""
    current_code = ""

    for bit in encoded_text:
        current_code += bit

        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""

    return decoded_text

def main():
    num_symbols, encoded_length = 12, 60
    codes = {
        ' ': '1011',
        '.': '1110',
        'D': '1000',
        'c': '000',
        'd': '001',
        'e': '1001',
        'i': '010',
        'm': '1100',
        'n': '1010',
        'o': '1111',
        's': '011',
        'u': '1101'
    }
    encoded_text = "100011110001001101000111111011001010011000010110011010111110"

    decoded_text = huffman_decode(codes, encoded_text)
    print(decoded_text)

main()
