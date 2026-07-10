from config.llm import llm
from prompts.explain import explain_prompt
from prompts.summarize import summarize_prompt
from prompts.translate import translate_prompt


def main():
    print("=" * 40)
    print("Study AI")
    print("=" * 40)

    print("1. Explain")
    print("2. Summarize")
    print("3. Translate")

    choice = input("\nChoose: ")

    if choice == "1":
        topic = input("Topic: ")
        prompt = explain_prompt.format(
            topic=topic
        )

    elif choice == "2":
        text = input("Text: ")
        prompt = summarize_prompt.format(
            text=text
        )

    elif choice == "3":
        text = input("Text: ")
        language = input("Language: ")

        prompt = translate_prompt.format(
            text=text,
            language=language
        )

    else:
        print("Invalid choice.")
        return

    response = llm.invoke(prompt)

    print("\nAI Response\n")
    print(response.content)


if __name__ == "__main__":
    main()