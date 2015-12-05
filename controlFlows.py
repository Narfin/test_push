# if, elif, else


def pos_neg(n):
    """Prints whether n is positive, negative, or zero."""
    if n < 0:
        print("Your number is Negative... But you already knew that.")
    elif n > 0:
        print("Your number is super positive! How nice.")
    else:
        print("Zero? Really? How boring.")


my_num = (input("Enter a number"))
pos_neg(my_num)
