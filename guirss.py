import feedparser
import tkinter as tk

def show_articles():
    # Parse the RSS feed
    url = entry.get()
    feed = feedparser.parse(url)

    # Clear the listbox
    listbox.delete(0, tk.END)

    # Add the titles of the articles in the feed to the listbox
    for entry in feed.entries:
        listbox.insert(tk.END, entry.title)

# Create the main window
root = tk.Tk()
root.title("RSS Feed Reader")

# Create a label
label = tk.Label(root, text="Enter the URL of the RSS feed:")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button
button = tk.Button(root, text="Show Articles", command=show_articles)
button.pack()

# Create a listbox
listbox = tk.Listbox(root)
listbox.pack()

# Start the main event loop
root.mainloop()
