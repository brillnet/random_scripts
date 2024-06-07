#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int marks_summation(int* marks, int number_of_students, char gender) {
  
  int index_start;
  int sum = 0;


  //Write your code here.
  if (gender=='b')
  {
    index_start = 0;
  }
  else
  {
    index_start = 1;
  }

  for (int i = index_start; i < number_of_students; i=i+2) 
  {
    sum = sum + marks[i];
  }

  return sum;
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}