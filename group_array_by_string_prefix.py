test_list = ['code1', 'code2', 'code2a', 'code2c', 'code3'] 
test_results = ['OK', 'Wrong', 'Runtime', 'OK', 'Runtime'] 
groups = {}
groups_final = {}
character_count = 0
item_count = 0
total_score = 0
category_score = 0
minlen = min(len(x) for x in test_list)

while character_count < minlen:
	item_count = 0
	for t in test_list:
		if t[:(character_count+1)] not in groups.keys():
			groups[t[:(character_count+1)]] = []
		groups[t[:(character_count+1)]].append({t:test_results[item_count]})
		item_count = item_count + 1
	character_count = character_count + 1

for k in groups.keys():
	if len(k) < minlen:
		pass
	else:
		groups_final[k] = groups[k]

print(groups_final)
for g in groups_final.keys():
	for gg in groups_final[g]:
		category_score = 1
		for ggg in gg.keys():
			if gg[ggg] == "Wrong" or gg[ggg] == "Runtime":
				category_score = 0
	total_score = total_score + category_score
			

print("final score is {0}%".format(str(round(total_score*100/len(groups_final)))))
