import os
from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)


def add_member():
    name = input("Member name: ").strip()
    email = input("Member email: ").strip()
    payload = {"name": name, "email": email}
    resp = sb.table("members").insert(payload).execute()
    print("Registered member:", resp.data)


def add_book():
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    category = input("Category: ").strip()
    stock = int(input("Stock quantity: ").strip())
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    print("Added book:", resp.data)


def update_book_stock():
    book_id = int(input("Book ID to update: ").strip())
    new_stock = int(input("New stock quantity: ").strip())
    resp = sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute()
    if resp.data:
        print("Updated book:", resp.data)
    else:
        print("No book found with that ID.")


def update_member_email():
    member_id = int(input("Member ID to update: ").strip())
    new_email = input("New email: ").strip()
    resp = sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()
    if resp.data:
        print("Updated member:", resp.data)
    else:
        print("No member found with that ID.")


def delete_member():
    member_id = int(input("Member ID to delete: ").strip())
    check = sb.table("borrow_records").select("record_id").eq("member_id", member_id).is_("return_date", None).execute()
    if check.data:
        print("Cannot delete. Member has borrowed books not returned.")
        return
    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    print("Deleted member:", resp.data)


def delete_book():
    book_id = int(input("Book ID to delete: ").strip())
    check = sb.table("borrow_records").select("record_id").eq("book_id", book_id).is_("return_date", None).execute()
    if check.data:
        print("Cannot delete. Book is currently borrowed.")
        return
    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    print("Deleted book:", resp.data)


def borrow_book():
    member_id = int(input("Member ID borrowing the book: ").strip())
    book_id = int(input("Book ID to borrow: ").strip())
    book_resp = sb.table("books").select("stock").eq("book_id", book_id).execute()
    if not book_resp.data:
        print("Book not found.")
        return
    stock = book_resp.data[0]["stock"]
    if stock < 1:
        print("Book out of stock.")
        return
    borrow_resp = sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()
    if borrow_resp.data:
        sb.table("books").update({"stock": stock - 1}).eq("book_id", book_id).execute()
        print("Borrowed successfully:", borrow_resp.data)
    else:
        print("Failed to borrow book.")


def return_book():
    record_id = int(input("Borrow record ID to return: ").strip())
    record_resp = sb.table("borrow_records").select("book_id, return_date").eq("record_id", record_id).execute()
    if not record_resp.data:
        print("Borrow record not found.")
        return
    record = record_resp.data[0]
    if record["return_date"]:
        print("Book already returned.")
        return
    now = datetime.utcnow().isoformat()
    update_resp = sb.table("borrow_records").update({"return_date": now}).eq("record_id", record_id).execute()
    if update_resp.data:
        book_resp = sb.table("books").select("stock").eq("book_id", record["book_id"]).execute()
        if book_resp.data:
            stock = book_resp.data[0]["stock"]
            sb.table("books").update({"stock": stock + 1}).eq("book_id", record["book_id"]).execute()
            print("Returned successfully.")
        else:
            print("Book not found to update stock.")
    else:
        print("Failed to update return.")


def list_books():
    books = sb.table("books").select("*").order("book_id").execute().data
    if books:
        for b in books:
            print(f"{b['book_id']}: {b['title']} by {b['author']} [{b['category']}] - Stock: {b['stock']}")
    else:
        print("No books available.")


def search_books():
    keyword = input("Search books (keyword): ").strip()
    results = sb.table("books").select("*").or_(
        f"title.ilike.%{keyword}%,author.ilike.%{keyword}%,category.ilike.%{keyword}%"
    ).execute().data
    if results:
        for b in results:
            print(f"{b['book_id']}: {b['title']} by {b['author']} [{b['category']}] - Stock: {b['stock']}")
    else:
        print("No matches found.")


def member_details():
    member_id = int(input("Member ID: ").strip())
    member_resp = sb.table("members").select("*").eq("member_id", member_id).execute()
    if not member_resp.data:
        print("Member not found.")
        return
    borrow_resp = sb.table("borrow_records").select("record_id, book_id, borrow_date, return_date, books(title, author)").eq("member_id", member_id).order("borrow_date", desc=True).execute().data or []
    print(f"Member: {member_resp.data[0]['name']} (Email: {member_resp.data[0]['email']})")
    print("Borrowed books:")
    for rec in borrow_resp:
        status = "Returned" if rec["return_date"] else "Borrowed"
        print(f" Record {rec['record_id']}: {rec['books']['title']} by {rec['books']['author']} - {status}")


def overdue_report():
    days = int(input("Overdue days threshold (default 30): ") or "30")
    threshold = (datetime.utcnow() - timedelta(days=days)).isoformat()
    overdue_list = sb.table("borrow_records").select("record_id, member_id, book_id, borrow_date, books(title), members(name)").lt("borrow_date", threshold).is_("return_date", None).execute().data
    if overdue_list:
        for rec in overdue_list:
            print(f"Record {rec['record_id']}: {rec['books']['title']} borrowed by {rec['members']['name']} on {rec['borrow_date']}")
    else:
        print("No overdue books.")


def menu():
    print("""
==== Library Management System ====
1. Register member
2. Add new book
3. Update book stock
4. Update member email
5. Delete member
6. Delete book
7. Borrow book
8. Return book
9. List all books
10. Search books
11. Show member details
12. Overdue books report
0. Exit
""")

    choice = input("Choose an option: ").strip()
    return choice


def main():
    while True:
        choice = menu()
        if choice == "1":
            add_member()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book_stock()
        elif choice == "4":
            update_member_email()
        elif choice == "5":
            delete_member()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            borrow_book()
        elif choice == "8":
            return_book()
        elif choice == "9":
            list_books()
        elif choice == "10":
            search_books()
        elif choice == "11":
            member_details()
        elif choice == "12":
            overdue_report()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
# Library_management_system.py
# Online Library Management System using Supabase/Postgres + Python
# Features:
# - Register members
# - Add, update, delete books
# - Borrow and return books
# - List and search books
# - View member details and overdue reports
# Requirements:
# - supabase (pip install supabase)
# - python-dotenv (pip install python-dotenv)
# Setup:
# 1. Create a Supabase account and project
# 2. Create tables: members, books, borrow_records
# 3. Get SUPABASE_URL and SUPABASE_KEY from project settings
# 4. Create a .env file with these keys
# 5. Run this script and interact via command line
# Note: This is a simplified example for educational purposes.
# Ensure to handle errors and edge cases in a production system.
# See accompanying notes for database schema and setup instructions.
# Database schema (SQL):
# CREATE TABLE members (
#     member_id serial PRIMARY KEY,
#     name text NOT NULL,
#     email text UNIQUE NOT NULL,
#     join_date timestamptz DEFAULT NOW()
# );
# CREATE TABLE books (
#     book_id serial PRIMARY KEY,
#     title text NOT NULL,
#     author text NOT NULL,
#     category text,
#     stock int NOT NULL DEFAULT 1
# );
# CREATE TABLE borrow_records (
#     record_id serial PRIMARY KEY,
#     member_id int REFERENCES members(member_id),
#     book_id int REFERENCES books(book_id),
#     borrow_date timestamptz DEFAULT NOW(),
#     return_date timestamptz
# );
