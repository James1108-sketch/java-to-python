import Book
import DVD

class Library:
    if __name__ == "__main__":
        book1 = Book("The Outsiders", "B001", "S.E. Hinton")
        dvd1 = DVD("Bill Nye the Science Guy", "D001", 120)
    print("Book Information:")
    print(book1)
    print()

    print("DVD Information:")
    print(dvd1)
    print()

    if book1.check_out():
        print(f"{book1.get_title()} has been checked out.")
    else:
        print(f"{book1.get_title()} is already checked out.")

    if book1.check_out():
        print(f"{book1.get_title()} has been checked out.")
    else:        
     print(f"{book1.get_title()} is not checked out.")

    print()

    if dvd1.check_out():
        print(f"{dvd1.get_title()} has been checked out.")
    else:
         print(f"{dvd1.get_title()} is already checked out.")
    if dvd1.check_out():
         print(f"{dvd1.get_title()} has been checked out.")
    else:
         print(f"{dvd1.get_title()} is not checked out.")

    print()
    print("Update DVD information:")
    print(dvd1)