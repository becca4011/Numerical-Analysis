from fractions import Fraction

def g(x):
    return Fraction((-9)*(x**2) + 17*x + 25, 10)

def fixpt(x0, es, imax, iter, ea):
    xr = x0
    while(True):
        xr_old = xr
        xr = g(xr_old)
        iter += 1
        if xr != 0:
            ea = Fraction(abs(Fraction(xr - xr_old, xr)) * 1000, 10)
            
        if ea < es or iter >= imax:
            break

        print("xr :", xr)
        print("xr_old :", xr_old)
        print("ea :", ea)
        print()

    if ea < es:
        print(xr)
    else:
        print("근을 찾을 수 없습니다.")

fixpt(5, Fraction(1, 100), 10, 0, 0)