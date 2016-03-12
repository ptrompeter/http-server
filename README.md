# http-server
Http server built for python 401 (week 2)
Created by Kyle Richardson and Patrick Trompeter.

# As of 3/11/16
The server can now handle specific URI requests. Parse the content of the request and attempt to open the URI locally. If the requested URI exists the sever respones with that content in bytes along with a success code. If a directory is attempted to get opened a basic html page with links to the directory's contents are is given as a response. If the request is wrong is someway an apporpiate error response is sent by the server. Such as a 404 error when the URI requested is not present on the server machine.
