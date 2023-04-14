def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b=a//10
    c=a%10

    return (b+c)%2==0
print(main(64))