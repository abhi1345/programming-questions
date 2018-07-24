#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// Complete the matrixRotation function below.
void matrixRotation(int matrix_rows, int matrix_columns, int** matrix) {

}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int rows,cols,rot;
    scanf("%d%d%d",&rows,&cols,&rot);
    int arr[rows][cols];
    int result[rows][cols];
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            scanf("%d", &arr[r][c]);
        }
    }

    rows--;
    cols--;
    for (int r = 0; r <= rows; r++) {
        
        
        for (int c = 0; c <= cols; c++) {
            
            
            
            int x = r < rows - r ? r : rows - r;
            int y = c < cols - c ? c : cols - c;
            int min = x < y ? x : y;
            int maxRow = rows - min;
            int maxCol = cols - min;
            int parameter = (maxRow + maxCol) * 2 - min * 4;

            int row = r;
            int col = c;
            
            
            
            for (int i = 0; i < rot%parameter; i++) {
                if (col == min && row < maxRow) {
                    row++;
                }
                else if (row == maxRow && col < maxCol) {
                    col++;
                }
                else if (row > min && col == maxCol) {
                    row--;
                }
                else if (row == min && col > min) {
                    col--;
                }
            }
            
            
            
            result[row][col] = arr[r][c];
        }
        
        
        
        
    }
    
    
    


    for (int t = 0; t <= rows; t++) {
        for (int y = 0; y <= cols; y++) {
            
            
            
            printf("%d ", result[t][y]);
            
            
            
        }
        printf("\n");
    }


    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
