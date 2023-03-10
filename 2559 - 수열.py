N,K = map(int,input().split())
temp = list(map(int,input().split()))
sum = 0
first_sum = 0
for i in range(K):
    first_sum += temp[i]
    sum += temp[i]
maxvalue = first_sum
for i in range(K,N):
    sum += temp[i] - temp[i-K]
    if sum > maxvalue:
        maxvalue = sum
print(maxvalue)