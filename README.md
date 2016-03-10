# http-server
Http server built for python 401 (week 2)
Created by Kyle Richardson and Patrick Trompeter.

# As of 3/9/16
This server returns a response based off a clients request. At this time the server requires a GET URI HTTP/1.1 request with a Host header. If it gets that then it responds with a 200 response along with the URI. If there's any other type of request or not with all the requirements it responds with an error code of some kind.
