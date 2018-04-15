"""
Flippy bit bot. It uses and was developed with the webdriver for Chromium. You
will need to install the correct drivers for your browser if you want to run
this. Change the browser at your own risk - I couldn't get firefox to work.

The constants defined at the start may need to be tweaked to suit your
preference.
"""

################################################################################


from time import sleep

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException

ARMISTICE_PAUSE = 2 # how long to wait if it doesn't see any enemies
START_SLEEP = 5 # how long to wait for the game to load at the start

driver = webdriver.Chrome()
driver.get("http://flippybitandtheattackofthehexadecimalsfrombase16.com/")

# used to find game elements
game = driver.find_element_by_id("game")
# used to send keypresses
body = driver.find_element_by_tag_name("body")

sleep(START_SLEEP)

print("clicking")
game.click()

# used to find current button states
curr_val = driver.find_element_by_id("attackValue")

try:
    while True:
        try:
            # find all enemies that haven't already been locked on to
            enemies = [enm for enm in
                            game.find_elements_by_css_selector("div.enemy")
                            if "under-attack" not in enm.get_attribute("class")]
            if enemies:
                for enemy in enemies:
                    # generate solution for current enemy
                    sol = bin(int(enemy.text, 16))[2:].rjust(8, "0")
                    # generate bits for current button state
                    crsol = bin(int(curr_val.text,
                                        16))[2:].rjust(8, "0")

                    print(("found enemy {}"
                           "- binary {}, calculated crsol as {}")
                           .format(enemy.text, sol, crsol))

                    for ind, (bit, sbit) in enumerate(
                            zip(sol, crsol), 1):
                        # essentially, takes the xor of current state and
                        # desired states, and XORs this with current state.
                        # NB: Curr ^ (Des ^ Curr) === Des
                        # This is essentially a 0-assumption approach, and
                        # results in very stable operation. It will happily
                        # keep running even if you change one of the bits.
                        if (bit == "1") ^ (sbit == "1"):
                            body.send_keys(str(ind))

            # if no enemies are found, pause
            else:
                print("no enemies to be seen")
                sleep(ARMISTICE_PAUSE)

        # to be on the safe side - this really only happens if an enemy
        # dies that was for some reason being examined due to a race
        # condition
        except StaleElementReferenceException:
            print("ignoring stale reference")


except KeyboardInterrupt:
    driver.close()
