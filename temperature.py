tem = input('請問你要將華氏轉攝氏(F),還是攝氏轉華氏(C): ')
if tem == 'F':
	f = input('請輸入華氏溫度:')
	f = int(f)
	c = (f - 32) * 0.555
	print('相當於攝氏溫度:', c)

elif tem == 'C':
	c = input('請輸入攝氏溫度:')
	c = int(c)
	f = (c * 1.8) + 32
	print('相當於華氏溫度:', f)

#pw:0