import json
import tweepy
from optparse import OptionParser

def prettyLimits(user,oauthkeys,excludeFull):
    auth = tweepy.OAuthHandler(oauthkeys[user]['consumer_key'], oauthkeys[user]['consumer_secret'])
    auth.set_access_token(oauthkeys[user]['token'], oauthkeys[user]['secret'])
    myapi = tweepy.API(auth)
    lm = myapi.rate_limit_status()
    for x in lm['resources'].keys():
        for y in lm['resources'][x].keys():
            if (excludeFull):
                if (lm['resources'][x][y]['limit'] != lm['resources'][x][y]['remaining']):
                    print "%s - %s - limit: %d remaining: %d"%(x,y,lm['resources'][x][y]['limit'],lm['resources'][x][y]['remaining'])
            else:
                print "%s - %s - limit: %d remaining: %d"%(x,y,lm['resources'][x][y]['limit'],lm['resources'][x][y]['remaining'])


parser = OptionParser()
parser.add_option("-u", "--user",dest="user",default=False,help="User to check api limits on")
parser.add_option("-n", "--number",dest="num",default=False,help="Select user by number")
parser.add_option("-l", "--list",action="store_true",dest="lst",default=False,help="List users")
parser.add_option("-f", "--full",action="store_true",dest="fl",default=False,help="Exclude endpoints with full limits")


(options, args) = parser.parse_args()

f = file("users.json","r").read()
oauthDir = json.loads(f)

if (options.lst):
    i = 0
    for x in oauthDir.keys():
        print "%d %s"%(i,x)
        i=i+1
if (options.num):
    myuser = oauthDir.keys()[int(options.num)]
    prettyLimits(myuser,oauthDir,options.fl)
if (options.user):
    myuser = options.user
    prettyLimits(myuser,oauthDir,options.fl)
