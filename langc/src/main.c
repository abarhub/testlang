#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

long last = 0;

int randomNumber(int max)
{
    last = (25214903917l * last + 11l) % 281474976710656l;
    long tmp = (last >= 0) ? last : -last;
    return tmp % max;
}

int *createArray(int len, int maxValue)
{
    int *p_array = (int *)malloc(sizeof(int) * len);
    for (int i = 0; i < len; i++)
    {
        p_array[i] = randomNumber(maxValue);
    }
    return p_array;
}

int comp(const void *elem1, const void *elem2)
{
    int f = *((int *)elem1);
    int s = *((int *)elem2);
    if (f > s)
        return 1;
    if (f < s)
        return -1;
    return 0;
}

bool prefix(const char *pre, const char *str)
{
    return strncmp(pre, str, strlen(pre)) == 0;
}

int main(int argc, char *argv[])
{
    int tabSize = 10000000;
    int maxValue = 5000000;
    bool noOutput = false;
    bool debug = false;

    for (int i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "--nooutput") == 0)
        {
            noOutput = true;
        }
        else if (prefix("--nbop=", argv[i]))
        {
            char *s = argv[i];
            int nb = atoi(s + 7);
            if (nb > 0)
            {
                tabSize = nb;
            }
        }
        else if (strcmp(argv[i], "--debug") == 0)
        {
            debug = true;
        }
    }

    if (debug)
    {
        for (int i = 0; i < argc; i++)
        {
            printf("   argv[%d] : '%s'\n", i, argv[i]);
        }
        printf("lang=c;tabSize=%d;maxValue=%d;noOutput=%d;debug=%d\n",
               tabSize, maxValue, noOutput, debug);
    }

    int *x = NULL;
    x = createArray(tabSize, maxValue);

    qsort(x, tabSize / sizeof(*x), sizeof(*x), comp);

    if (!noOutput)
    {
        int i = 0;
        for (i = 0; i < 10 && i < tabSize; i++)
        {
            printf("%d ", x[i]);
        }
        if (i < tabSize)
        {
            printf("...");
        }
        printf("\n");
    }

    free(x);

    return 0;
}