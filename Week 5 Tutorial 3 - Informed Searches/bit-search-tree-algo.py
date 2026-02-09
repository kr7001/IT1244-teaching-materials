def find_node(n):
    binary = bin(n)[2:]  # Get binary: bin(5) = '0b101' -> '101'
    path = binary[1:]     # Skip first bit: '101' -> '01'
    
    result = ""
    for bit in path:
        if bit == '0':
            result += 'L'
        else:
            result += 'R'
    
    return result

# Test
find_node(11) # 'LRR'
find_node(5) # 'LR'

