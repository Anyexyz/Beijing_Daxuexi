import os
import time
import sys
from study import study

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

accounts=[('16634486740', 'Anye20031003')]
print(f'账号数量：{len(accounts)}')
successful = 0
count = 0
for username, password in accounts:
    if username=='********':
        continue
    count += 1
    print(f'--User {count}--')
    if study(username, password, ua):
        successful += 1

failed = count - successful
print('--Summary--')
print(f'成功：{successful}，失败：{failed}')
if failed != 0:
    raise Exception(f'有{failed}个失败！')