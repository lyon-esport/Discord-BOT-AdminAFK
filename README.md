Discord BOT AdminAFK will make life better for CS:GO Admins

**This tool uses :**

* [eBot](http://www.esport-tools.net/ebot/)
* [Discord](https://discordapp.com/)
* [Discord.py](https://github.com/Rapptz/discord.py)
* [AdminAFK](https://github.com/lyon-esport/AdminAFK)

# Requirements

* Discord server
* eBot 3.1 or newer
* Python 3.6 or >=3.5.3
* Discord.py

# Install guide

1. Download or clone –> https://github.com/lyon-esport/Discord-BOT-AdminAFK
2. Extract the Discord-BOT-AdminAFK files
3. Install the requirements: `pip install -r requirements.txt`
4. Edit config.py with the good setting
5. Create an application here : https://discordapp.com/developers/applications/
6. Set the bot as a bot user. This will give you the token.
7. Add your bot to your discord (replace 0000000 by your client_id): https://discordapp.com/oauth2/authorize?client_id=0000000&scope=bot&permissions=1

## getting the channel_id

You should put discord in dev mode (https://support.discordapp.com/hc/fr/articles/206346498-O%C3%B9-trouver-l-ID-de-mon-compte-utilisateur-serveur-message-)
then right click on a channel -> copy channel id

# Usage guide

## Run the bot

You can start the bot with: `python main.py`

It's recommanded to run the bot in a tmux terminal.

## Commands
* !help - List of available commands

**ADMIN commands**

* !disable - Disable command
* !enable  - Enable command
* !status   - Status of a command
* !purge    - Purge messages [2-100]
* !flipcoin - Start a flipcoin (heads/tails)
* !maps     - Get five rounds of random maps
* !demo		- Generate an URL for download a demo on eBot
* !ping - Test bot connectivity
* !mute - Add the role muted to the user
* !unmute - Remove the role muted to the user

**USER commands**

* !bracket      - Get the link of bracket
* !connect      - Get the link of connect team
* !matchs       - Get info about matches on eBot
* !participants - Get the link of participants
* !report       - Get infos for report a player
* !rules        - Get the link of rules
* !gotv         - How to watch a demo ?
* !ebot         - Get the link of eBot

# Licence

The code is under CeCILL license.

You can find all details here: http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Lyon e-Sport, 2018

Contributor(s):

* Ortega Ludovic - ludovic.ortega@lyon-esport.fr
