def cap_text(text):
    """Capitalize the first letter of each word in a string."""
    words = text.split()
    title_words = [word.title() for word in words]
    return " ".join(title_words)




#added new line
