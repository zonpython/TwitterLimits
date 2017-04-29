TwitterLimits
===================
A command line tool to display twitter api rate limits.

----------


Usage
-------------


	-u USER, --user=USER  User to check api limits on
	-n NUM, --number=NUM  Select user by number
	-l, --list            List users
	-f, --full            Exclude endpoints with full limits

Configuration
-------------------
Place a file called users.json in the main directory
configure it like so.

	{
	   "name1":
	          {
	          "consumer_key": "the key",
	          "consumer_secret": "the secret key",
	          "token": "token",          
	          "secret": "secret key"
	          },
	   "name2":
	          {
	          "consumer_key": "the key",
	          "consumer_secret": "the secret key",
	          "token": "token",          
	          "secret": "secret key"
	          }
	}

examples
-------------
to list all available accounts.

	python TwitterLimits.py -l
	0 user1
	1 user2
	2 user3

To get the limits for user1 using their number, and have it exclude fulled up limits.

	python TwitterLimits.py -n 0 -f
	application - /application/rate_limit_status - limit: 180 remaining: 178
	users - /users/lookup - limit: 900 remaining: 899

To get the user by their name.

	python TwitterLimits.py -u user1

