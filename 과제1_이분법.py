def f(x):
    return -25 + 82*x - 90*(x**2) + 44*(x**3) - 8*(x**4) + 0.7*(x**5)

def bisect(xl, xu, es, imax, xr, iter, ea):
    fl = f(xl) # xl의 함숫값

    while True:
        xr_old = xr
        xr = (xl + xu) / 2 # xr을 구간의 반으로 함
        fr = f(xr)
        iter += 1 # 반복횟수 증가

        if xr != 0:
            ea = abs((xr - xr_old) / xr) * 100.0

        test = fl * fr
        if test < 0: # 근이 왼쪽에 있는 경우
            xu = xr # 상한값을 xr로 바꿈
        elif test > 0: # 근이 오른쪽에 있는 경우
            xl = xr # 하한값을 xr로 바꿈
            fl = fr
        else: # 참근일 경우
            ea = 0 # 오차가 없으므로 0
        
        if ea < es or iter >= imax:
            break
    
    if ea < es:
        print("수행횟수 :", iter)
        return xr
    else:
        print("근을 찾을 수 없었습니다.")

k = bisect(0.5, 1.0, 10.0, 100, 0, 0, 0)
print("근 :", k)