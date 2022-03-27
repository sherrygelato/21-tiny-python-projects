#!/usr/bin/env python3
# 2. argparse를 사용해서 명령줄 인수 처리하기

import argparse

def main():
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    args = parser.parse_args()
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
# 모든 프로그램과 모듈은 __name__이라는 변수를 통해 접근할 수 있는 이름을 가지고 있다. 
# 프로그램이 실행될 때 __name__이 '__main__'이라는 값으로 설정된다.
    main()
    # 조건이 일치하면 main() 함수를 호출한다.

# $ python3 ./06_main_function.py       
# $ python3 ./06_main_function.py --name sherry