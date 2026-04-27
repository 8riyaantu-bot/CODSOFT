def recommend():
    movies = {
        "action": ["Avengers", "Batman", "John Wick"],
        "comedy": ["Mr Bean", "The Mask", "Hangover"],
        "romance": ["Titanic", "Notebook", "La La Land"],
        "horror": ["Conjuring", "It", "Annabelle"]
    }

    print("Available categories: action, comedy, romance, horror")
    choice = input("Enter your favorite category: ").lower()

    if choice in movies:
        print("Recommended movies:")
        for movie in movies[choice]:
            print("-", movie)
    else:
        print("Category not found!")

recommend()
