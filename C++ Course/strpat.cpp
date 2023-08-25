#include <iostream>
#include <string>

using namespace std;

int main()
{

    string inp;
    cin >> inp;

    for (int j{0}; j < inp.length(); ++j)
    {
        int count{-1};
        for (int i{0}; i < 2 * inp.length(); ++i)
        {
            if (i < inp.length() - j)
            {
                cout << " ";
            }
            else if (i > inp.length() + j)
            {
                break;
            }
            else
            {
                if (i <= inp.length())
                {
                    ++count;
                }
                else
                {
                    --count;
                }
                cout << inp[count];
            }
        }
        cout << endl;
    }
    return 0;
}