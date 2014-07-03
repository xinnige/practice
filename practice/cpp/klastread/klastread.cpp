#include "stdlib.h"
#include "stdio.h"
#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int read_lines(char* fpath, string* lines, int& counter)
{
    fstream fs;
    fs.open(fpath);
    string line;
    while(getline(fs,line)){
        lines[(counter%10)]=line;
        counter++;
    } 
    fs.close();
    return 0;
}


int print_strings(string* lines, int counter)
{
    int begin = counter%10;
    for (int i=begin; i<10; i++){
        cout<<lines[i]<<endl;
    }
    for (int i=0;i<begin;i++){
        cout<<lines[i]<<endl;
    }
}

int main(int argc, char* argv[])
{
    //cout<<"Hello, World!"<<endl;
    string lines[10];
    int counter=0;
    read_lines(argv[1],lines,counter);
    print_strings(lines, counter);
    cout<<"Totally lines:"<<counter<<endl;
    return 0;
}
