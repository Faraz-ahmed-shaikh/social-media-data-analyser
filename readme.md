# Social Data Processor 🧠📊

A graphical user interface (GUI) tool built using Python and Tkinter for visualizing, cleaning, and analyzing social network data. The tool reads user and page data from a JSON file and provides intelligent features like friend and page recommendations.

---

## 📌 Features

- ✅ **View Raw Data**: Display all raw user and page data from the `data.json` file.
- 🧹 **Clean Data**:
  - Removes users with empty names.
  - Removes users with no friends or liked pages.
  - Eliminates duplicate friend entries.
  - Removes duplicate page records.
- 👥 **Friend Suggestions**: Suggests friends a user may know based on mutual connections.
- ❤️ **Page Suggestions**: Recommends pages a user may like based on the likes of similar users.

---

## 🖥️ GUI Overview

- A clean and modern Tkinter interface.
- Simple radio button selection for each operation.
- Optional input field for entering a user ID (required for friend/page recommendations).
- Scrollable results section for displaying outputs.

---

## 📁 File Structure

├── data.json # Original raw data (input)
├── cleanData.json # Output file with cleaned data
├── main.py # Main Python script with GUI and logic
├── README.md # This file




---

## 📋 Usage

### 1. Prepare your JSON data
Ensure your `data.json` file is in the following format:

```json
{
  "users": [
    {
      "id": 1,
      "name": "Alice",
      "friends": [2, 3],
      "liked_pages": [101, 102]
    },
    ...
  ],
  "pages": [
    {
      "id": 101,
      "name": "Tech World"
    },
    ...
  ]
}
```
### 2. Run the App 
  python main.py
### 3. Choose an Operation
Select one of the four operations using the radio buttons.
If using friend/page suggestion, enter a valid User ID before clicking Execute.
Results will be shown in the output area.

🛠️ Technologies Used
Python 3
Tkinter for GUI
JSON for data input/output

### 🙌 Author - Developed with 💡 and 🐍 by Faraz

