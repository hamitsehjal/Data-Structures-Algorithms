type Node<T> = {
  value: T;
  prev?: Node<T>;
  next?: Node<T>;
};

export default class DoublyLinkedList<T> {
  public length: number;
  private head?: Node<T>;

  constructor() {
    this.length = 0;
    this.head = undefined;
  }

  prepend(item:T):void{
    const node={value:item} as Node<T>;

    this.length++;
    if(!this.head)
    {
        this.head=node;
        return;
    }

    // Here we do double linking!!
    node.next=this.head;
    this.head.prev=node;
    this.head=node;
  }
}
