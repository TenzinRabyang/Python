# First Module
# reading the data into dictionaries as book and bookrate
book = {}
for line in open("Books.csv", "r", encoding="ISO-8859-1"):
    (isbn,bookTitle,author,yearofpublication) = line.split(";")[0:4]
    book.setdefault(isbn.replace('"',''),{})
    book[isbn.replace('"','')] = bookTitle.replace('"',''), author.replace('"',''),yearofpublication.replace('"','')
    
bookrate = {}
for line in open("Book-Ratings.csv","r",encoding="ISO-8859-1"):
    (userID,isbn,rating) = line.split(";")
    bookrate[isbn.replace('"','')] = userID.replace('"',''), rating.replace('"','')

# Mearging both of dictionaries into one by ISBN in user_preference
user_preference = {}
for i in bookrate.keys():
    if i in book.keys():
        a = (book[i])
        b = (bookrate[i])
        c = a + b
        user_preference.setdefault(c[3],{})
        user_preference[c[3]][c[0]] =i,c[1],c[2],c[4]
