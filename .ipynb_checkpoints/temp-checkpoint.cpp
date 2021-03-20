#include <iostream>
#include <math.h>

using namespace std;

int main(){
    
    int math_score;
    int programming_language_score;
    int data_structure_score;
    int sum;
    
    float average_score;
    
    string grade;
    
    cout << "Put the discrete math score: ";
    cin >> math_score;
    
    cout << "Put the programming language score: ";
    cin >> programming_language_score;
    
    cout << "Put the data structure score: ";
    cin >> data_structure_score;
      
    sum = math_score + programming_language_score + data_structure_score;
    average_score = sum / 3.0;

    if (average_score > 95){
        grade = "A+";
    }else if(average_score > 90){
        grade = "A0";
    }else if(average_score > 85){
        grade = "B+";
    }else if(average_score > 80){
        grade = "B0";
    }else if(average_score > 75){
        grade = "C+";
    }else if(average_score > 70){
        grade = "C0";
    }else{
        grade = "F";
    }
    
    cout<<fixed;
    cout.precision(2);
    
    cout << "The average score is "
        << average_score
        << " and the grade is "
        << grade
        << "\n";


    return 0;
}

   
