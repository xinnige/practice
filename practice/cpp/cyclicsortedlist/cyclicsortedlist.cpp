#include "stdio.h"
#include "stdlib.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

struct node 
{
    int value;
    struct node* pre;
    struct node* next;
   
    node(int number):value(number){} 
};

node* init_cyclic_sortedlist(string line)
{
    stringstream ss(line);
    string value;
    node* prev=NULL;
    node* first=NULL;
    while (ss >> value){
        cout << "processing..." << value << endl;
        int number = atoi(value.c_str());

        node* anode = new node(number);
        anode->pre=prev;
        if (prev == NULL){
            first = anode;
        } else {
            prev->next = anode;
        }        
        cout << "current node address: "<<anode <<endl;
    
        prev = anode;
        
    }
    first->pre=prev;
    prev->next=first;
    return first;
};

void print_cyclic_list(node* current)
{
    node* end = current->pre;
    while (current != end){
        cout<<current->value<<"->";
        current = current->next;
    }

    cout<<current->value<<"->"<<current->next->value<<endl;
}


void insert(int number, node* current)
{
    node* begin = current;
    while (current->next != begin){
        if ( current->value <= number && current->next->value >= number){
            node* insertpoint = new node(number);
            current->next->pre= insertpoint;
            insertpoint->next= current->next;
            current->next = insertpoint;
            insertpoint->pre = current;
            break;
        } else{
            current = current->next;
        }  
    }
    if (current->next == begin){
        node* insertpoint = new node(number);
        current->next->pre= insertpoint;
        insertpoint->next= current->next;
        current->next = insertpoint;
        insertpoint->pre = current;
    }
}

int main()
{
    // construct the sorted list from file.
    string filename = "cycliclist.txt";
    fstream fs;
    fs.open(filename.c_str());
    string line;
    getline(fs,line);
    fs.close();
   
    cout << "File:" << line << endl;     
 
    node* head = init_cyclic_sortedlist(line);
    print_cyclic_list(head);

    //
    insert(6,head);
    print_cyclic_list(head);

    return 0;
}
