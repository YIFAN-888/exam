# ex01.py
data=input('文字列を入力してください:')
print(len(data))




# ex02.py
import re
data = re.compile(r"[a-z][^@].com")
emails=input('文字列を入力してください:')

for i in emails:
    if not data.match(i):
        print(i,'正しいメールアドレスです')
    else:
        print(i,'何かおかしいです')
        
        
        
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
