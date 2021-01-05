def main():

    length = int(input("Enter the password length : "))

    import string
    import random

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = string.hexdigits

    s = [s1, s2, s3, s4, s5]

    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    s.extend(list(s5))

    random.shuffle(s)

    print("Your password is\n")
    print("".join(s[0:length]))
    

main()