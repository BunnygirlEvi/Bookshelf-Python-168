class Bookshelf:
    
    def __init__(self, name, author, price, publishing_year):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_publishingyear = publishing_year
    
    def add_book(self):
        print("Book Name: "+self.book_name)
        print("Author: "+self.book_author)
        print("Price: "+self.book_price)
        print("Publishing Year: "+self.book_publishingyear)
        print("Book Added")
    
    def years_since_published(self):
        years = 2024 - int(self.book_publishingyear)
        print("Book was published "+str(years) + " years ago.")
        
Book1 = Bookshelf("Sunny Makes Her Case", "Jennifer L. Holm and Hatthew Holm", "20.00", "2024")
Book2 = Bookshelf("Emily Windsnap and the Ship of Lost Souls", "Liz Kessler", "7.00", "2015")
Book1.add_book()
Book1.years_since_published()
Book2.add_book()
Book2.years_since_published()
