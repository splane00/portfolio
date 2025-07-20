def main():
    string = input("Enter a DNA string: ")
    new_string = ''
    for s in string:
        if s == 'T':
            new_string += 'U'
        else:
            new_string += s
    print(new_string,end='')

main()
