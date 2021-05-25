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

int main(int argc, char *argv[])
{
    int tabSize = 10000000;
    int maxValue = 5000000;

    bool noOutput = false;
    bool debug = false;


    for (int i = 1; i < argc; i++)
    {
        string arg(argv[i]);
        if (arg == "--nooutput")
        {
            noOutput = true;
        }
        else if (arg.rfind("--nbop=", 0) == 0)
        {
            char *s = argv[i];
            int nb = atoi(s + 7);
            if (nb > 0)
            {
                tabSize = nb;
            }
        }
        else if (arg == "--debug")
        {
            debug = true;
        }
    }

    if (debug)
    {
        for (int i = 0; i < argc; i++)
        {
            cout << "   argv[" << i << "] : '" << argv[i] << "'" << endl;
        }
        cout << "lang=cpp;tabSize=" << tabSize << ";maxValue=" << maxValue
             << ";noOutput=" << noOutput << ";debug=" << debug << endl;
    }

    int *arr = createArray(tabSize, maxValue);
    int n = tabSize / sizeof(arr[0]);

    /*Here we take two parameters, the beginning of the
    array and the length n upto which we want the array to
    be sorted*/
    sort(arr, arr + n);

    if (!noOutput)
    {
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
    }

    delete arr;

    return 0;
}