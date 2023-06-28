
# Hello Theodore!
What is MaskedBOT? Well, MaskedBOT is a Python based Discord bot that has a huge genre of features that you can toggle on and off via the included config file. MaskedBOT is capable of features like banning, kicking, muting, sending embeds and a plethra of other features. The main goal of this bot is to piss of companies like MEE6 or Dyno that has a paywall for some of the most basic features that Discord bots are capable of. As it's Python based and it's open sourced this bot (even with these "premium" features) is COMPLETELY free. There is no paywall, you don't have to pay for anything. You host it on your hardware and I will supply updates & fixes for the bot. I do not expect any payment from this project at all. It is completly just to annoy those scummy companies that charge you for something that took 10 mins to create. Please read through this README.md file as it has some very useful information regarding the bot, how to get it running and how you can request features or support. Thanks!

**WARNING: MaskedBOT is currently still in BETA phase and does not include all the features said above, please check the Features section to see current features in the most recent verison.**
## Deployment
Firstly, please head to this repositories [Releases](https://github.com/TCSMasked/MaskedBOT/releases) page and download the most recent, and stable build of MaskedBOT. Secondly, open up the `config.json` file in your text editor or prefered IDE. Now after opening the `config.json` file you are going to need to fill in some required information to get the bot running on your server.

config.json:
```
{
    "token": "TOKEN",
    "guildID": "GUILDID",
    "staffroleID": "CHANNELID",
    "mutedroleID": "CHANNELID",
    "logchannelID": "CHANNELID",
    "botStatus": "dnd", // Options: online, offline, idle, dnd, invisible
    "botPrefix": "!",
    "botStatusMSG": "Hello World!",
    "badWordDetecor": "true",
    "serverInvitesDetector": "true",
    "AntiSpam": "true",
    "welcomeFeature": "true",
    "welcomeFeatureChannelID": "CHANNELID", // leave empty if turned off
    "goodbyeFeature": "true",
    "goodbyeFeatureChannelID": "CHANNELID" // leave empty if turned off
}
```
After filling in these **required** fields you can now start the PIP requirements installation.\
Before continuing please ensure that you have a Python version of **Python 3.4** or above as these versions include the package manager PIP.\

Now, after ensuring you have Python 3.4 or above open a terminal prompt / command prompt *(with or without administrative access)* inside the same directory as MaskedBOT, and run this command.\
`py -m pip install -r requirements.txt` **or** `python -m pip install -r requirements.txt`\
After running this command all the required Python packages for MaskedBOT will now be installed to your machine, and you can finally run the file `main.py` with Python.
## Features
- Moderation Commands
- Logging
- Startup Message
## Usage
By downloading and using MaskedBOT you are agreeing to the following usage terms.\
**1)** You MUST not redistribute, sell or profit from this bot.\
**2)** If you reupload modified code you will credit the author (me).\
**3)** Modification of the code is allowed but you cannot profit from it.\
**4)** Do not use this bot with malicious intent, this means that you cannot use this bot for scams, spamming, raiding, and *(but not limited to)* trolling.\
**5)** Please make sure that any modified code respects Discord's TOS.\
**6)** I cannot be held accountable for any actions others make using this bot.\
**7)** I cannot be held accountable for any legallity problems this bot may cause.\
**8)** Please respect other services TOS if used.\
**9)** Respect that the author has but time into creating this for people, show them some respect and credit them.
## Contributing / Support
As already said, modification or addition to the code is more then welcome. However if you have any suggestions or features you personally would like to see then please feel free to contact me via my online social media. You can find my social media [here](https://tcsmasked.maskednet.org). There is a business email attached to my [website](https://tcsmasked.maskednet.org) if you would rather emailing me instead.\
If you require some support then you can contact me via the same methods mentioned above, please try to describe your issue or what you want added as best as possibly can. Thanks, and I hope you enjoy!
