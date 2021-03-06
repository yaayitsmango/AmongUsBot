### Summary

# Run this to start the program

# -------------------------------------------------

import os
os.system("cls")
print("\n[*] Warming up engine...\n\n")
print("[*] A chrome window will open now...\n[*] Enter your discord credentials in the window before we start")
from modules import module_grabscreen

from threading import Thread

class start_engine:
    def __init__(self, xResolution: int, yResolution:int):
        self.x, self.y = xResolution, yResolution
        self.run_main()

    def grabEndingScreen(self):
        module_grabscreen.grabEndingScreen(self.x, self.y)

    def grabDiscussionTitle(self):
        module_grabscreen.grabDiscussionTitle(self.x, self.y)

    def run_main(self):
        thread2 = Thread(target = self.grabEndingScreen) #need to grab 2 screens at a time
        thread3 = Thread(target = self.grabDiscussionTitle) 
        
        thread2.start()
        thread3.start()

if __name__ == "__main__":
    start = start_engine(1280, 720) #Please leave these values alone
