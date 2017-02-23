#TODO: Api things
#TODO: Fetch data
#TODO: Save them somewhere
#TODO: Count words and compare

#Api things
import re
import tweepy
c_k ="SeXL8PtmtatjcGZBMPBBG0o45"
c_s = "8IpuPbI9Ig1hiQ2db1MoSfgPPkVcTE0fr0piIxBsNVCRZk8U9G"
a_t = "603943157-OAFRe6xsKiz8akjq8vKbBhGFAVsDJLOgAwDwABji"
a_t_s = "kD0U8MaAy3wlLx91pQLCGrigz57oQecAxUhjGTicgzG7B"
auth = tweepy.OAuthHandler(c_k,c_s)
auth.set_access_token(a_t,a_t_s)
api = tweepy.API(auth)

#Fetch Data
names=[]
def TweetFetch():
    success=0
    while success==0:
        try:
                        data=""
                        print("Δωσε ενα username")
                        userid = input()
                        for status in tweepy.Cursor(api.user_timeline, id=userid, include_rts=False).items(10):
                            data = data + status.text + "\n"
                        success=1
                        names.append(userid)
                        return data;
        except tweepy.error.TweepError:
                        print("Το username δεν υπαρχει. Ξαναπροσπάθησε!")
#Save Data!
users=[]
for user in range(0,2):
	users.append(TweetFetch());
	

#Counting words
counter = []
reWord = re.compile(r"\S+")
for i in range(0,2):
	counter.append(re.findall(reWord,users[i]))

#Compare
synolo = [len(counter[0]),len(counter[1])]
if synolo[0] > synolo[1]:
	print("Ο χρήστης " + names[0] + " εχει τις περισσότερες λέξεις. Συγκεριμένα " + str(synolo[0]) + " λεξεις έναντι " + str(synolo[1]))
else:
	if synolo[0] == synolo[1]:
		print("Και οι δύο χρήστες έχουν το ίδιο σύνολο λέξεων. Συγκεκριμένα " + str(synolo[0]) + " λέξεις")
	else:
		print("Ο χρήστης " + names[1] + " εχει τις περισσότερες λέξεις. Συγκεριμένα " + str(synolo[1]) + " λεξεις έναντι " + str(synolo[0]))
