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
import requests
from . import exceptions, dodownload, setuptimeout
def post(url, post_data=None, request_headers=None, sync=True, 
    max_size=0, chunk_size=1000, connect_timeout=60, stream_timeout=0,
    proxy={}, callback=None, allow_redirects=True):

    timeouts = setuptimeout.__setup_timeout(connect_timeout, stream_timeout)
    
    req = requests.post(url, data=post_data, headers=request_headers,
        timeout=timeouts, stream=True, allow_redirects=allow_redirects, proxies=proxy)
    
    return dodownload.__do_download(req, max_size, chunk_size, callback, sync)