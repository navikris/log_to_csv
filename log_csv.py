import re
import os
import csv

os.system('cls')

user_statistics = {}
error_statistics = {}

errorfile = 'error_logs.csv'
userfile = "user_statistics.csv"

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
			if re.search(r"Error:", line):
				error = re.search("Error: (.*) ", line)
				error_statistics[error[1]] = error_statistics.get(error[1], 0) + 1

except Exception as E1:
	print(E1)

try:
	with open(userfile, 'w') as csvfile:
		csvfile.write("User,Info,Error\n")
		for key in user_statistics:
			csvfile.write("{},{},{}\n".format(key,user_statistics[key]["Info"],user_statistics[key]["Error"]))

except Exception as E2:
	print(E2)

try:
	with open(errorfile, 'w') as csvfile:
		csvfile.write("Error,Count\n")
		for key in error_statistics:
			csvfile.write("{},{}\n".format(key,error_statistics[key]))

except Exception as E3:
	print(E3)

input()
os.system('cls')