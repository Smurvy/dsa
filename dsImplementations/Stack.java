import java.util.ArrayList;

class Stack<T> {
    private ArrayList<T> stack;
    private int top;

    public Stack(){
        this.stack = new ArrayList<T>();
        top = -1;
    }

    public int push(T val){
        this.stack.add(val);
        top++;
        return top;
    }

    public T pop(){
        if (top == -1){
            throw new Error("The stack is currently empty!");
        }
        top--;
        return this.stack.removeLast();
    }

}