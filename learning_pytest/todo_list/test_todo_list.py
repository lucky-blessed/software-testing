from playwright.sync_api import sync_playwright, expect
import time 
import http.server
import socketserver
import threading
import os


#global server instance 
server = None 
server_thread = None 


def start_server(port=8000):
    # Start a HTTP server in a backgroung thread

    global server, server_thread

    # Create a HTTP sever 
    handler = http.server.SimpleHTTPRequestHandler
    server =  socketserver.TCPServer(("", port), handler)

    # Run the server daemon thread (will exit when main thread exits)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    print(f'Server is connected at http://localhost:{port}')
    time.sleep(1) # Gives the server a moment to start


def stop_server():
    global server
    if server:
        server.shutdown()
        print('Server is shutdown')


def test_add_todo_item():
    print("\n===Test: Add To-Do Item===")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=500)
        page = browser.new_page()

        # Open the app
        page.goto("http://localhost:8000")

        # Type in the task
        print("Adding new task...")
        page.get_by_test_id('todo-input').fill("Buy groceries")

        time.sleep(1)
        browser.close()

# Run out suite of test
def run_all_tests():
    try:
        pass
        # To-do implement test
    except AssertionError as e:
        print(f'Test failed: {e}')
    except Exception as e:
        print(f'An error occured: {e}')






if __name__ == "__main__":
    start_server(port=8000)

    try:
        run_all_tests()
    finally:
        stop_server()