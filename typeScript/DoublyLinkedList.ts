type Node<T> = {
  value: T;
  prev?: Node<T>;
  next?: Node<T>;
};

export default class DoublyLinkedList<T> {
  public length: number;
  private head?: Node<T>;
  private tail?: Node<T>;

  constructor() {
    this.length = 0;
    this.head = undefined;
    this.tail = undefined;
  }

  prepend(item: T): void {
    const node = { value: item } as Node<T>;

    this.length++;
    if (!this.head) {
      this.head = this.tail = node;
      return;
    }

    // Here we do double linking!!
    node.next = this.head;
    this.head.prev = node;
    this.head = node;
  }

  insert(item: T, idx: number): void {
    if (idx > this.length) {
      throw new Error("oh no!!");
    }

    // bookkeeping

    if (idx === this.length) {
      // if we are inserting at the end of the list, which basically is appending!!
      this.append(item);
      return;
    } else if (idx === 0) {
      // if we inserting at the first index, which basically is prepending!!
      this.prepend(item);
      return;
    }

    this.length++;

    // let curr = this.head;

    // // we will be traversing the list to get to that index!!
    // for (let i = 0; curr && i < idx; i++) {
    //   curr = curr.next;
    // }

    const curr = this.getAt(idx) as Node<T>;

    const node = { value: item } as Node<T>;

    // here "curr" is the node, before which we actually insert the new node

    node.next = curr;
    node.prev = curr.prev;
    curr.prev = node;

    if (node.prev) {
      node.prev.next = node;
    }
  }

  append(item: T): void {
    this.length++;

    const node = { value: item } as Node<T>;

    if (!this.tail) {
      this.head = this.tail = node;
      return;
    }

    // Here we do double linking!!
    node.prev = this.tail;
    this.tail.next = node;

    this.tail = node;
  }

  remove(item: T): T | undefined {
    let curr = this.head;

    for (let i = 0; i < this.length; i++) {
      if (curr?.value === item) {
        break;
      }
      curr = curr?.next;
    }

    // if there is no item to remove
    if (!curr) {
      return undefined;
    }

    return this.removeNode(curr);
  }

  get(idx: number): T | undefined {
    return this.getAt(idx)?.value;
  }

  removeAt(idx: number): T | undefined {
    const node = this.getAt(idx);

    if (!node) {
      return undefined;
    }

    return this.removeNode(node);
  }

  private removeNode(node: Node<T>): T | undefined {
    // bookkeeiping
    this.length--;

    if (this.length === 0) {
      const out = this.head?.value;
      this.head = this.tail = undefined;
      return out;
    }

    if (node.prev) {
      node.prev.next = node.next;
    }
    if (node.next) {
      node.next.prev = node.prev;
    }

    if (node === this.head) {
      this.head = node.next;
    }

    if (node === this.tail) {
      this.tail = node.prev;
    }

    // breaking current off!!
    node.prev = node.next = undefined;
    return node.value;
  }
  private getAt(idx: number): Node<T> | undefined {
    let curr = this.head;

    for (let i = 0; curr && i < idx; i++) {
      curr = curr.next;
    }


    return curr;
  }
}
