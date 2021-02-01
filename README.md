# Everyday Astronaut Bot

## Overview
A bot that parses all of the upcoming launches from the [Everyday Astronaut website](https://everydayastronaut.com/upcoming-launches/) and alerts bot followers when there is an upcoming launch.

## How it works
The bot goes to the upcoming launches page of the Everyday Astronaut website and iterates through the upcoming launches looking for each launch's webpage. The Everyday Astronaut website has a unique page for each launch. Once the bot parses all of the websites from the upcoming launch list, it will go to each individual launch page and scrape its information. The bot then sends out a tweet using the launch information.