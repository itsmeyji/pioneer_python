#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int num1;
    int j = 1;
    scanf("%d", &num1);
    while (j <= num1) {
        int i = 1;
        while (i <= j) {
            printf("*");
            i++;
        }
        printf("\n");
        j++;
    }
    return 0;
}