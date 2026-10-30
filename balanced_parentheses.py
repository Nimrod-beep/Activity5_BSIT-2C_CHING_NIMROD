
def balanced_parentheses(expression):
    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for character in expression:

        if character in "([{":
            stack.append(character)

        elif character in ")]}":

            if not stack:
                return False

            if stack[-1] != matching[character]:
                return False

            stack.pop()

    return len(stack) == 0


print("BALANCED PARENTHESES CHECKER")

expression = input("Enter an expression: ")

if balanced_parentheses(expression):
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")
