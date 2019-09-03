"""Content of this file aim to illustrate agnostic
usage of rest API in python.

Now days they are lot of rest API application out there
the question is always what to use.

In this demo I am focussing on:
    - Django (DRF)
    - FastAPI
    - Flask
    - Falcon

Each one of them are very use and have their own use case. 
The reason why I am implementing Yara (Yet Another Rest API)
Is to show that switching from one to another because it's new
or become a brand, better or faster is not enough reason the change 
your framework.

Choosing a framework should be base on a strong.

In this example we are going to implement a Rest API
that do some simple computations and return JSON response.

In our example I can state that if we want to make simple
and just have basic rest maybe we don't even need a framework.
But if you think you might need to manage configurations, 
Databases, schedules, swagger, Admin interfaces, ... Maybe you should
Agnostic select a Framework to do so with less code writing to do
so.


We are going to use built-in python http.server
https://docs.python.org/3/library/http.server.html#module-http.server
"""

import sys
import json
from typing import Dict

from http import HTTPStatus
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

DEFAULT_PORT: int = 8000
"""Default socket bind port
"""

DEFAULT_HOST: str = "0.0.0.0"
"""Default socket bind host
"""


def yara():
    """Simple hello function returning a json string
    containing a message.
    """

    return json.dumps({"message": "Hello Yara, Yet Another Rest API"})


ROUTES: Dict[str, str] = {
        '/': yara,
        '/yara': yara,
}
"""This variable store all routes that need to be exposed
externally.

Register all routes into global variable.
You an choose to write down a decorator it maybe look fancy

Note that representation is:
    { "path": callback }

TODO: Write complex route using python "re" built-in library 
"""


class Handler(BaseHTTPRequestHandler):
    """Implement handler methods as do_GET and do_POST

    We are only going to implement do_GET.
    For more informations read;
    https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
    """

    def _headers(self,
                 status: HTTPStatus = HTTPStatus.OK,
                 content_type: str = 'application/json'):
        """Prepare response headers

        This function should be called before each response
        sent back
        """
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """This function handle all method that
        came in using a GET header
        """
        
        try:
            output = ROUTES[self.path]()
            
            self._headers()
            self.wfile.write(output.encode('utf-8'))
        except KeyError:
            """The route is not found we return a 404 error
            """
            self._headers(status=HTTPStatus.NOT_FOUND)
            return


def run(host: str, port: int):
    """This function start a ThreadingHTTPServer
    with a given HTTP Handler bind to a host and port
    """

    try:
        print(f'Server is running on {host}:{port}')
        ThreadingHTTPServer((host, port), Handler).serve_forever()
        """Et Voila!!! Our server will be serving on the given
        port and host
        """
    except KeyboardInterrupt:
        """Catch Ctrl+c
        """
        print('Server shutdown.')
        sys.exit(0)


if __name__ == "__main__":

    """The application start here
    We need to parse some with args and set some
    options for the "run" function
    """
    port = DEFAULT_PORT
    host = DEFAULT_HOST

    if len(sys.argv) > 2:
        """I have lot of servers running on my computer
        I just don't want to edit to code to change a port
        I prefer handling it via args.

        In this example let's pretend the first argument 
        WILL ALWAYS be the port and the second the host
        """
        port = int(sys.argv[0])
        host = sys.argv[1]


    if len(sys.argv) == 2:
        """This case mean we only setted the port
        """
        port = int(sys.argv[0])


    run(host, port)
    """We start our server with the given arguments
    """
