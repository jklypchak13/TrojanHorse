from requests_oauthlib import OAuth1Session
import webbrowser
import pygame

# Relative imports
from game.style import color as cval
from game.style import text as txt
from common.input_text import InputText

class Twitter:
    consumer_key = 'aKkYumyPMh7vjw5FNAWvVtiyt'
    consumer_secret = '44tGvTDlEKS9hb52CXMHNsawksY1m8ARd76Inwq4oNRXKJZbBc'
    user_key = ''
    user_secret = ''
    twitter_auth_url = ""    
    password="PASSWORDHERE"
    
    def __init__(self, window, main_clock):
        running = True
    
        self.open_login_window()
    
        msg = txt.hacked_title.render("Enter verification code", 1, cval.white)

        input_box = InputText(100, 300, 140, 32)
        
        print("FROM TWITTER: running =", running)
        while running:        
            window.fill(cval.black)
         
            # Window height and width
            win_width, win_height = window.get_size()
            
            # Place twitter logo
            loc_x = win_width/2 - msg.get_width()/2
            loc_y = win_height/3 - msg.get_height()/2
            window.blit(msg, (loc_x, loc_y))
            
            # Draw
            input_box.draw(window)
            
            # Event handling
            for event in pygame.event.get():
                input_box.handle_event(event)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            pygame.display.update()
            main_clock.tick(60)
            
        
        print("FROM GAME: running =", running)
        
        return
    
    # STEP 1 call this function
    def open_login_window(self):
        request_token = OAuth1Session(client_key=self.consumer_key, client_secret=self.consumer_secret)
        url = 'https://api.twitter.com/oauth/request_token'
        data = request_token.get(url)

        data_token = str.split(data.text, '&')
        self.user_key = str.split(data_token[0], '=')[1]
        self.user_secret = str.split(data_token[1], '=')[1]

        twitter_auth_url = "https://api.twitter.com/oauth/authenticate?oauth_token={0}".format(self.user_key)
        webbrowser.open(twitter_auth_url)
    
    # STEP 2 place twitter_auth_url in the console to have the user log in & authorize the application
    # STEP 3 pass verifier as string to this function
    def get_account_access_token_list(self, verifier):
        oauth_token = OAuth1Session(client_key=self.consumer_key,
                                    client_secret=self.consumer_secret,
                                    resource_owner_key=self.user_key,
                                    resource_owner_secret=self.user_secret)
        url = 'https://api.twitter.com/oauth/access_token'
        data = {"oauth_verifier": verifier}
        access_token_data = oauth_token.post(url, data=data)
        access_token_list = str.split(access_token_data.text, '&')
        return access_token_list
    
    
    def twitter_get_access_token(self, access_token_list):
        access_token_key = str.split(access_token_list[0], '=')
        access_token_secret = str.split(access_token_list[1], '=')
        access_token_id = str.split(access_token_list[2], '=')
        access_token_name = str.split(access_token_list[3], '=')
        
        key = access_token_key[1]
        secret = access_token_secret[1]
        name = access_token_name[1]
        id = access_token_id[1]
        oauth_user = OAuth1Session(client_key=self.consumer_key,
                                   client_secret=self.consumer_secret,
                                   resource_owner_key=key,
                                   resource_owner_secret=secret)
        url_user = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        params = {"include_email": 'true'}
        user_data = oauth_user.get(url_user, params=params)
        print(user_data.json())
        return user_data.json()
