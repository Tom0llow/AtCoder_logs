K = int(input())

bin_str = format(K, 'b')

for i in range(len(bin_str)):
    if bin_str[i] == '1':
        bin_str = bin_str.replace(bin_str[i], '2')

ans = int(bin_str)

print(ans)
