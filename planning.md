# Planning - Vampire the Masquerade (V20) Discord bot

## Create a Discord bot account
- Create a new application on the Discord Developer website ✔️
- Invite the bot to a server ✔️

## Install discord.py library
- Install discord.py (easy enough with pip install) ✔️

## Respond to basic commands
- Start off with acknowledging a dice roll command ✔️

## Respond to dice rolling requests
- Roll a requested number of d10s and and report the results ✔️

## Difficulty
- User inputs the difficulty, bot reports number of dice which equal or surpass it (aka, how many successes)

## Advanced V20 rolling logic
- Recognise a botch (a 1 when no successes are present)
- User can mark the roll as using a specialty, therefore bot reports a 10 as 2 successes
- Use willpower for automatic successes


## Things to Think About
- **Error handling:** What if the user tries an invalid command (like trying to roll  0.7 dice or AAAD dice, etc)