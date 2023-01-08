from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import time
import pyautogui

class echoHandler(BaseHTTPRequestHandler) :
    def do_GET(self):
        self.send_response(200)
        self.send_header("content=type" , "text/html")
        self.end_headers()
        # print(self.path.encode())
        if self.path.endswith("/w"):
            print("w is pressed .....")
            os.system("")
            pyautogui.keyDown('w')
            time.sleep(1)
            pyautogui.keyUp('w')
        elif self.path.endswith("/s"):
            print("s is pressed .....")
            os.system("")
            pyautogui.keyDown('s')
            time.sleep(1)
            pyautogui.keyUp('s')
        elif self.path.endswith("/a"):
            print("a is pressed .....")
            os.system("")
            pyautogui.keyDown('a')
            time.sleep(1)
            pyautogui.keyUp('a')
        elif self.path.endswith("/d"):
            print("d is pressed .....")
            os.system("")
            pyautogui.keyDown('d')
            time.sleep(1)
            pyautogui.keyUp('d')

        else :
            pass

def main():
    PORT = 8999
    server = HTTPServer(('0.0.0.0' , PORT) , echoHandler)
    print("server is running")
    server.serve_forever()

main()