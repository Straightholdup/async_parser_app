import os
from service import async_parser_app

dirname = os.path.dirname(__file__)
config_dir = os.path.join(dirname, 'config.json')

# TODO CHANGE debug_mode IN CONFIG FILE TO false TO ENABLE MONITORING
app=async_parser_app.AsyncParserApp(config_dir=config_dir)

async def main():
    async with app.safe_requests.get("https://www.google.com/") as resp:
        print(await resp.text())

if __name__ == "__main__":
    app.run(main)