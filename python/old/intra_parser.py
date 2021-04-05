import intra_data as intra
import time
import json

def export_names_to_file(filename: str, names: list, appendix=False):
	if appendix:
		f = open(filename, 'wa')
	else:
		f = open(filename, 'w')
	
	for name in names:
		f.write(name)
		f.write("\n")

	f.close()

def import_names_fr_file(filename: str) -> []:
	f = open(filename, 'r')
	names = []

	for line in f:
		line = line.strip('\n')
		if len(line) != 0:
			names.append(line)
	return names

def download_users_json(filename: str, names: list, shift: float, debug: bool = True, appendix: bool = False):
	users = []
	count = 1
	all_users = len(names)

	if appendix:
		f = open(filename, 'wa')
	else:
		f = open(filename, 'w')

	for name in names:
		if debug:
			print('{0}/{2}: {1}'.format(count, name, all_users))
		time.sleep(shift)
		users.append(intra.get_user_data(name))
		count += 1

	if debug:
		print('EXPORTING TO FILE')

	json.dump(users, f)
	f.close()

def import_users_json(filename: str) -> []:
	with open(filename, "r") as file:
		return json.load(file)

def urangs_from_users(bdata: list) -> []:
	lvl_usr = []

	for user_data in bdata:
		curse_info = user_data['cursus_users']
		if len(curse_info) != 0:
			curse_info = curse_info[0]
			user_level = curse_info['level']
			user_login = curse_info['user']['login']
			lvl_usr.append((user_level, user_login))
	lvl_usr.sort()
	lvl_usr.reverse()
	return lvl_usr

def import_urangs_json(filename: str) -> []:
	BIG_DATA = import_users_json(filename)
	lvl_usr = []

	for user_data in BIG_DATA:
		curse_info = user_data['cursus_users']
		if len(curse_info) != 0:
			curse_info = curse_info[0]
			user_level = curse_info['level']
			user_login = curse_info['user']['login']
			lvl_usr.append((user_level, user_login))
	lvl_usr.sort()
	lvl_usr.reverse()
	return lvl_usr

def export_urangs_file(filename: str, rangs: list):
	with open(filename, "w") as file:
		for usr_rang in rangs:
			file.write("{:=2.3} lvl: {}\n".format(usr_rang[0], usr_rang[1]))
