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
import threading
from . import responsesize

def __run_callback(data, sync, callback=None):
    if callback is None: # Do nothing if there is no callback
        return
    if sync: # If synchronous (default), run callback normally
        callback(data)
    else: # If async, spawn a new thread (not good for CPU-bound cases)
        threading.Thread(target=callback, args=(data,)).start()
    
def __do_download(req, max_size, chunk_size, callback, sync):
    chunk_count = responsesize.SizeValidator(max_size) # Class to verify if the stream is staying within the max_size
    ret_data = b''
    if chunk_size == 0:
        raise ValueError("Chunk size cannot be zero")
    for chunk in req.iter_content(chunk_size=chunk_size):
        if max_size > 0:
            chunk_count.add(chunk_size)
        if not callback is None:
            __run_callback(chunk, sync, callback)
        ret_data += chunk
    if 'text' in req.headers['content-type']:
        ret_data = ret_data.decode('utf-8')
    return (req, ret_data)