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
from . import exceptions
class SizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0

    def add(self, amount):
        self.size += amount
        if self.size >= self.max_size:
            raise exceptions.ResponseLimitReached("The request has reached the maximum size limit of %s" % [self.max_size])
    
    def reset(self):
        self.size = 0