from server.discord_api import client,discord_token
URL="https://discord.com/api/oauth2/authorize?client_id=987953315587428352&permissions=8&scope=bot"

if __name__ == '__main__':
    client.run(discord_token)
