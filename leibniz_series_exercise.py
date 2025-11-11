def approximate_pi(n_terms):
    x = 0
    for i in range(0, n_terms):
        n= (-1)** i/(2*i+1)
        x= x+n
    y = 4*x
    return y
