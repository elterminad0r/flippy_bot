# flippy\_bot
Flippy bit bot. It uses and was developed with the webdriver for Chromium. You
will need to install the correct drivers for your browser if you want to run
this. Change the browser at your own risk - I couldn't get firefox to work.

It's of course also dependent on Selenium.

The constants defined at the start may need to be tweaked to suit your
preference/browser speed.

After a certain time, the bot will hit the limit of possible scores. This is
due to really quite primitive way the game approaches difficulty scaling.

Here are a selection of relevant screenshots of the game's JS code (`game.js`):

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_init.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/cons_init.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_attack.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_cycle.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/js_timeout.png)

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/config_timeout.png)

Basically, the game initially sets the millisecond interval between enemies to
5000 ms. Whenever an enemy dies this interval is decreased by 30 ms, and
whenever the game refreshed and the "cycle" function is called, the time is
further decreased by 0.2 ms. The cycle function has a constant interval of 10
ms, but also takes some time to run. This means that the upper bound of
achievable score is variable between computers, or even on the same computer
can depend on CPU and memory availability.

On my laptop, this apocalypse happens at around 80 enemies, two and a half
minutes in. This means that my refresh rate would be:

    (5000 - 80 * 30) / 150 / 0.2
    ~ 87 Hz

As a high-uncertainty estimate, this seems reasonable. It also leads to a cycle time of

    1 / 87
    ~ 11-12 ms

Reassuringly, this is more than 10 ms and would put the average execution speed
of a cycle at a couple of ms.

All in all, I consider this to be a satisfactory explanation of why this
happens.

Frustratingly, this result means that the best way to get a high score using
the bot is to play flippy bit on a slower computer.

However, if you as a human start to press as many keys as quickly as possible
as soon as the program crashes, your score actually goes up very fast. This is
because almost everything is on screen at once.

Here is the resulting apocalypse:

![screenshot](https://github.com/goedel-gang/flippy_bot/blob/master/screenshots/apocalypse.png)
