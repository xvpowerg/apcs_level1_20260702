def fac_rec(n):
    if n == 1:
        return 1
    else:
       return n *  fac_rec(n-1)

print(fac_rec(5))
