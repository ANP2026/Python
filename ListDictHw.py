books = ["Wonder", "Diary of a Wimpy Kid", "Divergent", "Insurgent", "Allegiant"]
print("The amount of books:", len(books))
print("The first book:", books[0])
print("The last book:", books[-1])
print("The first three books:", books[0:3])

books.append("Matilda")
print("After adding Matilda:", books)
books.remove("Diary of a Wimpy Kid")
print("After removing Diary of a Wimpy Kid:", books)
books.sort
print("After sorting alphabetiacally:", books)
books.reverse()
print("After reversing the order:", books)

librarian = {"Name": "Ms. Sharma", "Section": "Front Desk", "Experience": 7}
print("The librarian's name:", librarian["Name"])
librarian["Experience"] = 8
librarian["Email"]="Sharma@gmail.com"
librarian.pop("Section")

book_ids = [1, 2, 3, 4, 5,]
book_names=["Wonder", "Diary of a Wimpy Kid", "Divergent", "Insurgent", "Allegiant"]
book_directory=dict(zip(book_ids, book_names))
print("The book book_directory", book_directory)