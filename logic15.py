def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b1=a//100
    c3=a//10%10
    d2=a%100%10
    return (b1+c3+d2)%2==1
print(main(123))