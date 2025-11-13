# n=int(input())
# arr=list(map(int,input().split()))
# for i in range(n):
#     for j in range(i,n):
#         print(*arr[i:j+1])

N = int(input())
arr = list(map(int, input().split()))

# i picks the starting index
for i in range(N):
    subarray_str = ""  # empty string for this start
    # j picks from i to N-1, extending subarray by one element each time
    for j in range(i, N):
        subarray_str += str(arr[j])  # append current element to subarray string
        print(subarray_str)  # print current subarray
