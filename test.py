import argparse
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory

app = Flask(__name__)


def start():

    from startmoieintry import Entry
    mo=Entry.open(getentry=True)
    
app.add_url_rule('/tool', 'webio.view', webio_view(start)
                 , methods=['GET', 'POST', 'OPTIONS'])



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()
    start_server(start, port=args.port,debug=True,max_payload_size='10000000',reconnect_timeout=4)
