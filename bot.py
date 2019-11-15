import os
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from logging import getLogger, INFO, basicConfig

_format = "[%(asctime)s %(levelname)s %(name)s]: %(message)s"
basicConfig(level=INFO, format=_format)
logger = getLogger(__name__)

config = ConfigParser()
config.read('config.ini')

bot_config = config['bot']


chromedriver_path = os.getenv('CHROMEDRIVER_PATH', '')

options = Options()
options.add_argument('--user-agent=' + bot_config.get('user_agent', 'theme-bot'))
options.add_argument('--headless')
driver = webdriver.Chrome(chromedriver_path, chrome_options=options)

driver.get(bot_config.get('access_url'))

logger.info(driver.title)
driver.close()
driver.quit()
