'''
    StreamedRequests. A simple library for streaming HTTP requests
    Copyright (C) 2019 Kevin Froman https://chaoswebs.net/

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import sys, os, unittest
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import streamedrequests

def get_test_id():
    return str(uuid.uuid4()) + '.dat'

def _test_callback(text):
    print('got', text)

class TestInit(unittest.TestCase):

    def test_basic(self):
        streamedrequests.get('https://example.com/')

    def test_callback(self):
        pass
        streamedrequests.get('https://example.com/', chunk_size=1, callback=_test_callback)
    
    def test_async(self):
        streamedrequests.get('https://example.com/', chunk_size=1, callback=_test_callback, sync=False)

    def test_zero_chunk_size(self):
        try:
            streamedrequests.get('https://example.com/', chunk_size=0)
        except ValueError:
            pass
        else:
            self.assertTrue(failUnless)

unittest.main()