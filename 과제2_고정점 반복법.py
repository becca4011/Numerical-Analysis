def solve(a, b, c):
    r = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r

def g(x):
    #return (0.9/1.7)*(x**2) - (2.5/1.7)
    #return -2.5 / (-0.9*x + 1.7)
    return ((1.7*x + 2.5) / 0.9) ** 0.5

def fixpt(x0, es, imax, iter, ea):
    xr = x0
    while(True):
        xr_old = xr
        xr = g(xr_old)
        iter += 1
        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100.0
            
        if ea < es or iter >= imax:
            break

    if ea < es:
        r = solve(-0.9, 1.7, 2.5)
        print("반복횟수 :", iter)
        print("근 :", xr)
        print("참근 :", r)
        print("오차 :", r - xr)
    else:
        print("근을 찾을 수 없습니다.")

fixpt(5, 0.01, 20, 0, 0)