def autogen():
	try:
		users = [value]
		clear = "clear"
		os.system (clear)
		username = getpass.getpass ("[+]")
		if username in users:
			user = username
			sinput = sin.split(" ")[0]
			if sinput == "clear":
				os.system ("clear")