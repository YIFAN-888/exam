mail=input('メールアドレスを入力してください:')
atto='@'

def slicemail():
    findmail=mail.find(atto)
    cutmail=mail[findmail+1:]
    print(cutmail)
slicemail()