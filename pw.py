password = 'a123456'
times = 1
try_ = 3
while True:
	key_in = input('請輸入密碼:')
	if key_in == 'a123456':
		print('登入成功')
		break
	else:
		try_ = try_ - 1
		print('密碼錯誤! 你還有',try_ ,'次機會')
		times = times + 1
		if times == 3:
			break
