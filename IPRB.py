def main():
    k, m, n = map(int, input('Enter three integers (k, m, n) separated by spaces: ').split())
    total = k + m + n
    prob = 0
    prob += k/total
    prob += m/total * (k/(total-1) + 0.75*(m-1)/(total-1) + 0.5*n/(total-1))
    prob += n/total * (k/(total-1) + 0.5*m/(total-1))
    print(prob)

main()