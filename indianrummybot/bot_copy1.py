from botcity.core import DesktopBot

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
        
        while True:
            print('started automation.')
            if self.find("declare-button", matching = 0.85, waiting_time=3000):
                print('finded declare-button.')
                self.click_on("declare-button")
                break
            
            print('No Declare')
            
            if self.find("search-button", matching=0.75, waiting_time=60000):
                print('finded search button.')
                self.click_on("back-card")
                
            
            print('Added new card.')
            
            num_set = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
            # suite_set = ['black', 'red']
            finded = False
            
            for num in num_set:
                # for suite in suite_set:
                card_number = f'{num}'
                print(f"Finding {card_number}")
                if self.find(card_number, matching = 0.75, waiting_time=3000):
                    while True:
                        self.moveAndClick(wait_after= 1000)
                        print(f'there is {card_number}')
                        if self.find("discard-button", matching=0.75, waiting_time=60000):
                            self.click_on("discard-button")
                            print(f'{card_number} is discarded')
                            finded = True
                            break
                if finded:
                    break
                    
        if not self.find("leavegame-button", macthing = 0.85, waiting_time=60000):
            self.not_found("leavegame-button")
        self.click_on("leavegame-button")
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
