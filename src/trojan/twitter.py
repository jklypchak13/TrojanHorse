import webbrowser
import tweepy
import os
import pygame
from requests_oauthlib import OAuth1Session

# Relative imports
from game.style import color as cval
from game.style import text as txt
from common.input_text import InputText


class Twitter:
    consumer_key = ''
    consumer_secret = ''
    user_key = ''
    user_secret = ''
    twitter_auth_url = ""    
    media_upload_url = "https://upload.twitter.com/1.1/media/upload.json"
    session = None
    api = None
    
    def __init__(self, PATH_TO_ROOT):
        self.bkg_img = pygame.image.load(
            f"{PATH_TO_ROOT}{os.sep}assets{os.sep}menu{os.sep}twitter_background.jpg"
        )
    
    def login_screen(self, window, main_clock):
        """Pygame screen to allow the user to input the verification key
        obtained from the twitter login page"""
        running = True
        invalid_input = False
    
        # Window height and width
        win_width, win_height = window.get_size()
    
        msg = txt.fancy_title.render("Enter verification code", 1, cval.white)

        box_width = 140
        box_height = 32
        loc_x = win_width/2 - box_width/2
        loc_y = win_height/2 - box_height/2
        input_box = InputText(loc_x, loc_y, box_width, box_height)
        invalid_text = txt.default_font.render("Invalid verifier", 1, cval.red)
        
        login_status = False
        
        print("FROM TWITTER - LOGIN: running =", running)
        while running:        
            window.fill(cval.maya_blue)  # Default to fill window with black
            window.blit(self.bkg_img, (0, 0))  # Overlay background image
            
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
                    # Attempt to initialize twitter api using supplied verifier
                    if (self.init_api(input_box.submitted) == None):
                        invalid_input = True
                        # request new verifier.
                        self.open_login_window()
                    else:
                        login_status = True
                        running = False
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            pygame.display.update()
            main_clock.tick(60)
            
        print("FROM TWITTER - LOGIN: running =", running)
        return login_status        


    def thank_user_window(self, window, main_clock):
        """Pygame screen to thank the user for helping us advertise the game"""
        running = True
        y_offset = 50 # vertical pixel offset
    
        # Window height and width
        win_width, win_height = window.get_size()
    
        title = txt.fancy_title.render(
                "Thank you!",
                1,
                cval.white
        )
        
        subtitle = [
                txt.fancy_sub_title.render("By sharing our game on Twitter,", 1, cval.white),
                txt.fancy_sub_title.render("you've greatly helped us reach a", 1, cval.white),
                txt.fancy_sub_title.render("wider audience with our game.", 1, cval.white)
        ]
        
        nav_text = txt.default_font.render(
                'Press "esc" to return to the main menu.',
                1,
                cval.white
        )
        
        print("FROM TWITTER - THANK: running =", running)
        while running:        
            window.fill(cval.maya_blue)  # Default to fill window with black
            window.blit(self.bkg_img, (0, 0))  # Overlay background image
            
            # Place title
            loc_x = win_width/2 - title.get_width()/2
            loc_y = win_height/3 - title.get_height()/2
            window.blit(title, (loc_x, loc_y))
            
            # Place subtitle
            loc_y = win_height/3
            for s in subtitle:
                loc_x = win_width/2 - s.get_width()/2
                loc_y += y_offset
                window.blit(s, (loc_x, loc_y))
            
            # place navigation text
            loc_x = win_width/2 - nav_text.get_width()/2
            loc_y += y_offset
            window.blit(nav_text, (loc_x, loc_y))
            
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            pygame.display.update()
            main_clock.tick(60)
            
        print("FROM TWITTER - THANK: running =", running)


    def open_login_window(self):
        """Open local browser window to have user login, and obtain
        verification key to grant access permissions to api"""
        request_token = OAuth1Session(client_key=self.consumer_key, client_secret=self.consumer_secret)
        url = 'https://api.twitter.com/oauth/request_token'
        data = request_token.get(url)

        print(data)

        data_token = str.split(data.text, '&')
        self.user_key = str.split(data_token[0], '=')[1]
        self.user_secret = str.split(data_token[1], '=')[1]

        twitter_auth_url = "https://api.twitter.com/oauth/authenticate?oauth_token={0}".format(self.user_key)
        webbrowser.open(twitter_auth_url)
    

    def init_api(self, verifier):
        self.session = OAuth1Session(client_key=self.consumer_key,
                                    client_secret=self.consumer_secret,
                                    resource_owner_key=self.user_key,
                                    resource_owner_secret=self.user_secret)
        url = 'https://api.twitter.com/oauth/access_token'
        data = {"oauth_verifier": verifier}
        access_token_data = self.session.post(url, data=data)
        
        # Simple response checking/reporting
        if (access_token_data.text == "Request token missing"
            or access_token_data.text == "Error processing your OAuth request: Invalid oauth_verifier parameter"
            or access_token_data.text == "This feature is temporarily unavailable"):
            # invalid verifier or malformed data
            return None
        print(access_token_data.text)
        
        # parse response data
        access_token_list = str.split(access_token_data.text, '&')
        access_token_key = str.split(access_token_list[0], '=')
        access_token_secret = str.split(access_token_list[1], '=')
        self.user_key = access_token_key[1]
        self.user_secret = access_token_secret[1]
        
        # initialize tweepy api using user data and session information
        self.session = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.session.set_access_token(self.user_key, self.user_secret)
        self.api = tweepy.API(self.session)
        return access_token_list
    
    
    def post_image(self, img_path:str, text = ""):
        self.api.update_with_media(img_path, text)
    
    
    def tweet_advertisement(self):
        self.api.update_status("I just got this game about a horse, and it's great! Check it out below. https://gofile.io/?c=aGTCyq")
        pass
    
    
    def get_user_data(self, access_token_list):
        """Print user/account information about the currently logged in user."""
        access_token_key = str.split(access_token_list[0], '=')
        access_token_secret = str.split(access_token_list[1], '=')
        
        key = access_token_key[1]
        secret = access_token_secret[1]
        self.session = OAuth1Session(client_key=self.consumer_key,
                                   client_secret=self.consumer_secret,
                                   resource_owner_key=key,
                                   resource_owner_secret=secret)
        url_user = 'https://api.twitter.com/1.1/account/verify_credentials.json'
        params = {"include_email": 'true'}
        user_data = self.session.get(url_user, params=params)
        print(user_data.json())
        return user_data.json()
