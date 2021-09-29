from service import apps
import asyncio

async def main():
    companies_to_search = [
        "КЫДЫРАЛИН А. А.",
        "КЫДЫРАЛИН А. А.",
        "КЫДЫРАЛИН А. А.",
        "КЫДЫРАЛИН А. А.",
    ]

    tasks = []
    for company in companies_to_search:
        tasks.append(asyncio.create_task(app.services.searchCompany( company_name=company)))

    companies_res = await asyncio.gather(*tasks)

    print(companies_res)


if __name__ == "__main__":
    app = apps.AsyncParserApp()
    app.run(main)