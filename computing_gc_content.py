def main():
     with open("dna.txt", "r") as f:
        dna = f.read()
        parts = dna.split(">")  # divide into competing datasets

        for i in parts:
            if i.strip() == "":
                continue  # skip empty first split if present

            header = i[:13]
            sequence = i[13:]  # skip the header
            gc_count = 0

            for char in sequence:
                if char == 'C' or char == 'G':
                    gc_count += 1

            length = len(sequence)
            gc_per = (gc_count / length) * 100
            print(header, gc_per)

main()
