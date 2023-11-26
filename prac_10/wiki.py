import wikipedia


def main():
    user_input = input("Enter a Wikipedia page title or search phrase: ")
    while user_input != "":
        try:
            page_info = wikipedia.page(user_input)
            print("\nTitle:", page_info.title)
            print("Summary:", page_info.summary)
            print("URL:", page_info.url)
            summary = wikipedia.summary(user_input)
            print(summary)
            user_input = input("Enter a Wikipedia page title or search phrase: ")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Ambiguous term. Please choose a more specific title:")
            for i, option in enumerate(e.options, start=1):
                print(f"{i}. {option}")
            choice = input("Enter the number of the option you want: ")
            if choice.isdigit() and 1 <= int(choice) <= len(e.options):
                user_input = e.options[int(choice) - 1]
                try:
                    summary = wikipedia.page(title=user_input, auto_suggest=False)
                    print("\nSummary:")
                    print(summary)
                except wikipedia.exceptions.HTTPTimeoutError:
                    print("Timeout error. Please check your internet connection and try again.")
                except wikipedia.exceptions.PageError:
                    print("Page not found. Please enter a valid Wikipedia page title.")
                except wikipedia.exceptions.WikipediaException:
                    print(f"An unexpected error occurred")


if __name__ == "__main__":
    main()
