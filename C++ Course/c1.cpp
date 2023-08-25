#include<iostream>

using namespace std;

const float taxRate {0.06};
const int smallRoom {25};
const int largeRoom {35};
const int validity {30};

int main(){
    cout << "Enter the number of small rooms that needs to be cleaned ?";
    int numSmallRoom {0};
    cin >> numSmallRoom;

    cout << "Enter the number of large rooms that needs to be cleaned ?";
    int numLargeRoom {0};
    cin >> numLargeRoom;

    cout << "---------------------------------------------------------"<< endl;
    cout << "Estimate cost for cleaning service" << endl;
    cout << "Number of small rooms : " << numSmallRoom << endl;
    cout << "Number of large rooms : " << numLargeRoom << endl;
    cout << "\nPrice per small rooms : " << smallRoom << endl;
    cout << "Price per large rooms : " << largeRoom << endl;
    cout << "Cost : "<<((smallRoom * numSmallRoom)+(largeRoom*numLargeRoom))<<endl;
    cout << "Tax  : "<<((smallRoom * numSmallRoom)+(largeRoom*numLargeRoom))*taxRate <<endl;
    cout << "=========================================================="<< endl;
    cout << "\nTotal estimate : "<<(((smallRoom * numSmallRoom)+(largeRoom*numLargeRoom))+((smallRoom * numSmallRoom)+(largeRoom*numLargeRoom))*taxRate)<<endl;
    cout << "This estimate is valid for " << validity << " days"<<endl; 

    return 0;
}