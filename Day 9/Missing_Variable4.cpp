#include <iostream>
using namespace std;

int calculateSum() { // parameters refer to a & b (int)
    return a+b;
}

int main() {
    int result = calculateSum(); // call function after declaring variables
    int a = 5;
    int b = 10;
    cout << result << endl;
    return 0;
}