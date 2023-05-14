class Book:
    def __init__(self, Title, author, price):
        self.title = Title
        self.author = author
        self.price = price

    def view(self):
        print(f"Book Title is : {self.title}")
        print(f"Book Author is : {self.author}")
        print(f"Book Price is : {self.price}")


if __name__ == "__main__":
    library = []
    while True:
        print("1. Add Book")
        print("2. View Book")
        print("3. Delete Book")
        print("4. Exit")
        print("Enter Your Choice : ", end="")
        choice = int(input())
        if choice == 1:
            title = input("Enter Book Title : ")
            author = input("Enter Book Author : ")
            price = int(input("Enter Book Price : "))
            book = Book(title, author, price)
            library.append(book)
        elif choice == 2:
            print("Enter Book Title : ")
            title = input()
            for book in library:
                if book.title == title:
                    book.view()
                    break
        elif choice == 3:
            print("Enter Book Title : ")
            title = input()
            for book in library:
                if book.title == title:
                    library.remove(book)
                    break
                else:
                    print("Book Not Found")
                    break
        elif choice == 4:
            break
        else:
            print("Enter correct choice")
