
import urllib2, json

class Api:

	base_url = 'http://api.ponup.com'

	def set_base_url( self, base_url ):
		self.base_url = base_url

	def get_base_url( self ):
		return self.base_url

	def retrieve_games( self ):
		url = self.base_url + '/game/list'
		text = urllib2.urlopen( url ).read()
		return json.loads( text )

	def retrieve_scores( self, game_name, limit = 10 ):
		url = self.base_url + '/score/list?game_name=%s&limit=%d' % ( game_name, limit )
		text = urllib2.urlopen( url ).read()
		return json.loads( text )


