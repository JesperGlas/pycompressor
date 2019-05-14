import os
import sys

OUTPUT_FILE = 'output.txt'
OUTPUT_PATH = './' + OUTPUT_FILE

with open(sys.argv[1], 'r') as input_file:
    input_path = './' + sys.argv[1]

    print('Input file size: ', os.path.getsize(input_path))
    output = open('output.txt', 'w+')
    output_arr = []
    for byte in input_file.read():
        byte = format(ord(byte), '08b')
        print(byte)
    
    output_str = ''
    for element in output_arr:
        output_str += element

    output.write(output_str)
    
    print('Output file size: ', os.path.getsize(OUTPUT_PATH))

