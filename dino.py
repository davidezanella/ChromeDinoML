from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 

class Dino:
    FIGURES = {
        'CACTUS_SMALL': 0,
        'CACTUS_LARGE': 1,
        'PTERODACTYL': 2
    }

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/chromium"
        self._driver = webdriver.Chrome(options=options)

    def start(self):
        self._driver.get("chrome://dino")
        self._driver.execute_script("Runner.config.ACCELERATION=0")
        time.sleep(0.5) # wait the page loading
        self.jump() # in order to start the game

        time.sleep(4) # skip initial part of the game

    def jump(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_UP)

    def lower(self):
        self._driver.find_element_by_tag_name("body").send_keys(Keys.ARROW_DOWN)

    def get_score(self):
        return int(''.join(self._driver.execute_script("return Runner.instance_.distanceMeter.digits")))

    def is_game_over(self):
        return self._driver.execute_script("return Runner.instance_.crashed")

    def get_obstacles(self):
        obst_obj = self._driver.execute_script("return Runner.instance_.horizon.obstacles")

        if len(obst_obj) == 0:
            return [1000, 1000, 0, -1]
        i = obst_obj[0]

        type_fig = self.FIGURES[i['typeConfig']['type']]

        obstacle = [
            i['xPos'],
            i['yPos'],
            i['size'],
            type_fig,
        ]

        return obstacle

    def close(self):
        self._driver.close()
