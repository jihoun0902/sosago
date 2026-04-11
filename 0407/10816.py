n = int(input())
have_card = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
true_card = {}

for i in have_card:
    if i in true_card:
        true_card[i] += 1
    else : 
        true_card[i] = 1
for j in card:
    print(true_card.get(j,0),end=' ')