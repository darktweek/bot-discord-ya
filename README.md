# Bot Discord Yu'ānang

A small bot for my Discord Server [Yu'anang](https://yuanang.space) (a small community from StarCitizen player).

He use somes slash command to do his best automation.

## Prerequisites

See official doc [here](https://discordpy.readthedocs.io/en/stable/intro.html).
This bot need a `.env` file, who need to have "token=token-id" to work.
All files in the `conf` folder need to be filed with correct id or data to ensure the bot is running fine.

## Running the tests

ya-prod-discord.py is "production" product.
ya-dev-discord.py is "developpement" product.
When I try new fuction, I do in dev with a test discord server and make test.
If it run good, I copy code in prod.

## Hint

- *cmd to start with log:*

`nohup python3 ya-prod-discord.py 1>ya-prod-discord-log.out 2>ya-prod-discord-log.err &`

- *cmd to update git:*

`git add . && git commit -m "cause" && git push origin`

## Built With

- [Visual Studio Code](https://code.visualstudio.com) - Used for the Code.
- [Discord.py](https://discordpy.readthedocs.io/en/stable/) - Used convert python to Discord API and more.

## Authors

- **Tweek** -    [DoT~NoT](https://dotnot.be) -    [Yu'anang](https://yuanang.space)
