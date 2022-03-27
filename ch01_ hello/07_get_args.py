#!/usr/bin/env python3
# 2. argparse를 사용해서 명령줄 인수 처리하기

import argparse

# argparse 관련 모든 코드를 별도 분리해서 get_args()에 두기
def get_args():
# 인수 전용 함수
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()
    # 인수 전달 결과를 main() 함수에 반환하기 위해 return 호출

def main():
    args = get_args()
    # get_args() 함수를 호출해서 인수를 받는데, 입력값에 문제가 없어야 한다.
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()

# $ python3 ./06_main_function.py       
# $ python3 ./06_main_function.py --name sherrys

# $ python3 -m pip install flake8 pylint
# $ python3 -m pylint 07_get_args.py
"""
************* Module 07_get_args
07_get_args.py:22:33: C0303: Trailing whitespace (trailing-whitespace)
07_get_args.py:25:0: C0304: Final newline missing (missing-final-newline)
07_get_args.py:1:0: C0103: Module name "07_get_args" doesn't conform to snake_case naming style (invalid-name)
07_get_args.py:1:0: C0114: Missing module docstring (missing-module-docstring)
07_get_args.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
07_get_args.py:14:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 4.00/10
"""

