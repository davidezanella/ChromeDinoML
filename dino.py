from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 

class Dino:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/chromium"
        self._driver = webdriver.Chrome(options=options)

    def start(self):
        self._driver.get("chrome://dino")
        time.sleep(0.5) # wait the page loading
        self.jump() # in order to start the game

    def jump(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)

    def lower(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_DOWN)

    def get_score(self):
        return ''.join(self._driver.execute_script("return Runner.instance_.distanceMeter.digits"))

    def is_game_over(self):
        return self._driver.execute_script("return Runner.instance_.crashed") == 'true'

    def get_obstacles(self):
        obst_obj = self._driver.execute_script("return Runner.instance_.horizon.obstacles")
        obstacles = []

        for i in obst_obj:
            obstacles.append({
                'x': i['xPos'],
                'y': i['yPos'],
                'size': i['size'],
                'type': i['typeConfig']['type'],
            })

        return obstacles
