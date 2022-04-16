import socketserver
import SimpleHTTPServer

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHAndler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("Serving at port ", PORT)
httpd.serve_forever()
