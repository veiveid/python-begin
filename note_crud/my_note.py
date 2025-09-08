# -*- coding: UTF-8 -*-

NOTES_FILE = "notes.txt"  # note file

def show_menu():
    """show the menu"""
    print("\n=== note ===")
    print("1. add note")
    print("2. view all notes")
    print("3. delete all notes")
    print("4. quit")
    print("================")

def add_note():
    """add a new note"""
    note = input("please input note which you want:")
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(note + "\n")
        print("notes have been added！")

def view_notes():
    """view all notes"""
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = f.readlines()
            if notes:
                print("\nyour notes:")
                for i,note in enumerate(notes, 1):
                    print(f"{i}.{note.strip()}")

            else:
                print("no notes yet")
    except FileNotFoundError:
        print("notes file not found")

def delete_notes():
    """delete all notes"""
    open(NOTES_FILE, "w").close() # 清空文件
    print("all notes have been deleted")

def main():
    while True:
        show_menu()
        choice = input("please chose operate(1-4): ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("program has ended")
            break
        else:
            print("invalid choice please try again")

if __name__ == "__main__":
    main()




