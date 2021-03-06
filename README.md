# MonkeBot
A Discord bot that uploads gif and pictures of monkeys -- among other things.

## Main Usage Example:
![monkebot usage](https://i.imgur.com/CdBPr7U.png)

## Command List:
Every command uses the prefix .monke

**monke**: Gets a random gif of a monkey.

**gif \[query\]**: Gets a random, g-rated gif, given a query.

**gif_custom \[rating\] \[query\]**: Gets a random gif with the given rating, given a query.

**angry**: Gets a picture of an angry monkey.

**pog**: Gets a picture of a monkey with an open mouth.

**8ball \[question\]**: Will pick a random 8ball response to your question.

**fact**: Picks a random fact out of a list of 20 facts, and adds a picture of a thinking monkey to go along with it.

**hi**: Makes monkebot say "Hi, I'm Paul!" and play the gif of the dna productions outro.

**screech**: Will make monkebot join the current voice channel and play one of two clips of a monkey screeching.

**shoot \[person\]**: Will "shoot" whoever is @'d in the server by playing a random gif of a monkey shooting a gun. Saying "someone" instead of @ing someone will make the bot "shoot" a random member.

## How to Use
To use MonkeBot on your own, you will need:

A bot api key from Discord (get one here: https://discord.com/developers/applications), which you will need to put in token.txt

An api key from Giphy (get one here: https://developers.giphy.com/docs/api#quick-start-guide), which you will need to put in giphytoken.txt

A Google Custom Search API key (see instructions here: https://pypi.org/project/Google-Images-Search/), which you will need to put in imagestoken.txt. You will also need to replace the images_cx variable in image.py with the cx of your custom google search engine made during the process.

You will need the latest version of python, and need to install discord.py, google_images_search, and giphy_client via pip. 

Finally, you will need to install [ffmpeg](https://ffmpeg.org/).

Alternatively, you may add the bot to your server here:

https://discord.com/api/oauth2/authorize?client_id=757075376148185089&permissions=3270656&scope=bot

The bot will most likely not be online, but you are free to try!
