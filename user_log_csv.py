import re
import os
import csv

os.system('cls')

user_statistics = {}

try:
	with open('syslog.txt', 'r') as log:
		for line in log:
			result = re.search(r"\((.*)\)", line)
			if result[1] not in user_statistics:
				user_statistics[result[1]] = {}
				user_statistics[result[1]]["Info"] = user_statistics[result[1]].get("Info", 0)
				user_statistics[result[1]]["Error"] = user_statistics[result[1]].get("Error", 0)
			if re.search(r"Error:", line):
				user_statistics[result[1]]["Error"] = user_statistics[result[1]].get("Error", 0) + 1
			elif re.search(r"Info:", line):
				user_statistics[result[1]]["Info"] = user_statistics[result[1]].get("Info", 0) + 1

except Exception as E1:
	print(E1)

try:
	with open("user_statistics.csv", 'w') as csvfile:
		csvfile.write("User,Info,Error\n")
		for key in user_statistics:
			csvfile.write("{},{},{}\n".format(key,user_statistics[key]["Info"],user_statistics[key]["Error"]))

except Exception as E2:
	print(E2)

input()
os.system('cls')