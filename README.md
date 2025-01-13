# Finance Bot

This is a Discord bot that fetches stock information using the Yahoo Finance API and displays it on Discord.

## Prerequisites
- **Docker** installed on your machine (can also be ran locally but must give the bot token manually).
- **A Discord Bot Token**. You can get this by creating a bot through the [Discord Developer Portal](https://discord.com/developers/applications).
  
## Setup Instructions

1. **Clone the Repository**:
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/ayazzlockhat/finance-bot.git
   cd finance-bot
   ```

2. **Build the Docker Image**:
   Build the Docker image using the Dockerfile in the repository:
   ```bash
   docker build -t finance-bot .
   ```
3. **Run the Bot in Docker**:
   Now, you can run the bot in Docker by passing your Discord Bot Token as an environment variable:
   ```bash
   docker run -d --name finance-bot -e DISCORD_BOT_TOKEN=your-bot-token-here --restart unless-stopped finance-bot
   ```
   Variables:
   - ```-e DISCORD_BOT_TOKEN```: Set the environment variable ```DISCORD_BOT_TOKEN``` to your bot token.
4. **Interacting with the Bot**:
   The bot responds to ```$s``` command to get stock information
   
   Example:
   ```bash
   $s AAPL
   ```

   This command will fetch the current stock price, 52-week high, and price change for Apple (AAPL).
   ![image](https://github.com/user-attachments/assets/10156bd6-cd6c-46f4-9181-fb5a25708fb3)

