# flippy\_bot
Flippy bit bot. It uses and was developed with the webdriver for Chromium. You
will need to install the correct drivers for your browser if you want to run
this. Change the browser at your own risk - I couldn't get firefox to work.

The constants defined at the start may need to be tweaked to suit your
preference/browser speed.

After a certain time, the bot will hit the limit of possible scores. This is
due to really quite primitive way the game approaches difficulty scaling.

Here are a selection of relevant screenshots of the game's JS code (`game.js`):

![screenshot](https://github.com/elterminad0r/flippy_bot/blob/master/screenshots/js_init.png)

![screenshot](https://github.com/elterminad0r/flippy_bot/blob/master/screenshots/cons_init.png)

![screenshot](https://github.com/elterminad0r/flippy_bot/blob/master/screenshots/js_attack.png)

![screenshot](https://github.com/elterminad0r/flippy_bot/blob/master/screenshots/js_cycle.png)

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
    = 87 Hz

As an estimate, this seems reasonable, so I consider this to be a satisfactory
explanation of why this happens.

Here is the resulting apocalypse:

![screenshot](https://github.com/elterminad0r/flippy_bot/blob/master/screenshots/apocalypse.png)
