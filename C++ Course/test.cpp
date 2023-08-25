#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> nums{0, 1, 2, 3, 4};
    for (unsigned i = 0; i < nums.size(); ++i)
        cout << i << ((i % 2 == 0) ? " is even" : " is odd") << endl;
    for (int i : nums)
    {
        cout << i << " ";
    }
    cout << endl;
    system("pause");
    return 0;
}