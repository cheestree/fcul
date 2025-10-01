#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int gi1 = 123; // global variable initialized
int g1; // global variable uninitialized

int main (int argc, char **argv) // Command line arguments
{
    int l1; // local variable

    int *alloc = malloc(16);

    printf("l1 [%p]\n", &l1);
    printf("argc [%p], &argv [%p], argv [%p], *argv [%p] \n", &argc, &argv, argv, *argv); // *argv = program name
    printf("g1 [%p]\n", &g1);
    printf("gi1 [%p]\n", &gi1);
    printf("alloc [%p]\n", &alloc);
    return 0;
}

/*
c)
l1 - [0x7fffffffde54]
argc - [0x7fffffffde4c]
&argv - [0x7fffffffde40]
argv - [0x7fffffffdf48]
*argv - [0x7fffffffde2b9]
g1 - [0x555555755018]
gil - [0x555555755010]

l1, argc, &argv, argv, *argv are stored in stack segment due to being parameters and local variables

g1 is stored in bss segment due to being uninitialized global variable

gi1 are stored in data segment due to being global variables

d)
alloc - [0x7fffffffde50]

alloc is stored above global variables in stack segment due to being a local variable allocated with malloc

e)
l1 - [0x7fffffffde5c]
argc - [0x7fffffffde4c]
&argv - [0x7fffffffde30]
argv - [0x7fffffffdf48]
*argv - [0x7ffffffffe2b3]
g1 - [0x555555755018]
gil - [0x555555755010]
alloc - [0x7fffffffde50]

-fno-stack-protector 
Disables stack canaries, which are used to detect stack buffer overflows.
These are 4-8 byte values placed on the stack to detect corruption.
Function prologues and epilogues are shorter.


-fno-asynchronous-unwind-tables
Disables generation of unwind tables for exception handling.
This can reduce binary size and improve performance in some cases.
This is useful for programs that do not use exceptions or need stack unwinding.

*/