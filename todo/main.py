from http.server import BaseHTTPRequestHandler, HTTPServer
import json


tasks = [{"id":1,"title": "this is title", "description":"this is description"},
         {"id":2,"title": "this is title 2", "description":"this is description 2"}]

class HTTPRequestHandler(BaseHTTPRequestHandler):
    def send__response(self,status_code, data = None):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if data:
            self.wfile.write(json.dumps(data).encode("utf-8"))
        
    def do_GET(self):
        if self.path == "/todos":
            self.send__response(200, tasks)
        elif self.path.startswith("/todos/"):
            todo_id = int(self.path.split("/")[-1])
            todo = next((t for t in tasks if t["id"] == todo_id), None)
            if todo:
                self.send__response(200, todo)
            else:
                self.send__response(404, {"message": "Not Found"})
        else:
            self.send__response(404, {"message": "Invalid ID"})
    
    def do_POST(self):
        if self.path == "/todos":
            length = int(self.headers["Content-Length"])
            post = json.loads(self.rfile.read(length))
            unused_id = max([task["id"] for task in tasks]) + 1
            post["id"] = unused_id
            tasks.append(post)
            self.send__response(201, {"message": "Created ToDo"})
        else:
            self.send__response(404, {"message": "Invalid ID"})

if __name__ == "__main__":
    address = ("", 8000)
    http_server = HTTPServer(address, HTTPRequestHandler)
    print("Server is Running")
    http_server.serve_forever()