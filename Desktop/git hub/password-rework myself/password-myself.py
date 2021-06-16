password = 'a123456'
i = 3 #剩餘次數
while i > 0:
	i = i - 1
	userpassword = input('請輸入密碼 最多3次')
	if	userpassword == password:
		print('登入成功')
	else:
		if i > 0:
			print('密碼錯誤 還剩', i ,'次')
		else:
			print('登入失敗 帳號已鎖定')