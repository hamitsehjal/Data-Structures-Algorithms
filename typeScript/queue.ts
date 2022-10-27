// Implementing a Queue Data Structure

type Node<T> = {
  value: T;
  next?: Node<T>;
};
export default class Queue<T> {
  public length: number;
  private head?: Node<T>;
  private tail?: Node<T>;

  constructor() {
    this.head = this.tail = undefined;
    this.length = 0;
  }

  enqueue(item: T): void {
    this.length++;
    const node={value:item}as Node<T>;

    if (!this.tail) {
      this.tail = this.head = node;
      return;
    }

    this.tail.next=node;
    this.tail=node;
    
  }

  deque(): T | undefined {
    // popping item from beginning of queue
    if (!this.head) {
      return undefined;
    }

    // we need to do some bookeeping now!
    this.length--;

    const head = this.head;
    this.head = this.head.next;

    // free
    head.next = undefined;

    return head.value;
  }

  peek(): T | undefined {
    // if head is not null or not undefined, then get the value and return it
    return this.head?.value;
  }
}
