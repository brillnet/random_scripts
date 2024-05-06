#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>



int main() 
{
    int a, b;
    scanf("%d\n%d", &a, &b);

  	// Complete the code.
    int i;

    //  Creating array that has all values 0 to 9 written
    //  out.
    char *arr[] = { "zero",
                    "one", 
                    "two",
                    "three",
                    "four",
                    "five",
                    "six",
                    "seven",
                    "eight",
                    "nine" };

    for (i = a; i <= b; i++) 
    {
        if (i <= 9) 
        {
            printf("%s\n", arr[i]);
        }
        else if (i > 9 && i % 2 == 0) 
        {
            // Printing even
            printf("%s\n", "even");
        }
        else if(i > 9 && i % 2 != 0) 
        {
            // Printing odd
            printf("%s\n", "odd");
        }
        else
        {
            //  Unimplemented
        }
    }

    return 0;
}

