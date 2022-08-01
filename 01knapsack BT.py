W = int(input())
n = int(input())
w = input().split() 
for i in range(len(w)):
    w[i] = int(w[i])
p = input().split() 
for i in range(len(p)):
    p[i] = int(p[i])
for i in range(len(w)):
    for j in range(len(w)):
        if (p[i]/w[i])>(p[j]/w[j]):
            w[i],w[j] = w[j],w[i]
            p[i],p[j] = p[j],p[i]
maxprofit = [0]

def knapsack (i, profit, weight, maxprofit):
    if (weight<=W and profit>max(maxprofit)):
        maxprofit.append(profit)
    if (promising (i, weight, profit, maxprofit)):
        knapsack (i+1, profit+p[i+1], weight+w[i+1], maxprofit)
        knapsack (i+1, profit, weight, maxprofit)

def promising (i, weight, profit, maxprofit):
    if (weight >= W):
        return False
    else :
        j = i + 1
        bound = profit
        totweight = weight
        while (j<len(w) and totweight+w[j]<=W):
            totweight += w[j]
            bound += p[j]
            j += 1
        k = j
        if (k<len(w)):
            bound += (W-totweight*p[k]/w[k])
        return bound > max(maxprofit)
    
knapsack(-1,0,0,maxprofit)
print(max(maxprofit))