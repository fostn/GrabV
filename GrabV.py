import os,random
try:	
	import requests
	from bs4 import BeautifulSoup
	import re
	import json
except ModuleNotFoundError:
	os.system("pip install requests")
	os.system("pip install regex")
	os.system("pip install bs4")

def wproxy():
	print("[1]twitter\n[2]tiktok\n[3]instagram")
	def twitter():
		file_pro = input('Enter the proxies file name : ')
		list_proxies = []
		for P in open(file_pro, "r").read().splitlines():
			list_proxies.append(P)
		
		vverified = 0 
		uverified = 0 
		notfound = 0
		
		accounts = input("enter usernames file : ")
		for users in open(accounts,"r").read().splitlines():		
			try:
				
				proxy = str(random.choice(list_proxies))
				proxies = {"http":f"http://{proxy}","https":f"https://{proxy}"}			
				user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js' }
				url = "https://twitter.com/home?precache=1"
				r_token = requests.get(url, headers=user_agent,proxies=proxies,timeout=4)
				soup = BeautifulSoup(r_token.text, "html.parser")	
				token = re.findall(r'"gt=\d{19}', str(soup.find_all('script')[-1]), re.IGNORECASE)[0].replace("\"gt=","")
				url2 = f"https://mobile.twitter.com/i/api/graphql/gr8Lk09afdgWo7NvzP89iQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22{users}%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D"
				headers = {"x-csrf-token":"192e8d70a4b47525f760b6ab4d7179c7","User-Agent":"Mozilla\/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/14.0.3 Mobile\/15E148 Safari\/604.1","Accept-Encoding":"gzip, deflate, br","x-guest-token":token,"Cookie":"missing","Accept-Language":"en-us","x-twitter-active-user":"yes","Accept":"*\/*","Connection":"keep-alive","Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA","Content-Type":"application\/json","x-twitter-client-language":"en","Host":"mobile.twitter.com"}
					
				try:
					r = requests.get(url2,headers=headers,proxies=proxies,timeout=4).json()
					try:
						verified = r["data"]["user"]["result"]["legacy"]["verified"]
						if verified == True:		
							print(f"verified : {users}")
							#print(proxy)
							with open("twitter_verified.txt","a")as f:
								f.write(users+"\n")
							
							vverified = vverified +1
						elif verified == False:
							print(f"uverified : {users}")
							uverified = uverified +1 
					except Exception:
						print(f"{users} not found")
						notfound = notfound +1
				
				except Exception as e:
					pass
				
			except Exception as f:
				print(f"bad proxy : {proxy}")
			
		print("-"*40)
		print(f"verified[{vverified}] |uverified[{uverified}]")
		if vverified > 0:		
			print("file successfully saved as twitter_verified.txt")
		print("-"*40)
	
	def tiktok():
		v = 0 
		unv = 0
		file_pro = input('Enter the proxies file name : ')
		list_proxies = []
		for P in open(file_pro, "r").read().splitlines():
			list_proxies.append(P)
		file = input("enter usernames file : ")
		for username in open(file,"r").read().splitlines():
			proxy = str(random.choice(list_proxies))
			proxies = {"http":f"http://{proxy}","https":f"https://{proxy}"}
			
			url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"
			headers = {
				"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
				"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
				"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
			}
			try:
				
				r = requests.get(url,headers=headers,proxies=proxies,timeout=4).json()
				try:	
					custom_verify = r["data"]["custom_verify"]
					print(f"{username} : verified ")
					with open("tiktok_verified.txt","a")as f:
						f.write(username+"\n")
					v=v+1
				except KeyError:
					try:
						verify = r["data"]["enterprise_verify_reason"]	
						print(f"{username} : verified")
						v=v+1
						with open("tiktok_verified.txt","a")as f:
							f.write(username+"\n")
						
					except KeyError:
						print(f"{username} : uverified")
						unv=unv+1
			except requests.ConnectionError as e:
				print(f"bad proxy : {proxy}")
				
			except Exception as e:
				print(f"error : {username}") 
				print(e)
		
		print("-"*40)
		print(f"verified [{v}]| uverified [{unv}]")
		if v > 0:
			print("file successfully saved as tiktok_verified.txt")
		print("-"*40)
	
	def insta():
		verified = 0
		unverified = 0
		Proxies_File = input('Enter the proxies file name : ') 
		users_f = input("enter usernames file : ")	
		list_proxies = []
		for P in open(Proxies_File, "r").read().splitlines():
			list_proxies.append(P)
		for accounts in open(users_f,"r").read().splitlines():
			try:
				
				url = f"https://us-central1-newinsta-b23fb.cloudfunctions.net/profile?username={accounts}"
				proxy = str(random.choice(list_proxies))
				proxies = {"http":f"http://{proxy}","https":f"https://{proxy}"}
					
				r = requests.get(url,proxies=proxies,timeout=4).json()
				if 'graphql' in r:
					if r["graphql"]["user"]["is_verified"] == True:
						verified = verified +1
						with open("insta_verified.txt","a")as f:
							f.write(accounts+"\n")					
						
						print(f"{accounts} : verified ")
					elif r["graphql"]["user"]["is_verified"] == False:
						print(f"{accounts} : unverified ")
						unverified=unverified+1
						
					
				else:
					print(r)
					print("username not found")
			except requests.ConnectionError as e :
				print(f"bad proxy {proxy}")
		print("-"*40)
		print(f"verified [{verified}] | unverified [{unverified}]")
		if verified > 0:
			print("file successfully saved as insta_verified.txt")
		print("-"*40)
	choice = input("Enter number of application : ")
		
	if choice == "1":
		twitter()
	elif choice == "2":
		tiktok()
	elif choice == "3":
		insta()
	else:
		print("Exit")
		pass
