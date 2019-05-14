import os
import sys

OUTPUT_FILE = 'output.txt'
OUTPUT_PATH = './' + OUTPUT_FILE

VALUES = range(0, 255)

# Help Methods
def flipArray(input_arr):
    flipped_arr = []
    for element in input_arr:
        flipped_arr.insert(0, element)
    
    return flipped_arr

def sortFreqArray(input_arr):
    sorted_arr = []
    for idx, element in enumerate(input_arr):
        # If array is empty, add first element
        if sorted_arr.__len__() == 0:
            sorted_arr.append(element)
        # If new element freq is smaller than first sorted element, add first in the sorted array
        elif element[1] < sorted_arr[0][1]:
            sorted_arr.insert(0, element)
        # If new element freq is larger than last sorted element, add last in the sorted array
        elif element[1] > sorted_arr[sorted_arr.__len__() -1][1]:
            sorted_arr.append(element)
        # If no condition is met, find index where to put it
        else:
            idx = 0
            while idx < sorted_arr.__len__():
                if element[1] < sorted_arr[idx][1]:
                    sorted_arr.insert(idx, element)
                    break
                else:
                    idx += 1
    
    return sorted_arr

# Classes

class Node():

    r_node = None
    l_node = None

    def ___init__(self, value, r_node, l_node):
        self.value = value
        self.r_node = r_node
        self.l_node = l_node

    def setValue(self, value):
        self.value = value
    
    def getValue(self):
        return self.value

    def setRNode(self, node):
        self.r_node = node

    def setLNode(self, node):
        self.l_node = node

    def getRNode(self):
        return self.r_node

    def getLNode(self):
        return self.l_node

with open(sys.argv[1], 'r') as input_file:
    input_path = './' + sys.argv[1]

    # Print original file size for comparison
    print('Input file size: ', os.path.getsize(input_path))

    # Initilize a frequency array to keep track of reacuring patterns
    freq_arr = []

    # Loop through each character from the input file to create a frequency array
    for byte in input_file.read():
        # Convert char to byte
        byte_value = ord(byte)
        # Condition if the freq_array is empty, add first value
        if freq_arr.__len__() == 0:
            freq_arr.append([byte_value, 1])
        # Condition if new value is smaller than first element value, add new at index 0
        elif byte_value < freq_arr[0][0]:
            freq_arr.insert(0, [byte_value, 1])
        # Condiiton if new value is larger than last element value, add new at last index
        elif byte_value > freq_arr[freq_arr.__len__()-1][0]:
            freq_arr.append([byte_value, 1])
        # None of the above, sort
        else:
            idx = 0
            # Loop while there is elements or break
            while idx < freq_arr.__len__():
                # Condition if value at index is equal to new value, add one frequency
                if byte_value == freq_arr[idx][0]:
                    freq_arr[idx][1] += 1
                    break
                # Condition if value at current index is larger than the new one, insert new value at index
                elif freq_arr[idx][0] > byte_value:
                    freq_arr.insert(idx, [byte_value, 1])
                    break
                else:
                    # Increase index and repeat loop
                    idx += 1
                
    # Sort freq_arr based on frequency
    freq_arr = sortFreqArray(freq_arr)
    print(freq_arr)
        
    output = open('output.txt', 'w+')
    print('Output file size: ', os.path.getsize(OUTPUT_PATH))
    input_file.close()
    output.close()

