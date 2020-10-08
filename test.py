def main():
    # s = input().strip()

    s = "a  d s  f"

    i = 0
    while i < len(s):
        if s[i] == ' ':
            j = i+1
            while j == ' ':
                j += 1
            s[i+1:i+2] = s[j]
        i += 1



if __name__ == '__main__':
    main()
