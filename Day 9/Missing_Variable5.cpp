#include <iostream>
using namespace std;

int getScore() { // prefer putting int score in () as parameters
    int score;
    return score;
}

int main() {
    // name the variable (score) or 
    // get score from user 
    // int score = 0;
    // cin << score;
    cout << getScore() << endl; // getScore(score)
    return 0;
}