def main():
    # print integers from 11 to 20 on the same line with spacing
    for i in range(11,21):
    # align each number with spaces
        print(f"{i:<4}", end='')
    print ()

    # print squures of integers from 11 to 20 on the next line
    for i in range(11, 21):
    # align each number with spaces
        print(f"{i * i:<4}", end='')
    print ()
if __name__ == "__main__":
    main()