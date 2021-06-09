import os, uuid

ip = int(input("How many times do you want to commit? \n"))
autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system('git commit --allow-empty -m "hello {conard}"'.format(conard=uuid.uuid4()))	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push ssh://mathias_santourian@github/mathias777/how-much-time-can-you-commit master:master')