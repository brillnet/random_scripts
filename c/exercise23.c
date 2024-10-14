#include <stdio.h>

int main()
{
    char alphabet[26];
    int x;
    char *pn;

    // Intializing pointer
    pn = alphabet;

    // Filling array
    for(x=0;x<26;x++)
    {
        //  Incremnting the value at pointer memory address 
        //  adding x to char 'A' doing this 26 times. This 
        // should get us every letter in the alphabet.

        //   Incrementing the memory pointer by OBE bytes
        //   Remember when incrementing a pointer it will 
        //   increment by the default size of the data type
        //   set for the pointer. In this case a char is one byte.
        *pn++=x+'A';

    }

    // The below line is odd to me because if you print the memory
    // address of pn with %pn before the pointer is reinitialized
    // it will be the same as after reinitializing.

    // Re-Intializing pointer. 
    pn = alphabet;


    //  Filling and printing values in array and memory addresses for each
    //  variable.
    for(x=0;x<26;x++)
    {
        
        //  Printing value at pointers memory location in array.
        putchar(*pn);

        // Incrementing pointer
        pn++;
    }
    putchar('\n');

    return(0);

}