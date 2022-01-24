import re
import os
import csv

os.system("cls")

error = {}

try:
	with open('syslog.txt', 'r') as log:
		for line in log:
			if re.search(r"Error:", line):
				result = re.search("Error: (.*) ", line)
				error[result[1]] = error.get(result[1], 0) + 1


except Exception as E1:
	print(E1)

try:
	with open("error_logs.csv", 'w') as csvfile:
		csvfile.write("Error,Count\n")
		for key in error:
			csvfile.write("{},{}\n".format(key,error[key]))

except Exception as E2:
	print(E2)

input()
os.system('cls')