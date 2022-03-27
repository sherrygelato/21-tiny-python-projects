#!/usr/bin/env python3
# 2. argparse를 사용해서 명령줄 인수 처리하기

import argparse

parser = argparse.ArgumentParser(description='Say hello') 
# parser가 모든 인수 인지 
# description 도움말
parser.add_argument('name', help='Name to greet') 
# 인사 대상이 될 사람의 이름을 인수로 전달한다 표시
args = parser.parse_args()
# 인수를 프로그램에게 전달하라고 파서에 지시

print('Hello, ' + args.name + '!')

# $ cd ch01_hello 
# $ python3 ./04_argparse_positional.py sherry