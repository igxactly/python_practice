#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Author: Ingu Kang
#
# Python 실습 20150824월
# 구구단

def main():
    print9x9()
    print9x9(19, 9)

# 'A*B=곱셈결과' 스트링 생성
def mkstr_AxB_eq_AB(a, b, llhs=1, lrhs=2):
    tmp = '{{0:{0}}}*{{1:{0}}}={{2:{1}d}}'.format(llhs, lrhs)  # 줄맞춤
    return tmp.format(a, b, a * b)

# 9x9단 출력
def print9x9(max=9, w=3):
    # max = 몇 단?
    # w = width = 가로로 몇 칸으로 출력?

    # 줄 수 칸 수 계산
    nRows = (max - 1) // w + (1 if (((max - 1) % w) > 0) else 0)
    nCols = w

    # 줄맞춤 계산
    len_lhs = len(str(max))  # 곱할 숫자의 최대 길이
    len_rhs = len(str(max ** 2))  # 곱셈 결과값의 최대 길이

    print('# ' * 15 + '#')
    print('>> {1}행{2}열로 {0}단을 출력합니다!'.format('구구' if max == 9 else max, nRows, nCols))
    print('')

    for row in range(0, nRows):  # 행별 반복

        # 행 시작 및 끝 숫자
        rowStart = 2 + nCols * row
        rowEnd = rowStart + nCols

        # 마지막 줄에서는 끝 숫자가 max보다 커지지 않도록 처리
        if rowEnd > max + 1:
            rowEnd = max + 1

        # 숫자별 max까지 작은 행 반복
        for i in range(1, max + 1):
            for a in range(rowStart, rowEnd):
                print(mkstr_AxB_eq_AB(a, i, llhs=len_lhs, lrhs=len_rhs), end='  ')
            print('')

        print('')

if __name__ == '__main__':
    main()