from requests_oauthlib import OAuth1Session
import webbrowser
import pygame
import tweepy

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
    media_upload_url = "https://upload.twitter.com/1.1/media/upload.json"
    session = None
    api = None
    
    def login_screen(self, window, main_clock):
        running = True
        invalid_input = False
    
        # Window height and width
        win_width, win_height = window.get_size()
    
        msg = txt.hacked_title.render("Enter verification code", 1, cval.white)

        box_width = 140
        box_height = 32
        loc_x = win_width/2 - box_width/2
        loc_y = win_height/2 - box_height/2
        input_box = InputText(loc_x, loc_y, box_width, box_height)
        invalid_text = txt.default_font.render("Invalid verifier", 1, cval.red)
        
        print("FROM TWITTER: running =", running)
        while running:        
            window.fill(cval.black)
            
            # Place msg
            loc_x = win_width/2 - msg.get_width()/2
            loc_y = win_height/3 - msg.get_height()/2
            window.blit(msg, (loc_x, loc_y))
            
            input_box.draw(window)
            
            if invalid_input == True:
                loc_x = win_width/2 - invalid_text.get_width()/2
                loc_y = win_height/3 - invalid_text.get_height()*2/3
                window.blit(invalid_text, (loc_x, loc_y))
            
            # Event handling
            for event in pygame.event.get():
                input_box.handle_event(event)
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                    # Attempt to initialize twitter api
                    print("recvd: ", input_box.submitted)
                    if (self.init_api(input_box.submitted) == None):
                        invalid_input = True
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            pygame.display.update()
            main_clock.tick(60)
            
        print("FROM TWITTER: running =", running)
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
    def init_api(self, verifier):
        self.session = OAuth1Session(client_key=self.consumer_key,
                                    client_secret=self.consumer_secret,
                                    resource_owner_key=self.user_key,
                                    resource_owner_secret=self.user_secret)
        url = 'https://api.twitter.com/oauth/access_token'
        data = {"oauth_verifier": verifier}
        access_token_data = self.session.post(url, data=data)
        
        if (access_token_data.text == "Request token missing"
            or access_token_data.text == "Error processing your OAuth request: Invalid oauth_verifier parameter"
            or access_token_data.text == "This feature is temporarily unavailable"):
            # invalid verifier or malformed data
            return None
        print(verifier)
        print(access_token_data.text)
        access_token_list = str.split(access_token_data.text, '&')
        access_token_key = str.split(access_token_list[0], '=')
        access_token_secret = str.split(access_token_list[1], '=')
        self.user_key = access_token_key[1]
        self.user_secret = access_token_secret[1]
        self.session = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.session.set_access_token(self.user_key, self.user_secret)
        self.api = tweepy.API(self.session)
        return access_token_list
    
    
    def post_image(self, img_path:str, text = ""):
        self.api.update_with_media(img_path, text)
    
    
    def get_user_data(self, access_token_list):
        access_token_key = str.split(access_token_list[0], '=')
        access_token_secret = str.split(access_token_list[1], '=')
        #access_token_id = str.split(access_token_list[2], '=')
        #access_token_name = str.split(access_token_list[3], '=')
        
        key = access_token_key[1]
        secret = access_token_secret[1]
        #name = access_token_name[1]
        #id = access_token_id[1]
        self.session = OAuth1Session(client_key=self.consumer_key,
                                   client_secret=self.consumer_secret,
                                   resource_owner_key=key,
                                   resource_owner_secret=secret)
        url_user = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        params = {"include_email": 'true'}
        user_data = self.session.get(url_user, params=params)
        print(user_data.json())
        return user_data.json()
