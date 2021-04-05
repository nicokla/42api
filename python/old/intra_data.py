# import intra_data as fr_42
# fr_42.configure(uid, secret)
# fr_42.auth_token()
# # fr_42.__token
# aaa = fr_42.get_user_data('nklarsfe')
# print(aaa)

import requests
import time

__API_INTRA_HTTPS: str = 'https://api.intra.42.fr/'

def _print_token_data():
	print('UID: {}'.format(__client_id))
	print('SECRET: {}'.format(__client_secret))
	print('TOKEN: {}'.format(__token))

def	configure(uid: str, secret: str, token: str = None):
	global __token
	global __client_id
	global __client_secret
	__token = token
	__client_id = uid
	__client_secret = secret

def auth_token():
	global __token
	global __client_id
	global __client_secret
	if __client_id is None or __client_secret is None:
		raise RuntimeError("Intra UID and SECRET is not configured!\nCall intra.configure()")
	payload = {
		'grant_type': 'client_credentials',
		'client_id': __client_id,
		'client_secret': __client_secret
	}

	r = requests.post(__API_INTRA_HTTPS + 'oauth/token', data=payload)
	if r.status_code != requests.codes.ok:
		raise RuntimeError("Token doesn't initialized: Network_fail: {}".format(r.status_code))
	__token = r.json()['access_token']

def get_user_data(login: str) -> {}:
	global __token
	auth_token()
	if __token == None:
		raise RuntimeError("Token has not been generated! Use auth_token()")
	headers = {'Authorization': 'Bearer {}'.format(__token)}
	r = requests.get(__API_INTRA_HTTPS + 'v2/users/' + login, headers=headers)
	if r.status_code != requests.codes.ok:
		raise RuntimeWarning("Not OK: user='{}'".format(login))
	return (r.json())

def get_piscinec_filters(year: str = '2019', monthes: str = 'june', shift: int = 0) -> []:
	global __token
	auth_token()
	if __token == None:
		raise RuntimeError("Token has not been generated! Use auth_token()")
	headers = {
		'Authorization': 'Bearer {}'.format(__token)
		}
	params = {
		'filter[pool_year]': year,
		'filter[pool_month]': monthes,
		'filter[primary_campus_id]': '1',
		'page[number]': '0',
		'page[size]': '100'
	}
	names = []
	while True:
		params['page[number]'] = str(int(params['page[number]']) + 1)
		r = requests.get(__API_INTRA_HTTPS + 'v2/users', params=params, headers=headers)
		if shift != 0:
			time.sleep(float(shift))
		if r.status_code != requests.codes.ok:
			break
		json_data_object = r.json()
		for usr_obj in json_data_object:
			names.append(usr_obj['login'])
		if len(json_data_object) != 100:
			break
	return (names)

# month='september'
# allStuds = fr_42.get_piscinec_filters(monthes=month)
# myIterator = filter(lambda stud: stud[0] != '3', allStuds)
# selectedStuds = list(myIterator)
