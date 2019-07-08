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
import sys, os, unittest, threading, atexit
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import requests
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")
import streamedrequests

test_data_1 = 'test '*1000 + '\ntwo\n'
test_data = test_data_1 + 'test2'*1000

POST_PORT = 1337
class S(BaseHTTPRequestHandler):
    #https://gist.github.com/bradmontgomery/2219997
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        resp = "POST %s" % (test_data,)
        resp = resp.encode()
        self.wfile.write(resp)

def get_test_id():
    return str(uuid.uuid4()) + '.dat'

def setup():
    if not os.path.exists('testdata'):
        os.mkdir('testdata')
        with open('index.html', 'w') as testfile:
            testfile.write(test_data)

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('127.0.0.1', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def run_post(server_class=HTTPServer, handler_class=S):
    server_address = ('127.0.0.1', POST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def _test_callback(text):
    pass#print('got', text)

class TestInit(unittest.TestCase):

    def test_requests(self):
        if "test" not in requests.get('http://127.0.0.1:8000/').text:
            raise ValueError("test not found in test data")
        if "test" not in requests.post('http://127.0.0.1:%s' % (POST_PORT,)).text:
            print(requests.post('http://127.0.0.1:%s' % (POST_PORT,)).text)
            raise ValueError("test not found in post test data")

    def test_basic(self):
        streamedrequests.get('http://127.0.0.1:8000/')

    def test_fail(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            streamedrequests.get("http://127.0.1.1:1234")
        with self.assertRaises(requests.exceptions.ConnectionError):
            streamedrequests.post("http://127.0.1.1:1235")
        with self.assertRaises(requests.exceptions.ConnectTimeout):
            streamedrequests.get('https://1.1.1.1/', connect_timeout=0.0001)

    def test_callback(self):
        streamedrequests.get('http://127.0.0.1:8000/', chunk_size=1, callback=_test_callback)
    
    def test_async(self):
        streamedrequests.get('http://127.0.0.1:8000/', chunk_size=1, callback=_test_callback, sync=False)

    def test_zero_chunk_size(self):
        with self.assertRaises(ValueError):
            streamedrequests.get('http://127.0.0.1:8000/', chunk_size=0)
        with self.assertRaises(ValueError):
            streamedrequests.post('http://127.0.0.1:%s/' % (POST_PORT,), post_data='test', chunk_size=0)
    
    def test_post(self):
        streamedrequests.post('http://127.0.0.1:%s/' % (POST_PORT,))
        streamedrequests.post('http://127.0.0.1:%s/' % (POST_PORT,), post_data='test')

setup()
threading.Thread(target=run, daemon=True).start()
threading.Thread(target=run_post, daemon=True).start()

unittest.main()