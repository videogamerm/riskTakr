#include <stdio.h>
#include <time.h> 
  
int main() 
{ 
  
    struct tm* local; 
    time_t t = time(NULL); 
  
    local = localtime(&t); 
  
    printf("Time and date: %s\n", 
           asctime(local)); 
  
    return 0; 
} 
