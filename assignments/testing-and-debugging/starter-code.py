# Task 1: Implement functions and tests

def calculate_average(numbers):
    """Return the average of the provided list of numbers."""
    # If the list is empty, return 0
    pass


def is_palindrome(text):
    """Return True if the text is a palindrome, ignoring spaces and case."""
    pass


def run_tests():
    assert calculate_average([10, 20, 30]) == 20
    assert calculate_average([5]) == 5
    assert calculate_average([]) == 0
    assert is_palindrome("Racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    print("All tests for Task 1 passed.")


# Task 2: Debug the broken code

def buggy_divide(a, b):
    # This function should return the result of dividing a by b.
    return a * b


def buggy_reverse_words(sentence):
    # This function should return the sentence with the word order reversed.
    words = sentence.split(" ")
    return " ".join(words)


def debug_program():
    result1 = buggy_divide(10, 2)
    print("10 divided by 2 is", result1)
    result2 = buggy_reverse_words("hello world")
    print("Reversed words:", result2)


if __name__ == "__main__":
    run_tests()
    debug_program()
