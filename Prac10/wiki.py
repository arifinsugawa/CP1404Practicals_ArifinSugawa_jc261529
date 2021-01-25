import wikipedia
def main():
    user_input = 'a'
    while user_input != ' ':
        try:
            user_input = input("Please enter page title or search phase : ")
            page = wikipedia.page(user_input)
            print("Page title: " + page.title)
            print("Page Summary : " + wikipedia.summary(user_input, sentences=5))
            print("Page URL : " + page.url)

        except wikipedia.exceptions.DisambiguationError:
            print("Search phase / page title is too general")


main()
