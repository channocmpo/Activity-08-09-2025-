# 🐦 Django Tweet Posting Application

A Django web application that allows users to post tweets with optional images.  
The app blocks tweets containing the banned words: **"Shit"**, **"Fuck"**, and **"Bobo"**.

## 📌 Features
- Post tweets with **text** and an **optional image**.
- **Banned word filtering** before saving.
- Automatic timestamps for when tweets are created and updated.
- Uploaded images stored in `/media/tweets/`.

## 📥 How to Clone, Install, and Run

Follow these steps exactly to get the project running on your computer.

### 1️⃣ Install Python
Make sure you have **Python 3.x** installed.
- Check version:
  python --version
  or
  python3 --version
- If you don’t have Python, download it from:  
  https://www.python.org/downloads/

### 2️⃣ Clone the repository from GitHub
1. Open your terminal (or Command Prompt on Windows).
2. Navigate to the folder where you want to store the project:
   cd path/to/your/folder
3. Run:
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
4. Move into the project folder:
   cd YOUR-REPO-NAME

### 3️⃣ Create a virtual environment
This keeps your dependencies separate from your system Python.

Windows:
  python -m venv venv
Mac/Linux:
  python3 -m venv venv

### 4️⃣ Activate the virtual environment
Windows:
  venv\Scripts\activate
Mac/Linux:
  source venv/bin/activate
> When activated, you should see `(venv)` at the start of your terminal line.

### 5️⃣ Install project dependencies
  pip install -r requirements.txt
This will install Django, Pillow, and any other packages needed.

### 6️⃣ Apply database migrations
  python manage.py makemigrations
  python manage.py migrate
This creates the database tables needed for the app.

### 7️⃣ Create a superuser (admin account)
  python manage.py createsuperuser
- Enter a username, email, and password.
- You’ll use this account to log in and create tweets.

### 8️⃣ Run the development server
  python manage.py runserver
If successful, you’ll see:
  Starting development server at http://127.0.0.1:8000/

## ✍️ How to Create a Tweet
1. Open your browser and go to:
   http://127.0.0.1:8000/
2. Log in using your account.
3. Go to the **"Create Tweet"** page.
4. Enter tweet content (avoid banned words or you’ll get an error).
5. Optionally upload an image.
6. Click **Submit** to post your tweet.

## 📂 Project Structure
my_tweet_project/
│-- .gitignore
│-- manage.py
│-- requirements.txt
│-- README.md
│-- media/            (uploaded images)
│-- venv/             (virtual environment - excluded from Git)
│
├── app_name/
│   │-- models.py
│   │-- forms.py
│   │-- views.py
│   │-- urls.py
│   │-- templates/
│
├── my_tweet_project/
│   │-- settings.py
│   │-- urls.py
│   │-- wsgi.py

## 📌 Notes
- Ensure `.gitignore` excludes `venv/` and `db.sqlite3`.
- To modify banned words, edit the `BANNED_WORDS` list in `forms.py`.

## 📜 License
This project is open-source and can be used for educational purposes.
