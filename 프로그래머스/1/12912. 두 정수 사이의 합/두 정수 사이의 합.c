#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long solution(int a, int b) {
    long answer = 0;
    int big, small;
    if (a >= b){
        big = a;
        small = b;
    } else {
        big = b;
        small = a;
    }
    
    for (long i = small; i <= big; i++){
        answer += i;
    }
    return answer;
}