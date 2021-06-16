# ex01.py
data=input('文字列を入力してください:')
print(len(data))




# ex02.py
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
        
        
        
# ex03.py
mail=input('メールアドレスを入力してください:')
atto='@'

def slicemail():
    findmail=mail.find(atto)
    cutmail=mail[findmail+1:]
    print(cutmail)
slicemail()


# ex04.py
user = "yoshino"
pwd = "yt1974"

username = input('IDを入力してください:')
password = input('pwdを入力してください:')

if username == user and password == pwd:
	print('OKです')
else:
	print('IDかパスワードが違います')
  
  
  
  
  # ex05.py
  def listreplace():
    list=[13,17,31,57,' ',41,83]
    list.remove(' ')
    print(list)

listreplace()
def listave():
	list=[13,17,31,57,41,83]
	ave=sum(list)/len(list)
	print(ave)
listave()
