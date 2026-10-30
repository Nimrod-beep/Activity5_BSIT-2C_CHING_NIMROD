
from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def run_menu(structure, name, is_stack):

    while True:
        print("\n", name)

        if is_stack:
            print("1. Push")
            print("2. Pop")
            print("3. Peek")
        else:
            print("1. Enqueue")
            print("2. Dequeue")
            print("3. Peek Front")

        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Display Structure")
        print("0. Back")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                value = input("Enter value: ")

                if is_stack:
                    structure.push(value)
                else:
                    structure.enqueue(value)

                print("Value added.")

            elif choice == "2":
                if is_stack:
                    print("Removed:", structure.pop())
                else:
                    print("Removed:", structure.dequeue())

            elif choice == "3":
                if is_stack:
                    print("Top value:", structure.peek())
                else:
                    print("Front value:", structure.peek_front())

            elif choice == "4":
                print("Is empty:", structure.is_empty())

            elif choice == "5":
                print("Is full:", structure.is_full())

            elif choice == "6":
                print("Current state:", structure.show())

            elif choice == "0":
                break

            else:
                print("Invalid choice.")

        except (IndexError, OverflowError) as error:
            print("Error:", error)

        print("Structure state:", structure.show())


def main():

    while True:
        print("\n===== STACKS AND QUEUES =====")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            capacity = int(input("Enter capacity: "))
            stack = ArrayStack(capacity)
            run_menu(stack, "ARRAY STACK", True)

        elif choice == "2":
            stack = LinkedStack()
            run_menu(stack, "LINKED STACK", True)

        elif choice == "3":
            capacity = int(input("Enter capacity: "))
            queue = ArrayQueue(capacity)
            run_menu(queue, "CIRCULAR ARRAY QUEUE", False)

        elif choice == "4":
            queue = LinkedQueue()
            run_menu(queue, "LINKED QUEUE", False)

        elif choice == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
