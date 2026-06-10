#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector <string> items = {"Pen", "Book", "Eraser"};
    int index;

    cout << "Enter index (0-2): ";
    cin >> index;

//    old code:
//    cout << items[index] << endl;

    try {
        cout << items.at(index) << endl;
    } catch (out_of_range& e) {
        cout << "Error input" << endl;
    }

    return 0;
}