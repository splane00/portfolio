def main():
    dna = input('Enter a DNA string: ')
    
    new = ''
    for i in dna:
        if i == 'A':
            new += 'T'
        elif i == 'T':
            new += 'A'
        elif i == 'C':
            new += 'G'
        elif i == 'G':
            new += 'C'
    print(new[::-1])      

main()