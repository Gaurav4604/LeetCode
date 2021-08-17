#include<iostream>

using namespace std;

struct Node{
    int data;
    Node *next;
    Node *prev;
};


class DoubleLinkedList{

    private:
        Node *head;
        Node *curr;

    public:
        int length;

    DoubleLinkedList(){
        head = NULL;
        curr = NULL;
        length = 0;
    }

    void insert(int data){
        if(head == NULL){
            head = new Node();
            head -> data = data;
            head -> next = NULL;
            head -> prev = NULL;
        }
        else if(head -> next == NULL){
            Node *newNode = new Node();
            newNode -> data = data;
            newNode -> prev = head;
            head -> next = newNode;
            curr = newNode;
        }
        else{
            Node *newNode = new Node();
            newNode -> data = data;
            newNode -> prev = curr;
            curr -> next = newNode;
            curr = newNode;
        }
        length++;
    }

    void update(int index, int value){
        if(index < length){
            if(index == 0){
                head -> data = value;
            }
            else if(index == length - 1){
                curr -> data = value;    
            }
            else{
                Node *refToHead = head;
                int tempIndex = 0;
                while(tempIndex != index){
                    refToHead = refToHead -> next;
                    tempIndex++;
                }
                refToHead -> data = value;
            }
        }
        else{
            cout << "index out of range" << endl;
        }
    }

    void deleteNode(int index){
        if (index < length){
            if (index == 0){
                Node *temp = head;
                head = head -> next;
                head -> next -> prev = head;
                head -> prev = NULL;
                free(temp);
            }
            else if(index == length - 1){
                Node *temp = curr;
                curr = curr -> prev;
                curr -> prev -> next = curr;
                curr -> next = NULL;
                free(temp);
            }
            else{
                Node *temp = head;
                int tempIndex = 0;
                while (tempIndex != index){
                    temp = temp -> next;
                    tempIndex++;
                }
                temp -> prev -> next = temp -> next;
                temp -> next -> prev = temp -> prev;
                free(temp);
            }
            length--;
        }
        else{
            cout << "index out of range" << endl;
        }
    }

    void print(){
        Node *refToHead = head;
        while (refToHead -> next != NULL){
            cout << refToHead -> data << " ";
            refToHead = refToHead -> next;
        }
        cout << refToHead -> data << endl;
    }

    void printReverse(){
        Node *refToLast = curr;
        while (refToLast -> prev != NULL){
            cout << refToLast -> data << " ";
            refToLast = refToLast -> prev;
        }
        cout << refToLast -> data << endl;
    }
};

int main(){
    DoubleLinkedList list;
    list.insert(10);
    list.insert(20);
    list.insert(30);
    list.insert(40);
    list.insert(50);

    list.update(0, 15);

    list.deleteNode(2);

    list.print();
    list.printReverse();
}