#!/usr/bin/env python3
# 2. argparse를 사용해서 명령줄 인수 처리하기

import argparse

parser = argparse.ArgumentParser(description='Say hello') 
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
args = parser.parse_args()

print('Hello, ' + args.name + '!')

# $ cd ch01_hello 
# $ python3 ./05_argparse_option.py
# $ python3 ./05_argparse_option.py --name sherry

# $ python3 ./05_argparse_option.py -h // 도움말 확인
"""
usage: 05_argparse_option.py [-h] [-n name]

Say hello

optional arguments:
  -h, --help            show this help message and exit
  -n name, --name name  Name to greet                      =====> 옵션 인수
"""