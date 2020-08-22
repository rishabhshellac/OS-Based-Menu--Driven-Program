import os
print("********************************************************************************************")
print("                                Menu Driven OS Based Program")
print("********************************************************************************************")

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

    elif ("open" in p) and ('explorer' in p or 'file explorer' in p):
        os.system("start explorer")

    elif ("open" in p) and ('task manager' in p or 'taskmanager' in p):
        os.system("taskmgr")

    elif ("open" in p) and ('alarm' in p or 'clock' in p):
        os.system("start ms-clock:")

    elif ("open" in p) and ('calendar' in p):
        os.system("start outlookcal:")

    elif(("open" in p) or ("run" in p)) and ("calculator" in p):
        os.system("calc")

    elif(("open" in p)) and ("camera" in p):
        os.system("start microsoft.windows.camera:")

    elif ("open" in p) and ('action center' in p or 'notification' in p):
        os.system("start ms-actioncenter:")

    elif ("open" in p) and ('paint' in p):
        os.system("start ms-paint:")

    elif ("open" in p) and ('photo' in p or 'pic' in p):
        os.system("start ms-photos:")

    elif ("open" in p) and ('setting' in p):
        os.system("start ms-settings:")

    elif ("open" in p) and ('xbox' in p):
        os.system("start xbox:")

    elif ("open" in p) and ('map' in p):
        os.system("start bingmaps:")

    elif ("open" in p) and ('mail' in p):
        os.system("start outlookmail:")

    elif("exit" in p):
        print("Ok Bye")
        break
    else:
        print("Either the Request is Invalid or It can't  be Execute.\n")
