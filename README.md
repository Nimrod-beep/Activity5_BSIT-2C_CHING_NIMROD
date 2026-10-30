# Stacks and Queues

**Name:** Ching, Nimrod M.  
**Course, Year, and Section:** BSIT - 2C

## About
This project demonstrates how stacks and queues function using array and linked-list implementations. It also includes a program for checking balanced parentheses and a simulation of a printing queue.

## Project Files
- `array_stack.py` — contains the stack implementation using a fixed-size array.
- `linked_stack.py` — contains the stack implementation using linked nodes.
- `array_queue.py` — contains a circular queue using an array.
- `linked_queue.py` — contains a queue implemented with front and rear pointers.
- `main.py` — serves as the main menu for testing the four data structures.
- `balanced_parentheses.py` — checks if parentheses, brackets, and braces are properly matched.
- `print_queue.py` — simulates printing jobs based on the first-in, first-out (FIFO) rule.
- `analysis.md` — contains the written explanation for the analysis question.
- `sample_runs.md` — shows sample program outputs.

## Requirements
Make sure Python 3 is installed on your computer. The program does not require any additional libraries.

## How to Run the Programs
First, open the project folder in a terminal. To start the main program, enter:

```bash
python main.py
```

To open the balanced parentheses checker, use:

```bash
python balanced_parentheses.py
```

To run the printing queue simulation, enter:

```bash
python print_queue.py
```

## Testing the Programs
- Add more than three values to the Array Stack to test its overflow handling.
- Try removing an item from an empty stack to check its underflow handling.
- Add more than three items to the Circular Array Queue to test overflow.
- Attempt to remove an item from an empty queue to test underflow.
- Test the circular queue by adding A, B, and C, removing A and B, then adding D and E. The remaining order should be C, D, and E.
- Enter `({[]})` and `({[})` in the parentheses checker to test both balanced and unbalanced expressions.
- Add multiple printing jobs and verify that the earliest job added is processed first.

**GitHub Submission Reminder**

Upload each required file separately to your GitHub repository, following the laboratory instructions. Do not submit only a ZIP or compressed folder.
