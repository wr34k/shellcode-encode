jmp short three

one:
    pop rsi
    xor rcx, rcx
    mov cl, 20

two:
    sub byte [rsi + rcx -1], 1
    sub cl, 1
    jnz two
    jmp short four

three:
    call one

four:
