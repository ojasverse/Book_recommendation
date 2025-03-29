books_data = [ 
    ["Harry Potter and the Half-Blood Prince (Harry Potter #6)", "J.K. Rowling", 
"Fantasy"], 
    ["Harry Potter and the Order of the Phoenix (Harry Potter #5)", "J.K. Rowling", 
"Fantasy"], 
    ["The Fellowship of the Ring (The Lord of the Rings #1)", "J.R.R. Tolkien", 
"Fantasy"], 
    ["Harry Potter and the Chamber of Secrets (Harry Potter #2)", "J.K. Rowling", 
"Fantasy"], 
    ["Harry Potter and the Prisoner of Azkaban (Harry Potter #3)", "J.K. Rowling", 
"Fantasy"], 
    ["The Lightning Thief (Percy Jackson and the Olympians #1)", "Rick Riordan", 
"Fantasy"], 
    ["To Kill a Mockingbird", "Harper Lee", "Classics"], 
    ["1984", "George Orwell", "Dystopian Fiction"], 
    ["Pride and Prejudice", "Jane Austen", "Romance"], 
    ["The Catcher in the Rye", "J.D. Salinger", "Classics"], 
    ["The Great Gatsby", "F. Scott Fitzgerald", "Classics"], 
    ["The Hobbit", "J.R.R. Tolkien", "Fantasy"], 
    ["The Da Vinci Code", "Dan Brown", "Mystery"], 
    ["The Alchemist", "Paulo Coelho", "Fantasy"], 
    ["The Girl with the Dragon Tattoo", "Stieg Larsson", "Mystery"], 
    ["The Hunger Games", "Suzanne Collins", "Science Fiction"], 
    ["The Help", "Kathryn Stockett", "Historical Fiction"], 
    ["Gone Girl", "Gillian Flynn", "Mystery"], 
    ["The Fault in Our Stars", "John Green", "Young Adult Fiction"], 
    ["The Lord of the Rings: The Two Towers", "J.R.R. Tolkien", "Fantasy"], 
    ["The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "C.S. Lewis", 
"Fantasy"], 
    ["A Game of Thrones (A Song of Ice and Fire #1)", "George R.R. Martin", 
"Fantasy"], 
    ["The Shining", "Stephen King", "Horror"], 
    ["The Picture of Dorian Gray", "Oscar Wilde", "Classics"], 
    ["Brave New World", "Aldous Huxley", "Science Fiction"], 
    ["The Road", "Cormac McCarthy", "Dystopian Fiction"], 
    ["Frankenstein", "Mary Shelley", "Gothic Fiction"], 
    ["Moby-Dick", "Herman Melville", "Classics"], 
    ["Wuthering Heights", "Emily Brontë", "Gothic Fiction"], 
    ["Jane Eyre", "Charlotte Brontë", "Gothic Fiction"], 
    ["Dracula", "Bram Stoker", "Gothic Fiction"] 
] 
 
# Get user input for the book name 
user_book = input("Enter the book name: ") 
 
# Find the genre of the user-entered book 
user_genre = None 
for book in books_data: 
    if user_book.lower() in book[0].lower(): 
        user_genre = book[2] 
        break 
 
# Filter out books with the same genre as the user-entered book 
matching_books = [] 
for book in books_data: 
    if book[2] == user_genre and user_book.lower() not in book[0].lower(): 
        matching_books.append(book) 
 
# Print the matching books with numbers 
if matching_books: 
    for i, book in enumerate(matching_books, 1): 
        print(f"{i}. {book[0]} by {book[1]}") 
else: 
    print("No books found with the same genre as", user_book) 