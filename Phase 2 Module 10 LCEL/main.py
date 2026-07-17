from services import (
    BatchService,
    ExplainService,
    StreamService,
    SummarizeService,
    TranslateService,
)


def show_menu() -> None:
    print("\n" + "=" * 50)
    print("STUDY AI")
    print("=" * 50)

    print("1. Explain")
    print("2. Stream Explanation")
    print("3. Batch Explain")
    print("4. Summarize")
    print("5. Translate")
    print("0. Exit")


def handle_explain() -> None:
    topic = input("\nEnter topic: ").strip()

    if not topic:
        print("Topic is required.")
        return

    result = ExplainService.explain(
        topic
    )

    print("\nAI RESPONSE\n")
    print(result)


def handle_stream() -> None:
    topic = input("\nEnter topic: ").strip()

    if not topic:
        print("Topic is required.")
        return

    print("\nAI RESPONSE\n")

    for chunk in StreamService.stream_explanation(
        topic
    ):
        if chunk.content:
            print(
                chunk.content,
                end="",
                flush=True,
            )

    print()


def handle_batch() -> None:
    raw_topics = input("\nEnter topics separated by comma: ")

    topics = [
        topic.strip()
        for topic in raw_topics.split(",")
        if topic.strip()
    ]

    if not topics:
        print("Topics are required.")
        return

    results = BatchService.batch_explain(
        topics
    )

    for topic, result in zip(
        topics,
        results,
    ):
        print("\n" + "=" * 50)
        print(topic)
        print("=" * 50)

        print(result)


def handle_summarize() -> None:
    text = input("\nEnter text: ").strip()

    if not text:
        print("Text is required.")
        return

    result = SummarizeService.summarize(
        text
    )

    print("\nSUMMARY\n")
    print(result)


def handle_translate() -> None:
    text = input("\nEnter text: ").strip()

    language = input("Target language: ").strip()

    if not text or not language:
        print(
            "Text and language are required."
        )
        return

    result = TranslateService.translate(
        text=text,
        language=language,
    )

    print("\nTRANSLATION\n")
    print(result)


def main() -> None:
    handlers = {
        "1": handle_explain,
        "2": handle_stream,
        "3": handle_batch,
        "4": handle_summarize,
        "5": handle_translate,
    }

    while True:
        show_menu()

        choice = input(
            "\nChoose: "
        ).strip()

        if choice == "0":
            print("Goodbye!")
            break

        handler = handlers.get(choice)

        if handler is None:
            print("Invalid option.")
            continue

        try:
            handler()

        except Exception as error:
            print(
                f"Application error: {error}"
            )


if __name__ == "__main__":
    main()