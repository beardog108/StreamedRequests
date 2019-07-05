class ResponseLimitReached(Exception):
    '''For when the response of a streamed request exceeds the max'''