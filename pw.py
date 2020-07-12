password = 'a123456'
#times = 1
try_ = 3
while try_ > 0:
	try_ = try_ - 1
	key_in = input('請輸入密碼:')
	if key_in == password:
		print('登入成功')
		break
	else:
		
		print('密碼錯誤!')
		#times = times + 1
		if try_ > 0:
			print(' 你還有',try_ ,'次機會')
