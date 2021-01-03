import time

def printLyrics():
	songLyrics = "Soles on my shoes are worn,#the knees on my jeans are torn #Sweat comin’ through my shirt,#keep pushin’ even though it hurts #Chasing what I know is true,#there’s nothing that I would not do When everyone around me drops,#I’m never gonna ever stop#I’m a man on a mission#I’m a man on a mission#I don’t need no permission#I’m a man on a mission#(Take it up now, take it up now)#I ain’t waiting and wishin’#(take it up now, take it up now)#Oh I got that ambition #(take it up now, take it up)#I’m a man on a mission"
	songSplit = songLyrics.split("#")

	for i in songSplit:
		print(i)
		time.sleep(3)

printLyrics()