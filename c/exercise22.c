#include <stdio.h>

int main()
{
    int numbers[10];
    int x;
    int *pn;

    // Intializing pointer
    pn = numbers;

    // Filling array
    for(x=0;x<10;x++)
    {
        //  Incremnting the value at the pn memory
        //  pointer by 1.
        *pn=x+1;
        //   Incrementing the memory pointer by FOUR bytes
        //   Remember when incrementing a pointer it will 
        //   increment by the default size of the data type
        //   set for the pointer.
        pn++;

    }

    //  Printing values in array and memory addresses for each
    //  variable.
    for(x=0;x<10;x++)
    {
        //  Print number[index] = value 
        //  at memory location: memory_address_of_value
        printf("numbers[%d] = %d at mem location: %p\n",x,numbers[x],&numbers[x]);
    }

    return(0);

}