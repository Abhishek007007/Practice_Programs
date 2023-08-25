#include<iostream>

using namespace std;

int main(){
    int a {20},b{3};
    float c =  static_cast<float>(a) / b;
    cout << c <<endl;

    cout << std::boolalpha;
    cout << (a!=b) <<endl;
    cout << std::noboolalpha;

    return 0;
}