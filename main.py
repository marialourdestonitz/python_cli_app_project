def main():
    
    try:
        
        bookList = []  
        infile = open("theBookList.txt", "r")
        line = infile.readline()
        while line:
            bookList.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    
    except FileNotFoundError:
        print("The theBookList.txt not found!")
        print("Starting a new book list!")
        bookList = []
    
    
    choice = 0
    while choice != 4:
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display books")
        print("4) Quit")
        choice = int(input())
        
        if choice == 1:
            print("Adding a book...")
            nBook=input("Enter of the name of the book>>>")
            nAuthor=input("Enter of the name of the author>>>")
            nPages=input("Enter of the number of pages>>>")
            bookList.append([nBook,nAuthor,nPages])
            
        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Search Term:")
            for book in bookList:
                if keyword in book:
                    print(book)
                    
        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(bookList)):
                print(bookList[i])
                
        elif choice == 4:
            print("Quitting Program")
        print("Program Terminated!")
        
        outfile=open("theBookList.txt", "w")
        for book in bookList:
            outfile.write(",".join(book) + "\n")
        outfile.close()

       

if __name__ == "__main__":
    main()
