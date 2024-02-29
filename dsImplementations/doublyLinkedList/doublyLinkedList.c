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

struct Node pop(struct Node node1){
    if(node1.forwardPointer == NULL){
        if(node1.backwardPointer != NULL){
       
            // need to "unlink" the node we are returnign from the previous node
            node1.backwardPointer->forwardPointer = NULL;
            node1.backwardPointer = NULL;
        }
        
        return node1;
    }  else {
        pop(*node1.forwardPointer);
    }

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
    node1.backwardPointer = NULL;
    node1.forwardPointer = NULL;
    node1.number = 7;
    

    struct Node node2 = addNode(&node1,8);
    struct Node node3 = addNode(&node2,9);

    pop(node1);

    printLinkedList(node1);
    return 0;
}