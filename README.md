# balanced_teams
Create two teams that are as balanced as possible.

## Installation

```sh
pip install -r requirements.txt
```

## Running


### Setup

The app requires an API Key and a rankings file.
To provide these, you will need to create a [.env file](https://pypi.org/project/python-dotenv/) with:
```sh
cp .env.template .env
```

`BALANCE_THE_FORCE_API_KEY` is the discord bot api key.

`BALANCE_THE_FORCE_RANKINGS_DIRECTORY` is the directory where the rankings file `rankings.json` will be found.
If left blank, the app directory will be used. If provided, it must be an absolute path.

The `.env` file will need to exist, but the values can be overridden using command line arguments:
```sh
python balance_the_force.py --botkey ABC123 --rankings /path/to/dir
```

## Testing

```sh
python test.py
```

* TODO: Make use of discord.ext.commmands: https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html
* TODO: Add "bros" mode so that Balazs and Greg can play on the same team while making the teams as fair as possible
* TODO: Move rankings to a Google Sheet and allow users to dynamically upload or apply their own rankings
* TODO: When asking the bot to create teams, tell it who to include or who to exclude
