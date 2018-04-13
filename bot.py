"""
Flippy bit bot. It uses and was developed with the webdriver for Chromium. You
will need to install the correct drivers for your browser if you want to run
this. Change the browser at your own risk - I couldn't get firefox to work.

The constants defined at the start may need to be tweaked to suit your
preference. I've also found that sometimes it starts spawning enemies at a
ridiculous rate. I've yet to figure out why this is.
"""

################################################################################


from time import sleep
from collections import deque

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

ARMISTICE_PAUSE = 2
START_SLEEP = 5

driver = webdriver.Chrome()
driver.get("http://flippybitandtheattackofthehexadecimalsfrombase16.com/")

game = driver.find_element_by_id("game")
body = driver.find_element_by_tag_name("body")

sleep(START_SLEEP)

print("clicking")
game.click()

curr_val = driver.find_element_by_id("attackValue")

try:
    while True:
        enemies = [enm for enm in
                        game.find_elements_by_css_selector("div.enemy")
                        if "under-attack" not in enm.get_attribute("class")]
        if enemies:
            try:
                enemies.sort(key=lambda enm: bin(int(enm.text, 16)).count("1"))

                for enemy in enemies:
                    if True:
                        sol = bin(int(enemy.text, 16))[2:].rjust(8, "0")
                        crsol = bin(int(curr_val.text,
                                            16))[2:].rjust(8, "0")

                        print(("found enemy {}"
                               "- binary {}, calculated crsol as {}")
                               .format(enemy.text, sol, crsol))

                        for ind, (bit, sbit) in enumerate(
                                zip(sol, crsol), 1):
                            if (bit == "1") ^ (sbit == "1"):
                                body.send_keys(str(ind))

                    else:
                        print("silly game wants to kill dead enemy")
                        sleep(1)

            except StaleElementReferenceException:
                print("ignoring stale reference")
        else:
            print("no enemies to be seen")
            sleep(ARMISTICE_PAUSE)

except KeyboardInterrupt:
    driver.close()
