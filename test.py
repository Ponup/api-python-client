
import ponup
import unittest

class TestStringMethods( unittest.TestCase ):

    def setUp( self ):
        self.api = ponup.Api()

    def test_base_url( self ):
        self.assertEqual( 'http://api.ponup.com', self.api.get_base_url() )

    def test_return_type( self ):
        games = self.api.retrieve_games()
        self.assertIsInstance( games, list )

if __name__ == '__main__':
    unittest.main()

