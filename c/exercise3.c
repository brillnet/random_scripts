#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    /*  Reading single character*/
    char ch;
    scanf("%c", &ch);

     /* Reading newline character that is still in stdin */
    scanf("\n");

    /* Reading a string of characters until space is encountered or
    new line is encountered. */
    char s[100];
    scanf("%s", s);

    /* Reading newline character that is still in stdin */
    scanf("\n");

    /* Reading a string of characters until newline is encountered */
    char r[100];
    scanf("%[^\n]%*c", r);

    /* Printing out single character. */
    printf("%c", ch);
    
    /* Printing out newline. */
    printf("\n");

    /* Printing out multiple characters. */
    printf("%s", s);

    /* Printing out newline. */
    printf("\n");

    /* Printing out sentence. */
    printf("%s", r);

    /* Printing out newline. */
    printf("\n");

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;

}