#include <stdio.h>

struct Node {
    int n;
    struct Node* pointer;
};


struct Node addNode(struct Node* oldNode, int val){
    struct Node newNode;
    
    newNode.n = val;
    oldNode->pointer = &newNode;
    
    return newNode;
}

int main() {
    struct Node node1;
    
    node1.n = 7;
    struct Node node2 = addNode(&node1,5);
    
    printf("%d\n",node2.n);
    printf("pointer to original node: %p", node1.pointer);

    return 0;
}

