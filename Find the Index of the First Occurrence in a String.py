haystack = input('Enter the haystack string: ')
needle = input('Enter the needle string: ')

n = len(haystack)
m = len(needle)

for i in range(n - m + 1):
    if haystack[i:i+m] == needle:
        print(0)
        break
else:
    print(-1)
