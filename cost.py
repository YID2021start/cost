#計算買賣成本
def count():
	data = []
	import math
	name = input('輸入買入股票:') 
	buy = input('輸入買入金額:')
	buy =int(buy)
	d = math.floor(buy) * 0.001425
	d = math.floor(d) 
	sell = input('輸入賣出金額:')
	sell =int(sell)
	c = math.floor(sell) * 0.001425 
	e = math.floor(sell) * 0.003 
	c = math.floor(c) + math.floor(e)
	print('買入成本', d,'賣出成本', c, '共計', d + c)
	data.append([name,buy, sell, d, c])
	return data
data = count()