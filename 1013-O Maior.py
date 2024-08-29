a,b,c = list(map(int,input().split()))

maiorAB = (a + b + abs(a-b)) / 2
maior = int((maiorAB + c + abs(maiorAB-c)) / 2)

print(f"{maior} eh o maior")



