import tkinter as tk
from tkinter import messagebox
import json

def dataCollecting(Rawfilename):
    with open(Rawfilename, "r") as file:
        data = json.load(file)
        raw_data_text = "\nRaw Users Data:\n"
        for user in data["users"]:
            raw_data_text += f"ID - {user['id']}, Name - {user['name']}, Friends - {user['friends']}, Liked Pages - {user['liked_pages']}\n"
        
        raw_data_text += "\nRaw Pages Data:\n"
        for page in data["pages"]:
            raw_data_text += f"Page ID - {page['id']}, Page Name - {page['name']}\n"
        
        return raw_data_text

def cleanData():
    with open("data.json", "r") as file:
        data = json.load(file)
        data["users"] = [user for user in data["users"] if user["name"].strip()]
        data["users"] = [user for user in data["users"] if user['friends'] or user['liked_pages']]
        for user in data["users"]:
            user['friends'] = list(set(user['friends']))
        uniquePages = {}
        for page in data["pages"]:
            uniquePages[page['id']] = page
        data["pages"] = list(uniquePages.values())
        
        with open("cleanData.json", "w") as file:
            json.dump(data, file, indent=2)

        cleaned_data_text = "\nData Cleaned :)\nUsers Data:\n"
        for user in data["users"]:
            cleaned_data_text += f"ID - {user['id']}, Name - {user['name']}, Friends - {user['friends']}, Liked Pages - {user['liked_pages']}\n"
        
        cleaned_data_text += "\nPages Data:\n"
        for page in data["pages"]:
            cleaned_data_text += f"Page ID - {page['id']}, Page Name - {page['name']}\n"
        
        return cleaned_data_text

def findingPeopleYouMayKnow(userID):
    with open("cleanData.json", "r") as file:
        data = json.load(file)
        allfriends = {}
        for user in data["users"]:
            allfriends[user['id']] = user['friends']
        
        if userID not in allfriends:
            return "User doesn't Exist"
        
        onlyfriendsofuserID = allfriends[userID]
        suggestions = {}
        for friendofUserID in onlyfriendsofuserID:
            if friendofUserID not in allfriends:
                continue
            for otherfriend in allfriends[friendofUserID]:
                if otherfriend != userID and otherfriend not in onlyfriendsofuserID:
                    suggestions[otherfriend] = suggestions.get(otherfriend, 0) + 1
        
        sortedSuggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
        return f"Friend Suggestion for {userID} : ID no. {[suggestedFriend for suggestedFriend, _ in sortedSuggestions]}"

def findPagesYouMayLike(userID):
    with open("cleanData.json", "r") as file:
        data = json.load(file)
        allPages = {}
        for user in data['users']:
            allPages[user['id']] = user['liked_pages']
        
        if userID not in allPages:
            return f"{userID} does not exist in the records :("
        
        userLikedPages = set(allPages[userID])
        suggestedPages = {}
        for otherUsers, pages in allPages.items():
            if otherUsers != userID:
                sharedPages = userLikedPages.intersection(pages)
                for page in pages:
                    suggestedPages[page] = suggestedPages.get(page, 0) + len(sharedPages)
        
        sortedPages = sorted(suggestedPages.items(), key=lambda x: x[1], reverse=True)
        return f"User ID {userID} May like Page no. {[page for page, _ in sortedPages]}"

# Create the main window with modern styling
root = tk.Tk()
root.title("Social Data Processor")
root.geometry("700x600")
root.config(bg="#f5f5f5")

# Add a header and description with a clean layout
header_label = tk.Label(root, text="Social Media Data Processor", font=("Arial", 18, "bold"), fg="#4CAF50", bg="#f5f5f5")
header_label.pack(pady=20)

description_label = tk.Label(root, text="Choose an operation to process data from a social network database.", font=("Arial", 12), fg="#555", bg="#f5f5f5", wraplength=650)
description_label.pack(pady=10)

# Frame for options
frame_options = tk.Frame(root, bg="#f5f5f5")
frame_options.pack(pady=10)

selected_option = tk.IntVar()

# Create radio buttons for options with modern appearance
option_font = ("Arial", 12)
tk.Radiobutton(frame_options, text="View Raw Data", variable=selected_option, value=1, font=option_font, bg="#f5f5f5", anchor="w").pack(anchor="w", padx=20)
tk.Radiobutton(frame_options, text="Clean Data", variable=selected_option, value=2, font=option_font, bg="#f5f5f5", anchor="w").pack(anchor="w", padx=20)
tk.Radiobutton(frame_options, text="Find People You May Know", variable=selected_option, value=3, font=option_font, bg="#f5f5f5", anchor="w").pack(anchor="w", padx=20)
tk.Radiobutton(frame_options, text="Find Pages You May Like", variable=selected_option, value=4, font=option_font, bg="#f5f5f5", anchor="w").pack(anchor="w", padx=20)

# Entry field for user ID (for options 3 and 4)
entry_label = tk.Label(root, text="Enter User ID (for options 3 & 4):", font=("Arial", 12), bg="#f5f5f5")
entry_label.pack(pady=10)

entry_user_id = tk.Entry(root, font=("Arial", 12), width=40)
entry_user_id.pack(pady=5)

# Button to execute selected option with improved styling
btn_execute = tk.Button(root, text="Execute", command=display_data, font=("Arial", 14, "bold"), fg="white", bg="#4CAF50", relief="flat", width=20, height=2)
btn_execute.pack(pady=20)

# Text box for displaying results with a modern scroll bar
text_result_frame = tk.Frame(root, bg="#f5f5f5")
text_result_frame.pack(pady=10)

scrollbar = tk.Scrollbar(text_result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_result = tk.Text(text_result_frame, width=100, height=35, font=("Arial", 12), wrap=tk.WORD, yscrollcommand=scrollbar.set, bd=0, relief="flat", padx=10, pady=10)
text_result.pack()

scrollbar.config(command=text_result.yview)

# Run the main loop
root.mainloop()
