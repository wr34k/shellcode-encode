#!/usr/bin/env bash
nasm -f elf64 "$1.s"
ld -o "$1" "$1.o"
rm -f "$1.o"
