def solve_naive():
    n = int(input().strip())
    a = list(map(int, input().split()))
    
    count = 0
    
    # Loop over all possible middle elements j
    for j in range(n):
        for i in range(n):
            if i == j:
                continue
            for k in range(n):
                if k == j or k == i:
                    continue
                # Check if a[j]^2 = a[i] * a[k]
                if a[j] * a[j] == a[i] * a[k]:
                    count += 1
    
    print(count)

def main():
    t = int(input().strip())
    for _ in range(t):
        solve_naive()

if __name__ == "__main__":
    main()
