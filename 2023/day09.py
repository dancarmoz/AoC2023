text = open('input_day09.txt').read()
nums = [map(int,x.split()) for x in text.splitlines()]

def delta_sub(lst, d = 1):
    return [y-x for x,y in zip(lst[:-d], lst[d:])]

def extr_list_easy(l):
    ll = [l]
    while not all([x==0 for x in ll[-1]]):
        ll.append(delta_sub(ll[-1]))
    return sum(y[-1] for y in ll)

solve = lambda extr_list, nums: sum(map(extr_list, nums))
assert solve(extr_list_easy, nums) == 2174807968

def extr_list_hard(l):
    ll = [l]
    while not all([x==0 for x in ll[-1]]):
        ll.append(delta_sub(ll[-1]))
    return sum((1-2*(j&1))*y[0] for j,y in enumerate(ll))

assert solve(extr_list_hard, nums) == 1208
