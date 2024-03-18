# sBTC Tracker - Telegram Bot
sBTC telegram tracker using Hiro Chainhooks

## What is this? 
This is a tracker built with [Hiro Chainhooks](https://docs.hiro.so/chainhook) with Telegram, to receive notifications of any transaction with [sBTC](https://sbtc.tech/) on [Stacks](https://www.stacks.co/).

## How does it work?

Check this video.

## Steps to implement

1. Register in [Replit](https://replit.com/).
2. Fork [this template](https://replit.com/@nescampos/sBTCTokenTracker)
3. Create a telegram bot using [BotFather](https://t.me/botfather)
4. You will receive a token from the new bot.
5. Add that token as a secret in the Replit project, with the name **BOT_TOKEN**.
6. Deploy the Replit project and copy the new web app URL.
7. Create a [Hiro Project](https://platform.hiro.so/).
8. Create a Chainhook with the following parameters:
   - Chain: Stacks
   - Network: testnet
   - Scope: ft_event
   - Asset identifier: ST1R1061ZT6KPJXQ7PAXPFB6ZAZ6ZWW28G8HXK9G5.asset-3::sbtc
   - Actions: check all.
   - Action: http_post
   - URL: "The URL you got from Replit", adding at the end "/verify".
   - Start Block: 131527
9. Test your new bot in Telegram.

**You can use this project to track any token, just change the Asset Identifier and the Start Block in the Chainhook**


## Issues

- When creating a chainhook to monitor actions on a token, verify that the token has already been created in the start block (from where the monitoring starts) (that is, the creation time), because you will get an error when searching for the token on older blocks.
- By default, Telegram bots allow 30 messages per second. If you want more, contact telegram support.
