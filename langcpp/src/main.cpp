#include <bits/stdc++.h>
#include <vector>

using namespace std;

long last = 0;

int randomNumber(int max)
{
    last = (25214903917l * last + 11l) % 281474976710656l;
    long tmp = (last >= 0) ? last : -last;
    return tmp % max;
}

std::vector<int> *createArray(int len, int maxValue)
{
    std::vector<int> *p_array = new vector<int>();
    for (int i = 0; i < len; i++)
    {
        p_array->push_back(randomNumber(maxValue));
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

    std::vector<int> *arr = createArray(tabSize, maxValue);

    sort(arr->begin(), arr->end());

    if (!noOutput)
    {
        cout << "Array after sorting using "
                "default sort is : "
             << endl;
        int i = 0;
        for (auto it = arr->cbegin(); it != arr->cend() && i < 10; ++it, i++)
        {
            cout << *it << " ";
        }

        if (i < tabSize)
        {
            cout << "...";
        }
        cout << "\n";
    }

    delete arr;

    return 0;
}