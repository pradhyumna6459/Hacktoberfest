'''
Chef owns an icecream shop in Chefland named scoORZ. There are only three types of coins in Chefland: Rs. 5, Rs. 10 and Rs. 15. An icecream costs Rs. 5.

There are N people (numbered 1 through N) standing in a queue to buy icecream from scoORZ. Each person wants to buy exactly one icecream. For each valid i, the i-th person has one coin with value ai. It is only possible for someone to buy an icecream when Chef can give them back their change exactly ― for example, if someone pays with a Rs. 10 coin, Chef needs to have a Rs. 5 coin that he gives to this person as change.

Initially, Chef has no money. He wants to know if he can sell icecream to everyone in the queue, in the given order. Since he is busy eating his own icecream, can you tell him if he can serve all these people?
'''
# cook your dish here
def algo(a, n):
    p = []
    p.append(0)
    if a[0] != 5:
        return "NO"
    else:
        p.append(a[0])
        s = 0
        for i in range(1, n):
            p.append(a[i])
            q = a[i] - 5
            if q in p:
                s = s + 1
                if q !=0:
                    p.remove(q)
            elif q==10 and p.count(10)==0:
                if p.count(5)>=2:
                    s=s+1
                    p.remove(5)
                    p.remove(5)

        if s == len(a) - 1:
            return "YES"
        else:
            return "NO"



for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(algo(a, n))
