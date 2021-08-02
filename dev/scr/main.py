try:
    import os,time #Non install
    import asyncio, websockets, ait #Install

    import pynput.mouse as mouse
    from pynput import keyboard
except ImportError:
    dep = ["asyncio","websockets","autoit","pynput"] #For every dep added put it in this list
    print("Import error\nDownloading dependencies")
    time.sleep(3)
    for i in dep:
        os.system(f"cmd /c pip install {i}")

#Info
__version__ = "1.0.2"
__devURL__  = "https://github.com/The-Glit-ch"

#YOU CAN CHANGE ME
PORT = 6969 #Can be replaced with a custom port number
LeftClickButton = "q" #Can be changed to other keys. Try to stick letters
RightClickButton = "e" #Can be changed to other keys. Try to stick letters

#Vars
ms = mouse.Controller()

async def main(websocket, path):
    print("Device connected")
    async for message in websocket:
        Pos = str(message).replace("'","").replace("(","").replace(")","").replace("b","").split(",") #this could look better ik
        ms.position = (int(float(Pos[0])), int(float(Pos[1]))) #Gotta do int(float(Pos[x])) due to some weird error
        ait.move(int(float(Pos[0])),int(float(Pos[1]))) #Makes this work on roblox


#Keyboard listen
def on_press(key):
    try:
        if key.char == LeftClickButton:
            ms.press(mouse.Button.left)
        elif key.char == RightClickButton:
            ms.press(mouse.Button.right)
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.KeyCode.from_char(LeftClickButton):
        ms.release(mouse.Button.left)
    elif key == keyboard.KeyCode.from_char(RightClickButton):
        ms.release(mouse.Button.right)

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

asyncio.get_event_loop().run_until_complete(websockets.serve(main, "", PORT))
print(f"Mobile Tab(PC) v{__version__}\nMade by The-Glit-ch({__devURL__})")
asyncio.get_event_loop().run_forever()