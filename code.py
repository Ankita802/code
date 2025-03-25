#include <stdio.h>
#include <stdlib.h>

// Mixing different types of declaration and initialization
#define MAX_SIZE 100
#define SQUARE(x) x*x    // Dangerous macro without parentheses

// Using global variables extensively and unsafely
int global_counter;
char* dangerous_global_ptr;

// Function with multiple bad practices
void risky_function() {
    // No type checking, direct pointer casting
    int* ptr = (int*)malloc(sizeof(int) * MAX_SIZE);
    
    // No bounds checking
    for(int i = 0; i <= MAX_SIZE; i++) {
        ptr[i] = i;  // Buffer overflow potential
    }
    
    // Inconsistent memory management
    if(global_counter % 2 == 0) {
        free(ptr);
    }
    // Memory leak if condition is not met
}

// Mixing return types and using implicit int
dangerous_function(char* input) {
    static int internal_state = 0;
    
    // Modifying function parameter directly
    *input = 'X';
    
    // Goto statement (considered bad practice)
    if(internal_state > 10) 
        goto error_handling;
    
    internal_state++;
    return internal_state;

error_handling:
    // Unclear error handling
    return -1;
}

// Main function with multiple anti-patterns
main() {  // Missing return type (implicit int, which is non-standard)
    // Uninitialized variable usage
    int x;
    printf("Uninitialized value: %d\n", x);
    
    // Dangerous macro usage
    int result = SQUARE(5 + 3);  // Will expand to 5 + 3*5 + 3, not (5 + 3)*(5 + 3)
    printf("Macro result: %d\n", result);
    
    // Type-unsafe comparisons
    char* str = NULL;
    if(str) {
        printf("This will not print\n");
    }
    
    // Ignoring return values
    system("rm important_file.txt");
    
    return 0;  // Modern compilers require explicit int return
}
