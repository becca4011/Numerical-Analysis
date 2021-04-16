def f(x):
    return -25 + 82*x - 90*(x**2) + 44*(x**3) - 8*(x**4) + 0.7*(x**5)

def false_pos(xl, xu, es, imax, xr, iter, ea):
    fl = f(xl) # xl의 함숫값
    fu = f(xu) # xu의 함숫값

    il = 0 # xl이 연속으로 변하지 않으면 카운트
    iu = 0 # xu가 연속으로 변하지 않으면 카운트

    while True:
        xr_old = xr
        xr = xu - fu * (xl - xu) / (fl - fu) # 가위치법 공식
        fr = f(xr) # xr의 함숫값
        iter += 1 # 반복횟수 1 증가

        if xr != 0: # 0으로 나눌 수 없으므로 조건 걸기
            ea = abs((xr - xr_old) / xr) * 100.0 # 참백분율상대오차 구하기

        test = fl * fr # 두 함숫값의 부호가 다를 경우 -, 같을 경우 +
        if test < 0: # 왼쪽에 근이 있을 경우
            xu = xr # xu 변경
            fu = fr # fu의 함숫값은 fr과 같음 (xu가 xr의 값으로 변경되었기 때문)
            il += 1 # xl이 변하지 않으므로 +1
            iu = 0 # xu가 위에서 변했으므로 초기화
            if il >= 2: # xl이 2번 이상 나왔을 경우
                fl = fl / 2 # xl의 함숫값을 반으로 나눔

        elif test > 0: # 오른쪽에 근이 있을 경우
            xl = xr # xl 변경
            fl = fr
            il = 0 # xl이 위에서 변했으므로 초기화
            iu += 1 # xu가 변하지 않으므로 +1
            if iu >= 2:
                fu = fu / 2

        else: # 참근일 경우
            ea = 0
        
        if ea < es or iter >= imax: # 근사백분율상대오차가 허용오차보다 작을 경우 또는 반복횟수가 최대 반복횟수를 넘은 경우 반복 종료
            break
    
    if ea < es:
        print("수행횟수 :", iter)
        return xr
    else: # iter >= imax 조건으로 인해 반복이 종료되었을 경우
        print("근을 찾을 수 없었습니다.") # 근이 초기구간 안에 없음

k = false_pos(0.5, 1.0, 0.2, 100, 0, 0, 0)
print("근 :", k)