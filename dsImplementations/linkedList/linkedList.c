#include <stdio.h>

struct Node {
    int number;
    struct Node* pointer;
};


struct Node* addNode(struct Node* oldNode, int val){
    struct Node newNode;
    
    newNode.number = val;
    oldNode->pointer = &newNode;

    return oldNode->pointer;
}

int main() {
    struct Node node1;
    
    node1.number = 7;
    struct Node node2 = *addNode(&node1,87);
    
    printf("%d\n",node2.number);
    printf("pointer to original node: %p", node1.pointer);

    return 0;
}

