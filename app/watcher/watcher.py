import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from app.rag.ingest import ingest_documents


class KnowledgeHandler(
    FileSystemEventHandler
):

    def __init__(self):
        self.last_run = 0

    def on_modified(
        self,
        event
    ):

        if event.is_directory:
            return

        if not event.src_path.endswith(
            ".txt"
        ):
            return

        current_time = time.time()

        if current_time - self.last_run < 2:
            return

        self.last_run = current_time

        print(
            f"\nFile Updated: {event.src_path}"
        )

        try:

            ingest_documents()

            print(
                "Qdrant Updated"
            )

        except Exception as e:

            print(
                f"Error: {e}"
            )


def start_watcher():

    path = "knowledge/icd10"

    event_handler = (
        KnowledgeHandler()
    )

    observer = Observer()

    observer.schedule(
        event_handler,
        path,
        recursive=True
    )

    observer.start()

    print(
        "Watching knowledge folder..."
    )

    try:

        while True:

            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()


if __name__ == "__main__":

    start_watcher()