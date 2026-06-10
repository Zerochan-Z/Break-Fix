// Index out-of-bounds → use .at() for safe access.

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector <int> scores = {85, 90, 78};

//  old code: 
//  cout << scores[5] << endl;

    try {
        cout << scores.at(5) << endl;
    } catch (out_of_range& e) {
        cout << "Error: Index out of range!" << endl;
    }

    return 0;
}