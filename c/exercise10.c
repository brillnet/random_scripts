#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    
    //  Creating buffer
    char snum[6];
    
    //  Creating total
    int total = 0;
    
    //initializing i counter
    int i;

    //  This integer will hold the integer value
    //  of snum[i]
    int int_value;

    //  Converting the integers to a string buffer.
    //  The integers will be stored in decimal numbers
    //  but the decimal numbers will be equal the ascii
    //  equivalent. Example 57 in decimal would equal '9' 
    //  in ascii.
    sprintf(snum,"%d",n);

    // Looping through the string to get the total.
    for (i = 0; i < 5; i++) 
    {
        //  Determining integer value of snum[i] by subtracting 
        //  '0' from the value. Subtracting the ASCII value 
        //  of 0 will give us the integer value of snum[i].
        int_value = snum[i] - '0';

        //  Adding the integer value of snum[i] to the total.
        total = total + int_value;        
    }

   //  Printing the total. 
   printf("%d",total);
    
    return 0;
}