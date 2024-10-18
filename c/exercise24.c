#include <stdio.h>

// ** is almost always tied to an array of pointers.

int main()
{
    char *fruit[] = {
        "watermelon",
        "banana",
        "pear",
        "apple",
        "coconut",
        "grape",
        "blueberry"    
        };

    //  Setting up char pointer pa to fruit char
    //  pointers array.
    char *pa = *fruit;

    int x;
    for(x=0;x<7;x++)
    {
        //  Getting value of char
        //  located at pointer of current position
        //  AND THEN incrementing the pointer.
        char current_char = *pa++;
        
        //  Checking to see if the current char
        //  is at end of char string.
        while(current_char)
        {
            //  Printing current char.
            printf("%c",current_char);
            
            //  Getting value of char
            //  at pointer of current position
            //  AND THEN incrementing the pointer.
            current_char = *pa++;
        }
        //  Inserting newline.
        putchar('\n');
    }

    return(0);

}