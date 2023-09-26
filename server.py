# Primary References:
# - https://pythonbasics.org/webserver/
# - https://github.com/Densaugeo/uploadserver/blob/master/uploadserver/__init__.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess
import os

hostName = "localhost"
serverPort = 8080

class Server(BaseHTTPRequestHandler):
    def save_file(post_data):
        with open('uploaded_files/task.py', 'w') as file:
            # Note: I don't know the "right" way to actually parse POST request bodies...
            post_data_lines = post_data.decode().splitlines()
            file_data = ''
            parsing_body = False

            for line in post_data_lines:
                if not parsing_body and line == '':
                    parsing_body = True
                elif parsing_body and '-----------------------------' in line:
                    break
                elif parsing_body:
                    file_data += line + '\n'

            file.write(file_data)
    
    # File upload handler (via POST requests)
    def do_POST(self):
        post_data = None
        if self.path == '/upload':
            content_length = int(self.headers['Content-Length'])
            # Careful! Only read from rfile when there is content to read! Otherwise it will hang!
            post_data = self.rfile.read(content_length)
        if not post_data:
            # Note: this isn't actually a good response code
            self.send_error(400, "Couldn't read POST request body")
            return

        # Save file to local machine
        # Note: if this were called in the form 'self.save_file(...)',
        # then `self` would be passed as the first argument, so it's
        # called here as a static method of the Server class
        Server.save_file(post_data)

        # Run and collect the output of the Python script
        # Note: 100% unsecured RCE who?
        output = subprocess.run(['python', 'uploaded_files/task.py'], stdout=subprocess.PIPE)

        # Respond to client with HTTP code 201, telling them the
        # file was uploaded, and the output of the Python script
        self.send_response(201)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        # Note: writing to self.wfile writes to the response body
        self.wfile.write(output.stdout)

    # GET request handler
    def do_GET(self):
        # Note: this assumes any requested non-css
        # or javascript files are html files
        content_type = 'text/css' if self.path.endswith('.css') \
                        else 'text/javascript' if self.path.endswith('.js') \
                        else 'text/html'
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.end_headers()

        # We can't just serve the root, so '/' is manually
        # converted to 'index.html' in this ternary statement
        path = self.path if self.path != '/' else 'index.html'
        with open(os.path.basename(path), 'rb') as file:
            self.wfile.write(file.read())

# Always gets run when this script is run
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")