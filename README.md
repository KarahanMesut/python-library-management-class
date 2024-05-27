Students' Simple Python Library Management System / Öğrenciler İçin Basit Python Kütüphane Yönetim Sistemi
This project is a simple Library Management System created using the Python programming language. It allows for the management of books and members. Members can borrow and return books. The system tracks the current status of books and which member has borrowed which book.

Bu proje, Python programlama dili kullanılarak oluşturulmuş basit bir Kütüphane Yönetim Sistemi'dir. Kitapların ve üyelerin yönetimini sağlar. Üyeler kitap ödünç alabilir ve geri verebilir. Sistem, kitapların mevcut durumunu ve hangi üyenin hangi kitabı ödünç aldığını takip eder.

Features / Özellikler
Book Management: Add and list books.

Member Management: Add and list members.

Borrowing and Returning: Members can borrow and return books.

Kitap Yönetimi: Kitap ekleme, listeleme.

Üye Yönetimi: Üye ekleme, listeleme.

Ödünç Alma ve Geri Verme: Üyelerin kitap ödünç alabilmesi ve geri verebilmesi.

Classes Used / Kullanılan Sınıflar
Book
Stores information for each book:

title
author
isbn
is_borrowed (flag indicating if the book is borrowed)
Her bir kitap için şu bilgileri saklar:

title (başlık)
author (yazar)
isbn (ISBN numarası)
is_borrowed (ödünç alınıp alınmadığını belirten bayrak)
Member
Stores information for each member:

name
member_id
borrowed_books (list of borrowed books)
Her bir üye için şu bilgileri saklar:

name (isim)
member_id (üye numarası)
borrowed_books (ödünç alınan kitapların listesi)
Library
Stores and manages information for the library:

name
books (list of books)
members (list of members)
Kütüphane için şu bilgileri saklar ve yönetir:

name (isim)
books (kitapların listesi)
members (üyelerin listesi)

# Create a library / Kütüphane oluşturma
library = Library("City Library")

# Create some books / Kitap oluşturma
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1234567891")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567892")

# Add books to the library / Kitapları kütüphaneye ekleme
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create some members / Üye oluşturma
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")

# Add members to the library / Üyeleri kütüphaneye ekleme
library.add_member(member1)
library.add_member(member2)

# Borrow and return books / Kitap ödünç alma ve geri verme işlemleri
member1.borrow_book(book1)
member2.borrow_book(book1)  # Attempt to borrow an already borrowed book / Zaten ödünç alınmış kitabı ödünç almaya çalışmak
member2.borrow_book(book2)
member1.return_book(book1)
member2.return_book(book2)
member1.borrow_book(book3)

# List all books in the library / Kütüphanedeki tüm kitapları listeleme
print("\nAll books in the library / Kütüphanedeki tüm kitaplar:")
for book in library.list_books():
    print(book)

# List all members in the library / Kütüphanedeki tüm üyeleri listeleme
print("\nAll members in the library / Kütüphanedeki tüm üyeler:")
for member in library.list_members():
    print(member)

Installation and Running / Kurulum ve Çalıştırma
Clone the repository / Depoyu klonlayın

git clone https://github.com/KarahanMesut/python-library-management-class.git

Navigate to the project directory / Proje dizinine gidin:
cd python-library-management-class

Run the Python script / Python betiğini çalıştırın
python demo-library.py


Contributing / Katkıda Bulunma
If you would like to contribute, please open an issue or send a pull request.

Katkıda bulunmak isterseniz, lütfen bir issue açın veya bir pull request gönderin.

