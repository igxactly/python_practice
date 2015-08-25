#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Author: Ingu Kang
#
# Python 실습 20150824월
# 다이아몬드

# 다이아몬드 스트링 생성
def strDia(sz=3):
    s = ""
    for i in range(sz * 2):
        spaces = abs(sz - i)
        stars = i if (i <= sz) else (2 * sz - i)
        s += " " * spaces + "* " * stars  + "\n"

    return s

def main():
    print("== 마지막에 출력한 것을 읽어 출력합니다 ==")
    try:
        with open('diafile.txt', 'r') as f:
            s = f.readline()
            print('가로 길이:', s)

            s = f.read()
            print(s)
    except FileNotFoundError:
        print("이전에 출력한 파일이 존재하지 않습니다.")

    print("== 새로운 다이아몬드를 생성합니다 ==")

    diaSize = 0
    cntTry = 0

    while (diaSize <= 0):
        try:
            diaSize = int(input("가로 길이 입력: " if cntTry <= 0 else "1 이상의 정수를 입력해야 합니다. 재입력: "))
        except:
            diaSize = 0
            print("입력 형식이 잘못되었습니다.")
    else:
        s = strDia(diaSize)

    print(s)

    print("== 새로운 다이아몬드를 저장합니다 ==")
    try:
        with open('diafile.txt', 'w') as f:
            f.write(str(diaSize))
            f.write(s)
            f.write("\n")
        print("diafile.txt 생성 완료")
    except:
        print("diafile.txt 생성 실패")

if __name__ == '__main__':
    main()