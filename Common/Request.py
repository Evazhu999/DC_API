import requests
headers = {'user-agent': 'my-app/0.0.1'}
data={"mobile":"917838381868","phone_code":91}
data1={
	"mobile":"917838381868",
	"code":"123456",
	"phone_code":"91"
}
apply= requests.get('http://10.10.10.132:12000/api/apply',headers=headers)
sms= requests.post('http://10.10.10.132:12000/api/auth/sms',data=data)
login= requests.post('http://10.10.10.132:12000/api/login',data=data1)

print(apply.text)
print(sms.text)
print(sms.status_code)
print(login.text)

s = 'python'
print(s [::-1])#第一种方式
l = list(s)
l.reverse()
print(''.join(l))#第二种方式
