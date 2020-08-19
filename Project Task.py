import os
print("Menu Driven OS Based Program")
print("Chat with me - ")
while(1):
    print("Tell Me What u want to do?")
    p = input().lower()

    if(("open" in p) or ("run" in p)) and (("editor" in p) or ("notepad" in p)):
        os.system("notepad")

    elif("run" in p) and ("chrome" in p):
        if 'incognito' not in p or 'private' not in p:
            p = input("Do you want Incognito/Private Chrome? ").lower()
            if ('incognito' in p or 'private' in p or 'yes' in p):
                os.system("start chrome -incognito")
            else:
                os.system("start chrome google.com")

    elif(("play" in p) or ("start" in p)) and ("music" in p):
        desire = input("Do you want to Play Music in Window Music Player/Groove Music ? ").lower()
        if("window" in desire):
                os.system("wmplayer")
        else:
            os.system("start mswindowsmusic:")

    elif ('explorer' in p or 'file explorer' in p):
        os.system("start explorer")

    elif ('task manager' in p or 'taskmanager' in p):
        os.system("taskmgr")

    elif ('alarm' in p or 'clock' in p):
        os.system("start ms-clock:")

    elif ('calendar' in p):
        os.system("start outlookcal:")

    elif(("open" in p) or ("run" in p)) and ("calculator" in p):
        os.system("calc")

    elif(("open" in p)) and ("camera" in p):
        os.system("start microsoft.windows.camera:")

    elif ('action center' in p or 'notification' in p):
        os.system("start ms-actioncenter:")

    elif ('paint' in p):
        os.system("start ms-paint:")

    elif ('photo' in p or 'pic' in p):
        os.system("start ms-photos:")

    elif ('setting' in p):
        os.system("start ms-settings:")

    elif ('xbox' in p):
        os.system("start xbox:")

    elif ('map' in p):
        os.system("start bingmaps:")

    elif ('mail' in p):
        os.system("start outlookmail:")

    elif("exit" in p):
        print("Ok Bye")
        break
    else:
        print("Either the Request is Invalid or It can't  be Execute.\n")
