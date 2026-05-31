import os
import zipfile

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(
    api_subscription_key=
    os.getenv(
        "SARVAM_API_KEY"
    )
)


def ocr_agent(state):

    print(
        "OCR Agent Started"
    )

    document_path = state[
        "document_path"
    ]

    job = (
        client
        .document_intelligence
        .create_job(
            language="en-IN",
            output_format="md"
        )
    )

    print(
        "Uploading document..."
    )

    job.upload_file(
        document_path
    )

    print(
        "Starting OCR job..."
    )

    job.start()

    print(
        "Waiting for completion..."
    )

    status = (
        job.wait_until_complete()
    )

    print(
        f"Job Status: {status.job_state}"
    )

    output_zip = (
        "ocr_output.zip"
    )

    job.download_output(
        output_zip
    )

    extract_dir = (
        "ocr_output"
    )

    with zipfile.ZipFile(
        output_zip,
        "r"
    ) as zip_ref:

        zip_ref.extractall(
            extract_dir
        )

    md_text = ""

    for root, dirs, files in os.walk(
        extract_dir
    ):

        for file in files:

            if file.endswith(
                ".md"
            ):

                file_path = (
                    os.path.join(
                        root,
                        file
                    )
                )

                with open(
                    file_path,
                    "r",
                    encoding="utf-8"
                ) as f:

                    md_text += (
                        f.read()
                        + "\n"
                    )

    state[
        "ocr_text"
    ] = md_text

    print(
        "OCR Completed"
    )

    return state