with open("UC_network.txt", 'w') as ww:
	with open("UC_Irvine_Network.txt", 'r') as f:
		for line in f:
			l = line.split(" ")
			new_line = ' '.join([l[2], l[3]])
			ww.write(new_line + "\n")