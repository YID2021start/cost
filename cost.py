import codecs
import os

#讀取檔案
def read_file():
    data = []
    if os.path.isfile('stock.csv'):
        with open('stock.csv', 'r', encoding='utf_8_sig') as f:
            for line in f:
                if '公司,買入價格,賣出價格,買入成本,賣出成本' in line:
                    continue
                name, buy, sell, d, c = line.strip().split(',')
                data.append([name, buy, sell, d, c])                   
    return data            

#計算買賣成本
def count(data):
    import math
    name = input('輸入買入股票:') 
    buy = input('輸入買入金額:')
    sell = input('輸入賣出金額:')
    buy =int(buy)
    d = math.floor(buy) * 0.001425 * 0.6
    d = math.floor(d) 
    sell =int(sell)
    c = math.floor(sell) * 0.001425 * 0.6
    e = math.floor(sell) * 0.003 
    c = math.floor(c) + math.floor(e)
    print('買入成本', d,'賣出成本', c, '共計', d + c)
    data.append([name, buy, sell, d, c])
    return data

#寫入檔案
def write_file(data):
    with open('stock.csv', 'w', encoding='utf_8_sig') as f:
        f.write('公司,買入價格,賣出價格,買入成本,賣出成本\n')
        for p in data:
           f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2]) + ',' + str(p[3]) + ',' + str(p[4]) + '\n')

def main():
    data = read_file()
    data = count(data)
    write_file(data)

if __name__ == '__main__':
    	main()    

