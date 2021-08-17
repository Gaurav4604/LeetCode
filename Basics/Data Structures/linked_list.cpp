#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node *next;
};



class SingleLinkedList{
    private:
        Node *head;
        Node *curr;

    public:
        int length;

    SingleLinkedList(){
        head = NULL;
        curr = NULL;
        length = 0;
    }

    void insert(int data){
        if (head == NULL){
            head = new Node();
            head->data = data;
            head->next = NULL;
        }
        else
        {
            Node *newNode = new Node();
            newNode->data = data;
            Node *refToHead = head;
            if (refToHead->next == NULL)
            {
                head->next = newNode;
            }
            else
            {
                curr->next = newNode;
            }
            // passing reference of last element to current (so that current is the last element of linked list)
            curr = newNode;
        }
        length++;
    }

    void update(int index, int value)
    {
        if (index < length)
        {
            int listIndex = 0;
            Node *refToHead = head;
            if (index == length - 1)
            {
                curr->data = value;
                return;
            }
            while (refToHead->next != NULL)
            {
                if (listIndex == index)
                {
                    refToHead->data = value;
                    break;
                }
                refToHead = refToHead->next;
                listIndex++;
            }
            return;
        }
        else
        {
            cout << "Index out of range";
        }
    }

    void deleteListNode(int index)
    {
        if (length > index)
        {
            if (index == 0)
            {
                Node *temp = head;
                head = head->next;
                free(temp);
            }
            else if (index == length - 1)
            {
                Node *refToHead = head;
                // to traverse to the second last element of the list
                while (refToHead->next->next != NULL)
                {
                    refToHead = refToHead->next;
                }
                // store current last value of list
                Node *temp = curr;
                // pointing to the desired last value of the list
                curr = refToHead;
                curr->next = NULL;
                // deleting the old last value of list
                free(temp);
            }
            else
            {
                int count = 0;
                Node *refToHead = head;
                Node *refToPrev = NULL;

                while (count != index)
                {
                    refToPrev = refToHead;
                    refToHead = refToHead->next;
                    count++;
                }
                Node *nextToBeDeleted = refToHead->next;
                refToPrev->next = nextToBeDeleted;
                free(refToHead);
            }
            length--;
        }
    }

    void print()
    {
        Node *refToHead = head;
        if (refToHead != NULL)
        {
            while (refToHead->next != NULL)
            {
                // traversing through the list
                cout << refToHead->data << " ";
                refToHead = refToHead->next;
            }
            // to print out the last element of the list
            cout << refToHead->data << endl;
        }
        else
        {
            cout << "List is empty";
        }
    }
};




int main()
{
    SingleLinkedList list;
    list.insert(10);
    list.insert(20);
    list.insert(30);
    list.insert(40);
    list.insert(50);
    list.print();

    list.update(1, 15);
    list.print();

    list.deleteListNode(3);
    list.print();
}