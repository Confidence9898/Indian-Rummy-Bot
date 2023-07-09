from botcity.core import DesktopBot
import os
import pandas

class Bot(DesktopBot):
    def action(self, execution=None):
        
        self.start_emulator()
    
    def start_emulator(self):
        self.execute("D:\Memu\MEmu\MEmu.exe")
        
        self.open_indianrummy()
        
        self.play_rummy()

    def open_indianrummy(self):
        if not self.find("app-start", matching = 0.85, waiting_time=60000):
            self.not_found("app-start")
        self.click(interval_between_clicks = 700)
    
    def play_rummy(self):
        if not self.find("rummy-room", matching=0.85, waiting_time=60000):
            self.not_found("rummy-room")
        self.click(interval_between_clicks = 700)
        
        if not self.find("new-game-button", matching = 0.85, waiting_time=60000):
            self.not_found("new-game-button")
        self.click(interval_between_clicks = 700)
                            
        if not self.find("play-button", matching=0.85, waiting_time=60000):
            self.not_found("play-button")
        self.click(interval_between_clicks = 700)
        
        # if not self.find("throw-a-card", matching=0.85, waiting_time=60000):
        #     self.not_found("throw-a-card")
        # self.move()
            # if not self.find("back-card", matching = 0.7, waiting_time=60000):
            #     self.not_found("back-card")
            # self.moveAndClick(interval_between_clicks = 2000)
        
        # if not self.find("back-card", matching = 0.7, waiting_time=60000):
        #     self.not_found("back-card")
        # self.moveAndClick(interval_between_clicks = 700)
        while True:
            print('started automation.')
            if self.find("declare-button", matching = 0.85, waiting_time=3000):
                print('finded declare-button.')
                self.click_on("declare-button")
                break
            
            print('No Declare')
            
            if self.find("search-button", matching=0.85, waiting_time=60000):
                print('finded search button.')
                self.click_on("back-card")
                
            
            print('added new card.')
            
            while True:
                self.click_at(200, 945)
                print('clicked origin card.')
                if self.find("discard-button", matching=0.85, waiting_time=60000):
                    self.click_on("discard-button")
                    print('droped.')
                    break
                
        if not self.find("leavegame-button", macthing = 0.85, waiting_time=60000):
            self.not_found("leavegame-button")
        self.click_on("leavegame-button")
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
