#include<iostream>
#include<vector>

using namespace std;

int main(){
    vector <int> vec {10,20,30,40,50};
    vec.at(0) = 100;
    vec.at(4) = 1000;
    for(int i=0;i<5;i++){
        cout << i+1 <<"th element is " <<vec.at(i)<<endl; 
    }
    return 0;
}