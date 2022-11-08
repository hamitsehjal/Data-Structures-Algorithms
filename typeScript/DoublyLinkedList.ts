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

    let curr = this.head;

    // we will be traversing the list to get to that index!!
    for (let i = 0; curr && i < idx; i++) {
      curr = curr.next;
    }

    curr = curr as Node<T>;
    const node = { value: item } as Node<T>;

    // here "curr" is the node, before which we actually insert the new node

    node.next = curr;
    node.prev = curr.prev;
    curr.prev = node;

    if (curr.prev) {
      curr.prev.next = curr;
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

    // bookkeeiping
    this.length--;

    if (this.length === 0) {
      const out = this.head?.value;
      this.head = this.tail = undefined;
      return out;
    }

    if (curr.prev) {
      curr.prev = curr.next;
    }
    if (curr.next) {
      curr.next.prev = curr.prev;
      // curr.next=curr.prev --> this is primeagan code *** ask through github!!
    }

    if (curr === this.head) {
      this.head = curr.next;
    }

    if (curr === this.tail) {
      this.tail = curr.prev;
    }

    // breaking current off!!
    curr.prev = curr.next = undefined;
    return curr.value;
  }
}
