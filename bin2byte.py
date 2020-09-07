#!/usr/bin/env python3
import sys

my_file = sys.argv[1]
binarray = []
with open(my_file, 'rb') as file_t:
    while (byte := file_t.read(1)):
        binarray.append(byte.hex())
    print("new byte[" + str(len(binarray)) + "] { 0x" + binarray[0] + ",0x"+ ",0x".join(binarray[1:]) + " };")
