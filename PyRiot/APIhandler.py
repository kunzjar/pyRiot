import APIkey #APIkey is a local python file that is excluded from git which contains a single variable 'key' which is a string containing the developer's riot API key
import requests
import json

"""
builds a URL based on the type of request being made. Should return a valid URL that accesses the appropriate riot api endpoint
"""
def urlBuilder(requestInfo):

	if requestInfo['rtype'] == 'summonerid':

		return 'https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/%s?api_key=%s' % (requestInfo['summonernames'], APIkey.key)

def getSummonerId(summonernames):
	namestring = ','.join(summonernames)
	url = urlBuilder({'rtype': 'summonerid', 'summonernames': namestring})
	response = requests.get(url)
	responsedict = json.loads(response.text)
	print(responsedict['moronil'])

#temporary main function to execute for testing
if __name__ == '__main__':
	names = ['Moronil', 'Calaquendi']
	getSummonerId(names)