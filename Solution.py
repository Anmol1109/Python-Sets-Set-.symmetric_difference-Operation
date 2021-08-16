# Enter your code here. Read input from STDIN. Print output to STDOUT
n1 = int(input())
E  = set(input().split())
n2 = int(input())
F  = set(input().split())

print(len(E ^ F))
