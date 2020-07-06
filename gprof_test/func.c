#include <stdio.h>

void func() {
    printf("Inside func\n");
    int i = 0;

    for (; i < 0xffffff; ++i);
    return;
}

