#include <bits/stdc++.h>
using namespace std;

long last = 0;

int randomNumber(int max)
{
    last = (25214903917l * last + 11l) % 281474976710656l;
    long tmp = (last >= 0) ? last : -last;
    return tmp % max;
}

int *createArray(int len, int maxValue)
{
    int *p_array = new int[len];
    for (int i = 0; i < len; i++)
    {
        p_array[i] = randomNumber(maxValue);
    }
    return p_array;
}

int main()
{
    const int tabSize = 10000000;
    const int maxValue = 5000000;

    int* arr = createArray(tabSize, maxValue);
    int n = tabSize / sizeof(arr[0]);

    /*Here we take two parameters, the beginning of the
    array and the length n upto which we want the array to
    be sorted*/
    sort(arr, arr + n);

    cout << "\nArray after sorting using "
            "default sort is : \n";
    int i = 0;
    for (i = 0; i < n && i < 10; ++i)
    {
        cout << arr[i] << " ";
    }
    if (i < n)
    {
        cout << "...";
    }
    cout << "\n";

    delete arr;

    return 0;
}