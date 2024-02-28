#include <stdio.h>

struct Node {
    int number;
    struct Node* forwardPointer;
    struct Node* backwardPointer;
};

void printInfo(struct Node n){
    printf("Number: %d\n",n.number);
    printf("forward pointer: %p\n",n.forwardPointer);
    //printf("backward pointer: %p\n",n.backwardPointer);
    printf("nodes location in memory: %p\n",&n);
}


struct Node addNode(struct Node* oldNode, int val){
    struct Node node2;
    node2.number = val;
    node2.backwardPointer = oldNode;
    oldNode->forwardPointer = &node2;
    return node2;

}



void printLinkedList(struct Node node){
    if(node.forwardPointer != NULL){
        printf("%d\n",node.number);
        printLinkedList(*(node.forwardPointer));
    } else {
        printf("%d\n",node.number);
    }
    
      
}

int main() {
    // if no value is set, the pointers automatically point to itself
    struct Node node1;
    node1.number = 7;


    struct Node node2 = addNode(&node1,8);
    struct Node node3 = addNode(&node2,9);


    printLinkedList(node1);
    return 0;
}