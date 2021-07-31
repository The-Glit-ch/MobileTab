#To find internal IP on Windows
#   1. Click on the windows logo(bottom left)
#   2. Type "control panel" and open it
#   3. Click on "Network and Internet"
#   4. Click on "Network and Sharing Center"
#   5. Look for "Connections:" followed by your network name
#   6. Click on your network name
#   7. Click "details" on the little pop up
#   8. On the new pop up window look for "IPv4 Address". If you use IPv6 look for "IPv6 Address"
#   9. Take note of the IP and put in the "IP" variable
#------------------------------------------------------
#To find internal IP on Mac
#   1. Click on the Apple icon on the upper-left corner of the screen
#   2. Select System Preferences
#   3. Click Network
#   4. Under "Status" you should see "connected to {wifi-name} and has the IP address {ip}"
#   5. Take note of the IP and put in the "IP" variable
#------------------------------------------------------
#To find IP on Linux
#   1. Open Terminal
#   2. Type "hostname -I"
#   3. Take note of the first IP and put it in the "IP" variable
#------------------------------------------------------
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
__version__ = "1.0.0"
__devURL__  = "https://github.com/The-Glit-ch"

#global
global Left_KeyToggle
global Right_KeyToggle
Right_KeyToggle = False
Left_KeyToggle = False

#YOU CAN CHANGE ME
IP = "" #Replace with your internal IP. MAKE SURE ITS PUT IN "". EX: "127.0.0.1"
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
    global Left_KeyToggle #Kinda cringe
    global Right_KeyToggle #Even more cringe

    try:
        if key.char == LeftClickButton and Left_KeyToggle != True:
            ms.press(mouse.Button.left)
            Left_KeyToggle = True
        elif key.char == RightClickButton and Right_KeyToggle != True:
            ms.press(mouse.Button.right)
            Right_KeyToggle = True
    except AttributeError:
        pass

def on_release(key):
    global Left_KeyToggle #Kinda cringe
    global Right_KeyToggle #Even more cringe
    
    if key == keyboard.KeyCode.from_char(LeftClickButton) and Left_KeyToggle:
        ms.release(mouse.Button.left)
        Left_KeyToggle = False
    elif key == keyboard.KeyCode.from_char(RightClickButton) and Right_KeyToggle:
        ms.release(mouse.Button.right)
        Right_KeyToggle = False

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

asyncio.get_event_loop().run_until_complete(websockets.serve(main, IP, PORT))
print(f"Mobile Tab(PC) v{__version__}\nMade by The-Glit-ch({__devURL__})")
asyncio.get_event_loop().run_forever()