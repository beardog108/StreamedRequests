# StreamedRequests

[![Build Status](https://travis-ci.org/beardog108/StreamedRequests.svg?branch=master)](https://travis-ci.org/beardog108/StreamedRequests)

Python module to stream HTTP requests in order to ensure content length sanity.

# Install

`$ pip install StreamedRequests`

# Basic Usage

```
from streamedrequests import get, post

def my_func(data):
    # prints every 5 bytes of data from site
    print(data)

get('https://example.com/', callback=my_func, chunk_size=5)
```

sync: bool (default True) when set to false creates and starts a new thread for streaming

request_headers param can be used to set req headers

post() is the same, but use post_data to set request body.


# Contact

https://chaoswebs.net/