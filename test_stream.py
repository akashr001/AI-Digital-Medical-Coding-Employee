import asyncio

from app.graph.workflow import graph


async def main():

    async for chunk in graph.astream(
        {
            "document_path":
            "documents/neuro.jpg"
        }
    ):

        print(
            "\nCHUNK:"
        )

        print(chunk)


asyncio.run(main())