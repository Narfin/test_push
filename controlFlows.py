# if, elif, else


def pos_neg(n):
    """Prints whether int n is positive, negative, or zero."""
    if n < 0:
        print("Your number is Negative... But you already knew that.")
    elif n > 0:
        print("Your number is super positive! How nice.")
    else:
        print("Zero? Really? How boring.")


my_num = int(input("Enter a number: "))
pos_neg(my_num)


# for


def reverse_str(word):
    """Prints word in reverse"""
    print(word[::-1], " lol")  # [begin:end:step], in this case reversing word.


my_word = input("Enter a word to flip: ")
reverse_str(my_word)


# while

x = 8
while (x != 0):
    print(x)
    x -= 1
