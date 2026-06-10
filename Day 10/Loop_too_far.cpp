#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector <int> nums = {10, 20, 30, 40, 50};

//    for (int i = 0; i <= nums.size(); i++) {  (fixed <= -> <)
//        cout << nums[i] << " ";  (index include 0, so i must be smaller than its size)
//    }

    for (int i = 0; i < nums.size(); i++) {
        cout << nums.at(i) << " ";
    }
    return 0;
}