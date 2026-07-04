import json

data = [
    {'title': 'laws of power', 'author': 'robert green', 'copies': 5},
    {'title': 'the mist', 'author': 'carl sandburg', 'copies': 5},
    {'title': 'the art of seduction', 'author': 'robert green', 'copies': 9}
]

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    p = json.load(f)

class person:
    def __init__(self, name):
        self.name = name

class member(person):

    def borrow(self, title):
        for t in p:
            if t['title'] == title:
                t['copies'] -= 1
        print(f'{title} borrowed by {self.name}')
        with open('data.json', 'w') as f:
            json.dump(p, f, indent=4)

    def return_book(self, title):
        for o in p:
            if o['title'] == title:
                o['copies'] += 1
        print(f'{title} returned by {self.name}')
        with open('data.json', 'w') as f:
            json.dump(p, f, indent=4)

class librarian(person):

    def add_book(self, title, author, copies):
        p.append({'title': title, 'author': author, 'copies': copies})
        with open('data.json', 'w') as f:
            json.dump(p, f, indent=4)

    def show_data(self):
        print(data)

while True:
    print("\n=== Library Management System ===")
    print("1. Show all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Add a book (librarian)")
    print("5. exit")
    

    choice = input("\nEnter your choice (1-6): ")

    if choice == '1':
        for r in p:
            print(r['title'], r['author'], r['copies'])

    elif choice == '2':
        name = input('enter your name :')
        title = input("Enter book title: ")
        m = member(name)
        m.borrow(title)

    elif choice == "3":
        name = input("Enter your name: ")
        title = input("Enter book title: ")
        m = member(name)
        m.return_book(title)

    elif choice == "4":
        name = input("Enter librarian name: ")
        title = input("Enter book title: ")
        author = input("Enter author: ")
        copies = int(input("Enter copies: "))
        l = librarian(name)
        l.add_book(title, author, copies)
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again")
