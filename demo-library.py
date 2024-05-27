class Book:
    def __init__(self,name,type,writer,publicationYear,isbn):
        self.name=name
        self.type=type
        self.writer=writer
        self.publicationYear=publicationYear
        self.isbn=isbn
        self.is_borrowed=False

       
    def __str__(self):
       return f"Kitap Adı : {self.name}, Türü :{self.type}, Yazarı : {self.writer}, Yayın Yılı : {self.publicationYear}, ISBN No: {self.isbn} {'[Ödünç Alınmış]' if self.is_borrowed else '[Mevcut]'} "


class Members:
    def __init__(self,name,membr_id):
        self.name=name
        self.member_id=membr_id
        self.borrowed_books = []    
        

    def borrow_book(self,book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} ödünç verildi. '{book.name}'")
        else:
            print(f"'{book.name}' Zaten Ödünç Verildi")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.is_borrowed=False
            self.borrowed_books.remove(book)
            print(f"{self.name} iade edildi '{book.name}'")
        else:
            print(f"{self.name} ödünç alınmadı. '{book.name}'")

    def __str__(self):
        return f"Üye {self.name} (Üye ID: {self.member_id}), Ödünç Alınan Kitap: {[book.title for book in self.borrowed_books]}"  
    

class Library:
    def __init__(self,name):
        self.name=name
        self.books = []
        self.members = [] 

    def add_book(self, book):
        self.books.append(book)
        print(f"Kitap Eklendi {book}")    

    def add_member(self, member):
        self.members.append(member)
        print(f"Üye Eklendi {member}")

    def list_books(self):
        return [str(book) for book in self.books]
    
    def list_members(self):
        return [str(member) for member in self.members]
    
    def __str__(self):
        return f"Library {self.name}"
    

library=Library("Şehir Kütüphanesi")

book1=Book('Ölüler Diyarı','Polisiye Roman','Jean-Christophe Grangé','2018','123456789')
book2=Book('İhanet Noktası','Gerilim , Sürükleyici , Bilim Kurgu','Dan Brown','2001','123456789')
book3=Book('Inferno','Gizem Sürükleyici, Gerilim','Dan Brown','2016','123456789')

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Members("Mesut", "M001")
member2 = Members("Özge", "M002")

library.add_member(member1)
library.add_member(member2)

print("\nTüm Kitaplar Listesi:")
for book in library.list_books():
    print(book)

print("\nKütüphanedeki tüm üyeler:")
for member in library.list_members():
    print(member)    

member1.borrow_book(book1)
member2.borrow_book(book1)  
member2.borrow_book(book2)
member1.return_book(book1)
member2.return_book(book2)
member1.borrow_book(book3)    