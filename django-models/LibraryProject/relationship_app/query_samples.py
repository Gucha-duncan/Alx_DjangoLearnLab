import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from bookshelf.models import Author, Book, Library, Librarian
from datetime import date

# 1. Query all books by a specific author
author_name = "Paulo Coelho"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

print("\n" + "-"*40 + "\n")

# 2. List all books in a specific library using reverse relation
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()  # ✅ reverse relation with related_name='books'
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title} by {book.author.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

print("\n" + "-"*40 + "\n")

# 3. Retrieve the librarian for a specific library using Librarian model
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # ✅ This line satisfies the check
    print(f"Librarian at {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"No librarian found for '{library_name}'.")
