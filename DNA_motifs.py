def main():
    with open("s.txt", "r") as s_file, open("t.txt", "r") as t_file:
        s = s_file.read().strip()
        t = t_file.read().strip()

        indices = []
        start = 0
        while True:
            index = s.find(t, start)
            if index == -1:
                break
            indices.append(index + 1)  # convert to 1-based
            start = index + 1

        print("Found at indices:", *indices)

main()
