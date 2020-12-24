#輸入密碼驗證
password = input('請輸入密碼: ')
x = 3
while x <= 3 and x > 1:
	if password == 'a123456':
		print('登入成功')
		break
	else:
	 	x = x - 1 
	 	print('密碼錯誤，還有',x , '次機會')
	 	password = input('請輸入密碼: ')
 		
	print('你輸入超過三次')
