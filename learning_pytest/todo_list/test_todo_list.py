from playwright.sync_api import Page, expect
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
    # Change the working directory of the HTML file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    # Create a HTTP sever 
    handler = http.server.SimpleHTTPRequestHandler
    server =  socketserver.TCPServer(("", port), handler)

    # Run the server daemon thread (will exit when main thread exits)
    server_thread = threading.Thread(target=server.serve_forever, daemon=True)
    server_thread.start()

    print(f'Server is connected at http://localhost:{port}')
    time.sleep(1) # Gives the server a moment to start

# Stop server
def stop_server():
    global server
    if server:
        server.shutdown()
        print('Server is shutdown')


def test_add_todo_item(page: Page):
    print('\n=== Runing test: Add To-Do Item ===')

    # Navigate to the app
    page.goto('http://localhost:8000/todo_list.html')
    print('Adding a new task...')

    # Find the input element and fill it in with new task
    page.get_by_test_id('todo-input').fill('Buy groceries')

    # Click the submit butten
    page.get_by_role("button", name="Submit").click()

    page.wait_for_timeout(500)

    # Verify that the tast appears on the UI list
    todo_items = page.get_by_test_id('todo-item')
    assert todo_items.count() == 1, "Should have 1 to-do item after adding"

    # Verify the counter update
    total_count = page.locator('#total-count').text_content()
    assert total_count == 1, f'Total count should be 1 after adding, but got {total_count}'

    print("Task added succefully!")

    page.wait_for_timeout(500)

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