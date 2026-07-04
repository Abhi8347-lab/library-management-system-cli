# Library Management System CLI

A command-line application that simulates a real library —
members can borrow and return books, librarians can manage
the collection, and all data persists across sessions using JSON.

## The problem it solves

Most library demos lose all data when the program closes.
This one saves every borrow, return, and new addition
instantly to a JSON file — reopen it tomorrow and
your library is exactly where you left it.

## Features

- Borrow a book — copies reduce automatically
- Return a book — copies restore automatically  
- Add new books (librarian access)
- Search books by author
- View full catalog with live copy count
- All data saved to books.json after every action

## Concepts used

- OOP — Person, Member, Librarian class hierarchy
- Encapsulation — copy count changes only through methods
- Polymorphism — Member and Librarian behave differently
- Inheritance — both extend base Person class
- File handling — JSON read/write for persistence
- CLI — while loop menu for real user interaction

## How to run

git clone https://github.com/yourusername/library-management-system-cli
cd library-management-system-cli
python main.py

## What's coming next

- Exception handling for invalid inputs
- SQL database replacing JSON
- REST API with FastAPI
- Web frontend

## Built by

Abhi — building toward AIML engineering,
documenting every step publicly on GitHub.
