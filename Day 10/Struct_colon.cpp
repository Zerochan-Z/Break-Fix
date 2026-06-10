#include <iostream>
#include <string>
using namespace std;

struct Student {
    string name;
    int age;
    double gpa;
}; // <<-- don't forget about semicolons

struct Course {
    string title;
    int credits;
}; // <<-- don't forget about semicolons

void displayStudent(Student s) {
    cout << "Name: " << s.name << endl;
    cout << "Age: " << s.age << endl;
    cout << "GPA: " << s.gpa << endl;
}

int main() {
    Student student1;
    student1.name = "Alice";
    student1.age = 20;
    student1.gpa = 3.8;

    Course course1;
    course1. title = "C++ Programming";
    course1.credits = 4;

    displayStudent(student1);

    cout << "\nCourse: " << course1.title << endl;
    cout << "Credits: " << course1.credits << endl;

    return 0;

}