#wproxy()
#===========#===========#===========#=======#
def noproxy():	
	print("[1]twitter\n[2]tiktok\n[3]instagram")
	def twitter():
		vverified = 0 
		uverified = 0 
		notfound = 0
		
		accounts = input("enter usernames file : ")
		try:
			
			for users in open(accounts,"r").read().splitlines():
				
				user_agent = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'Referer' : 'https://twitter.com/sw.js' }
				url = "https://twitter.com/home?precache=1"
				r_token = requests.get(url, headers=user_agent)
				soup = BeautifulSoup(r_token.text, "html.parser")	
				token = re.findall(r'"gt=\d{19}', str(soup.find_all('script')[-1]), re.IGNORECASE)[0].replace("\"gt=","")
				url2 = f"https://mobile.twitter.com/i/api/graphql/gr8Lk09afdgWo7NvzP89iQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22{users}%22%2C%22withSafetyModeUserFields%22%3Atrue%2C%22withSuperFollowsUserFields%22%3Atrue%7D"
				headers = {"x-csrf-token":"192e8d70a4b47525f760b6ab4d7179c7","User-Agent":"Mozilla\/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit\/605.1.15 (KHTML, like Gecko) Version\/14.0.3 Mobile\/15E148 Safari\/604.1","Accept-Encoding":"gzip, deflate, br","x-guest-token":token,"Cookie":"missing","Accept-Language":"en-us","x-twitter-active-user":"yes","Accept":"*\/*","Connection":"keep-alive","Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA","Content-Type":"application\/json","x-twitter-client-language":"en","Host":"mobile.twitter.com"}
					
				try:
					r = requests.get(url2,headers=headers).json()
					try:
						verified = r["data"]["user"]["result"]["legacy"]["verified"]
						if verified == True:		
							print(f"verified : {users}")
							with open("twitter_verified.txt","a")as f:
								f.write(users+"\n")
							
							vverified = vverified +1
						elif verified == False:
							print(f"uverified : {users}")
							uverified = uverified +1 
					except Exception:
						print(f"{users} not found")
						notfound = notfound +1
				
				except Exception as e:
					pass
				
		except FileNotFoundError as f:
			print(f)
		print("-"*40)
		print(f"verified[{vverified}] |uverified[{uverified}]")
		if vverified > 0:
			print("file successfully saved as twitter_verified.txt")
		print("-"*40)
		
	def insta():
		verified = 0 
		uverified = 0
		users_f = input("enter usernames file : ")
		for accounts in open(users_f,"r").read().splitlines():
			try:
				
				url = f"https://us-central1-newinsta-b23fb.cloudfunctions.net/profile?username={accounts}"
				r = requests.get(url).json()
				if 'graphql' in r:
					if r["graphql"]["user"]["is_verified"] == True:
						verified = verified +1
						with open("insta_verified.txt","a") as f:
							f.write(accounts+"\n")														
		
						print(f"{accounts} : verified ")
					
					elif r["graphql"]["user"]["is_verified"] == False:
						print(f"{accounts} : uverified ")
						uverified = uverified +1
					
				elif 'graphql' not in r:
					print(r)
				else:
					print(r)
			except Exception as e :
				print(f"username {accounts} not found")
		print("-"*40)
		print(f"verified [{verified}]| uverified [{uverified}]")
		if verified > 0:
			print("file successfully saved as insta_verified.txt")
		print("-"*40)
	def tiktok():
		v = 0 
		unv = 0
		file = input("enter usernames file : ")
		for username in open(file,"r").read().splitlines():
			
			url = f"https://tiktok-best-experience.p.rapidapi.com/user/{username}"
			headers = {
				"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
				"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
				"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
			}
			try:
				
				r = requests.get(url,headers=headers).json()
				try:	
					custom_verify = r["data"]["custom_verify"]
					print(f"{username} : verified ")
					with open("tiktok_verified.txt","a")as f:
						f.write(username+"\n")
					v=v+1
				except KeyError:
					try:
						verify = r["data"]["enterprise_verify_reason"]	
						print(f"{username} : verified")
						v=v+1
						with open("tiktok_verified.txt","a")as f:
							f.write(username+"\n")
						
					except KeyError:
						print(f"{username} : uverified")
						unv=unv+1
			except Exception:
				print(f"error : {username}") 
		print("-"*40)
		print(f"verified [{v}]| uverified [{unv}]")
		if v > 0:
			print("file successfully saved as tiktok_verified.txt")
		print("-"*40)
	
	choice = input("Enter number of application : ")
		
	if choice == "1":
		twitter()
	elif choice == "2":
		tiktok()
	elif choice == "3":
		insta()
	else:
		print("Exit")
		pass
print("""
  ___  ____    __    ____  _  _ 
 / __)(  _ \  /__\  (  _ \( \/ )
( (_-. )   / /(__)\  ) _ < \  / 
 \___/(_)\_)(__)(__)(____/  \/  
""")
print("-"*40)
print("grab verified accounts | iG f09l")
print("-"*40)
print("[1]with proxies\n[2]without proxies")
choice = input("choice your opinion : ")
if choice == "1":
	print("-"*40)
	print("proxies on")
	print("-"*40)
	wproxy()
elif choice == "2":
	print("-"*40)
	print("proxies off")
	print("-"*40)
	noproxy()
	
else:
	print("Exit")
	pass
