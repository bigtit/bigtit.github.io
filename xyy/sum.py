import sys

lines = sys.stdin.read().split('\n')

def todouble(str):
    try:
        return float(str)
    except:
        return 'NaN'

total = 0
for line in lines:
    subtotal = line.split('=')[-1]
    subtotal = todouble(subtotal)
    if subtotal == 'NaN':
        print('可能的数值错误')
        continue
    print(subtotal)
    subtotal = int(subtotal*1000)
    total = total + subtotal

total = total/1000

print('total={}'.format(total))
