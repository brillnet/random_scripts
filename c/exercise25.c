#include <stdio.h>
#include <string.h>

int main()
{
    // Creating array of char pointers.
    char *fruit[] = {
        "apricot",
        "banana",
        "pineapple",
        "apple",
        "persimmon",
        "pear",
        "blueberry"
    };

    // Creating temp char pointer.
    char *temp;
    int a,b,x;
    int result;

    for(a=0;a<6;a++)
    {
        for(b=a+1;b<7;b++)
        {
            result = strcmp(*(fruit+a), *(fruit+b));

            //  Comparing individual char ascii values in str1 against str2
            //  if str1 is > str2 the two strings will be switched in the array.
            //  by changing the individual pointer values.
            if(result > 0)
            {
                temp = *(fruit+a);
                *(fruit+a) = *(fruit+b);
                *(fruit+b) = temp;
            }
        }
    }

    // Printing the values in the array.
    for(x=0;x<7;x++)
    {
        puts(fruit[x]);
    }

    return(0);
}