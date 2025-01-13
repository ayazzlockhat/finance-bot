import discord
from discord.ext import commands
import yfinance as yf
import os
from dotenv import load_dotenv

load_dotenv()
# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is ready! Logged in as {bot.user}")

# Function to get stock data
def get_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        price = info.get('currentPrice') or info.get('navPrice')
        previous_close = info.get('regularMarketPreviousClose')
        high_52_week = info.get('fiftyTwoWeekHigh')
        long_name = info.get('longName', symbol.upper())
        
        if None in (price, previous_close, high_52_week):
            raise ValueError("Missing key data in stock information.")
        
        change_percent = ((price - previous_close) / previous_close) * 100
        return price, change_percent, high_52_week, long_name
    except Exception as e:
        print(f"Error fetching stock data for {symbol}: {e}")
        return None, None, None, None

@bot.command()
async def s(ctx, symbol: str = None):
    price, change_percent, high_52_week, long_name = get_stock_info(symbol)
    
    if price is None:
        await ctx.send("Error fetching stock data.")
        return
    
    # Creating embed for the message
    color = discord.Colour.green() if change_percent >= 0 else discord.Colour.red()
    
    # Creating embed for the message
    embed = discord.Embed(title=long_name, colour=color, description=symbol.upper())
    embed.add_field(name="Current Price", value=f"${price:.2f} ({change_percent:+.2f}%)", inline=False)
    embed.add_field(name="52 Week High", value=f"${high_52_week:.2f}", inline=False)
    
    # Sending the embed
    await ctx.send(embed=embed)

# Run the bot with your token
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)