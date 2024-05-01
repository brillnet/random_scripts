#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    
    /* Creating greeting list of chars */
    char greeting[] = "Hello, World!\n";     
	
    char s[100];
    scanf("%[^\n]%*c", &s);
    
    /* Printing greeting */
    printf("%s", greeting);
    
    /* Printing user input*/
    printf("%s", s);
  	
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}