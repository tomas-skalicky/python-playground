import sys
from builtins import int

def translate_binary(chunk):
    return str(int(chunk, 2))

def translate_rest(chunk, output):
    for digit in chunk:
        if (digit == '0'):
            output += '8'
        else:
            output += '9'
    return output

def restore_till_7(digit):
    return bin(digit)[2:].zfill(3)

def restore_8_and_9(digit):
    if (digit == 8):
        return '0'
    else:
        return '1'

def main():
    
    original_input = ''
    output = ''
    
    with open('input.txt', mode='r') as in_file:
        while True:
            new_chunk = in_file.read(3)
            if not new_chunk:
                break
            original_input += new_chunk
            if len(new_chunk) == 3:
                output += translate_binary(new_chunk)
            else:
                output = translate_rest(new_chunk, output)
    
    print(output)
    
    restored_output = ''
    
    for digitChar in output:
        digit = int(digitChar)
        if digit < 8:
            restored_output += restore_till_7(digit)
        else:
            restored_output += restore_8_and_9(digit)
    
    print(restored_output)
    
    if original_input == restored_output:
        print('same')
    else:
        print('DIFFERENT')
        print(original_input)
        print(restored_output)

main()