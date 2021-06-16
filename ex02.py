email = input(' メールアドレスを入力してください : ')

def check_mail(mail):
	if email.count('@')==1 and not email[0]=='@' and not email[-1]=='@' :
		flg=0
	else:
		flg = 1
	return flg

flg = check_mail(email)
if flg==0:
	print('正しいメールアドレスです')
else:
	print('何かおかしいです')