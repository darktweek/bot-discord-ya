# Bot Discord Yu'ānang

A small bot for my Discord Server [Yu'anang](https://yuanang.space) (a small community from StarCitizen player).

He use somes slash command to do his best automation.

## Prerequisites

See official doc [here](https://discordpy.readthedocs.io/en/stable/intro.html).
This bot need a `.env` file, who need to have "token=token-id" to work.
Set your variables to `var_dev` and/or `var_prod`.
When bot start, he call for *dev* or *prod* variables.

## Running the tests

When you start ya-discord.py prompt ask you `DEV` or `PROD` witch change where the bot start.
Use `DEV` to test the bot.

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
