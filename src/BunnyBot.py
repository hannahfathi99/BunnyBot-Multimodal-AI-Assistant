# 1- Import library
import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import sqlite3
from tkinter import messagebox
from time import strftime


# 2-Read API_KEY
apiKey = open("API_KEY", "r").read().strip()

openai.api_key = apiKey

# 3-Switch windows function
def switch_to_window12():
    win1.withdraw()
    win2.deiconify()
    pass
def switch_to_window21():
    win2.withdraw()
    win1.deiconify()
    pass
def switch_to_window13():
    win1.withdraw()
    win3.deiconify()
    pass
def switch_to_window31():
    win3.withdraw()
    win1.deiconify()
    pass
def switch_to_window14():
    win1.withdraw()
    win4.deiconify()
    pass
def switch_to_window41():
    win4.withdraw()
    win1.deiconify()
    pass
def switch_to_window15():
    win1.withdraw()
    win5.deiconify()
    pass
def switch_to_window51():
      win5.withdraw()
      win1.deiconify()
      pass
def show_main_window():
    global register_page
    register_page.destroy()
    login_page.deiconify()
def switch_to_registration():
    login_page.withdraw()
    open_registration_page()

def switch_to_account():
    win1.withdraw()
    account_page.deiconify()
    pass

def switch_to_win1():
    account_page.withdraw()
    win1.deiconify()
    pass


# 4-Date and Time function
def digital_time():
    time_string = strftime('%H:%M:%S%p\n%d/%m/%Y')
    time.config(text=time_string)
    time.after(1000, digital_time)


# 5-Create a database
user_conn = sqlite3.connect('user_database.db')
user_cursor = user_conn.cursor()

# 6-Create a new table
user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        mobile_number TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        birth_date DATE,
        gender TEXT,
        country TEXT,
        email TEXT,
        password TEXT
    )
''')

user_conn.commit()


register_page = None
entry_first_name = None
entry_last_name = None
entry_birt_date = None
var_gender = None
entry_country = None
entry_mobile = None
entry_email = None
entry_password = None

# 7-Store in database
def save_to_database():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    birth_date = entry_birt_date.get()
    gender = var_gender.get()
    country = entry_country.get()
    mobile_number = entry_mobile.get()
    email = entry_email.get()
    password = entry_password.get()

    # Validation checks
    if not password.isdigit() or len(password) < 8:
        messagebox.showerror("Invalid Password", "Password must contain only numbers and more than 8 characters.")
        return

    if not mobile_number.isdigit() or len(mobile_number) != 11:
        messagebox.showerror("Invalid Mobile Number", "Mobile number should contain only numbers and 11 characters.")
        return

    if not (first_name.isalpha() and last_name.isalpha() and country.isalpha()):
        messagebox.showerror("Invalid Characters", "First name and last name and country should only contain alphabetic characters.")
        return

    # Check if the mobile number or email is already registered
    user_cursor.execute('SELECT * FROM users WHERE mobile_number=? OR email=?', (mobile_number, email))
    existing_user = user_cursor.fetchone()

    if existing_user:
        # Notify the user about the attempt to re-register
        messagebox.showerror("Registration Failed", "This mobile number or email is already registered. If you forgot your password, use the login page.")
        return

    # Insert user data into the database
    user_cursor.execute('''
        INSERT INTO users (mobile_number, first_name, last_name, birth_date, gender,country, email, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (mobile_number, first_name, last_name, birth_date, gender, country, email, password))
    user_conn.commit()

    # Notify the user about successful registration
    messagebox.showinfo("Registration Successful", "Registration Successful,Use mobile number as username" )

#register_page
def open_registration_page():
    global register_page, entry_first_name, entry_last_name, entry_birt_date, var_gender, entry_country, entry_mobile, entry_email, entry_password

# 8-Create register_page
    register_page = tk.Toplevel(login_page)
    register_page.title("Registration Form")
    register_page.resizable(False, False)
    register_page.geometry("830x545")
    register_page.configure(background="white")

    register_page_frame1=tk.Frame(register_page,padx=70,pady=40)
    register_page_frame1.configure(background="pink")
    register_page_frame1.grid(row=0, column=1)

    register_page_frame2=tk.Frame(register_page,padx=20,pady=20)
    register_page_frame2.configure(background="white")
    register_page_frame2.grid(row=0, column=0)

    label_register_page = tk.Label(register_page_frame1, text="Bunny_bot", font=("Courier", 25, 'bold'), foreground='silver')
    label_register_page.configure(background='white')
    label_register_page.grid(row=0, column=2, padx=20, pady=110)
    label_first_name = tk.Label(register_page_frame2, text="First Name:",font=("Courier", 12, 'bold'), foreground='black')
    label_first_name.configure(background="white")
    label_first_name.grid(row=0, column=0, padx=10, pady=1)
    entry_first_name = tk.Entry(register_page_frame2,width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_first_name.grid(row=0, column=1, padx=10, pady=10)

    label_last_name = tk.Label(register_page_frame2, text="Last Name:",font=("Courier", 12, 'bold'), foreground='black')
    label_last_name.configure(background='white')
    label_last_name.grid(row=1, column=0, padx=10, pady=10)
    entry_last_name = tk.Entry(register_page_frame2,width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_last_name.grid(row=1, column=1, padx=10, pady=10)

    label_birth_date = tk.Label(register_page_frame2, text="Birth Date (YYYY-MM-DD):",font=("Courier", 12, 'bold'), foreground='black')
    label_birth_date.configure(background='white')
    label_birth_date.grid(row=2, column=0, padx=10, pady=10)
    entry_birt_date = tk.Entry(register_page_frame2,width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_birt_date.grid(row=2, column=1, padx=10, pady=10)

    label_gender = tk.Label(register_page_frame2, text="Gender:",font=("Courier", 12, 'bold'), foreground='black')
    label_gender.configure(background='white')
    label_gender.grid(row=3, column=0, padx=10, pady=10)
    var_gender = tk.StringVar(register_page_frame2)
    var_gender.set("ّFemale")
    gender_menu = tk.OptionMenu(register_page_frame2, var_gender, "Female", "Male")
    gender_menu.configure(background="white",font=("Courier", 10, 'bold'), foreground='black',relief="solid")
    gender_menu.grid(row=3, column=1, columnspan=1, padx=10, pady=10, sticky="s")

    label_country = tk.Label(register_page_frame2, text="Country:",font=("Courier", 12, 'bold'), foreground='black')
    label_country.configure(background='white')
    label_country.grid(row=4, column=0, padx=10, pady=10)
    entry_country = tk.Entry(register_page_frame2,width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_country.grid(row=4, column=1, padx=10, pady=10)

    label_mobile = tk.Label(register_page_frame2, text="Mobile Number:",font=("Courier", 12, 'bold'), foreground='black')
    label_mobile.configure(background='white')
    label_mobile.grid(row=5, column=0, padx=10, pady=10)
    entry_mobile = tk.Entry(register_page_frame2,width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_mobile.grid(row=5, column=1, padx=10, pady=10)

    label_email = tk.Label(register_page_frame2, text="Email:",font=("Courier", 12, 'bold'), foreground='black')
    label_email.configure(background='white')
    label_email.grid(row=6, column=0, padx=10, pady=10)
    entry_email = tk.Entry(register_page_frame2,width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_email.grid(row=6, column=1, padx=10, pady=10)

    label_password = tk.Label(register_page_frame2, text="Password:",font=("Courier", 12, 'bold'), foreground='black')
    label_password.configure(background='white')
    label_password.grid(row=7, column=0, padx=10, pady=10)
    entry_password = tk.Entry(register_page_frame2, show="*",width=14,font=("Courier", 12,"bold"),relief="solid")
    entry_password.grid(row=7, column=1, padx=10, pady=10)

    button_submit = tk.Button(register_page_frame1, text="Register",font=("Courier", 12, 'bold'), foreground='black', command=save_to_database)
    button_submit.configure(background='white')
    button_submit.grid(row=1, column=2, columnspan=1, padx=20, pady=20)

    back_to_login_button = tk.Button(register_page_frame1, text=" Login  ",font=("Courier", 12, 'bold'), foreground='black', command=show_main_window)
    back_to_login_button.configure(background='white')
    back_to_login_button.grid(row=2, column=2, columnspan=1, padx=20, pady=20)

    exit_button = tk.Button(register_page_frame1, text="  Exit  ",font=("Courier", 12, 'bold'), foreground='black', command=register_page.destroy)
    exit_button.configure(background='white')
    exit_button.grid(row=3, column=2, columnspan=1, padx=20 ,pady=20)


user_mobile_number = None

def switch_to_window1():
    global user_mobile_number
    username = username_entry.get()
    password2 = password2_entry.get()
    user_cursor.execute('SELECT * FROM users WHERE mobile_number=? AND password=?', (username, password2))
    user_data = user_cursor.fetchone()
    if not username or not password2:
        messagebox.showerror("Empty Fields", "Please enter both username and password.")
        return
    if user_data:
        if username == user_data[0] and password2 == user_data[7]:
            messagebox.showinfo("Login Successful", "Welcome to the program")
            login_page.withdraw()
            win1.deiconify()
            user_mobile_number = username  # store the logged in user's mobile number

        elif username == user_data[0] and password2 != user_data[7]:
            messagebox.showerror("Login Failed", "Incorrect password. Please try again.")
            return
    else:
        messagebox.showerror("Login Failed", "User not found. Please register first.")
        return


# 9-Create login_page
login_page = tk.Tk()
login_page.title("Login Page")
login_page.resizable(False, False)
login_page.geometry("830x545")
login_page.iconphoto(True, tk.PhotoImage(file='C:\\Users\\irantech24\\Desktop\\Bunnt_bot(AI Assistant)\\photo\\pxfuel1.png'))
login_page_frame = tk.Frame(login_page, padx=20, pady=20)
login_page_frame.configure(background="pink")
login_page_frame.grid()
background_image2=tk.PhotoImage(file="C:\\Users\\irantech24\\Desktop\\Bunnt_bot(AI Assistant)\\photo\\bunny1.png")
background_login_page = tk.Label(login_page_frame, image=background_image2)
background_login_page.grid(row=0, column=2,columnspan=1, padx=30, pady=30,sticky='s')

login_page_label = tk.Label(login_page_frame, text="Login", font=("Courier", 40, 'bold'), foreground='white')
login_page_label.configure(background="pink")
login_page_label.grid(row=0, column=0,columnspan=2, padx=40,pady=90,sticky='s')

username_label = tk.Label(login_page_frame, text="Username:",font=("Courier", 14))
username_label.configure(background="pink")
username_label.grid(row=1, column=0,columnspan=1, padx=40, pady=10)
username_entry = tk.Entry(login_page_frame, width=20,font=("Courier", 12,"bold"),relief="solid")
username_entry.configure(background="white")
username_entry.grid(row=1, column=1,columnspan=1, padx=20, pady=10)

password2_label = tk.Label(login_page_frame, text="Password:",font=("Courier", 14))
password2_label.configure(background="pink")
password2_label.grid(row=2, column=0,columnspan=1, padx=40, pady=10)
password2_entry = tk.Entry(login_page_frame, show="*",font=("Courier", 12,"bold"),relief="solid")
password2_entry.grid(row=2, column=1,columnspan=1, padx=20, pady=15)


button_frame = tk.Frame(login_page, padx=20, pady=30)
button_frame.configure(background="white")
button_frame.grid()

buttons_login_page = [
    ("    Login     ", switch_to_window1),
    ("Create account", switch_to_registration),
    ("     Exit     ", login_page.quit),
]

for i, (request0, command) in enumerate(buttons_login_page):
    button0 = tk.Button(login_page_frame, text=request0, fg="black", font=("Courier", 10,'bold'), command=command)
    button0.configure(background="white")
    button0.grid(row=i+1, column=2,padx=50, pady=10,sticky='s')

# 10-Create the window1
win1 = tk.Toplevel()
win1.title("Bunny_bot")
win1.resizable(False, False)
win1.geometry("830x545")
win1.withdraw()

frame = tk.Frame(win1, padx=10, pady=10)
frame.configure(background="white")
frame.grid()
background_image1=tk.PhotoImage(file="C:\\Users\\irantech24\\Desktop\\Bunnt_bot(AI Assistant)\\photo\\pxfuel1.png")
background_label = tk.Label(frame, image=background_image1)
background_label.grid(row=1, column=1,columnspan=1, padx=20, pady=10)
win1_label = tk.Label(frame, text="Hi,I'm Bunny_bot", font=("Courier", 25, 'bold'), foreground='silver')
win1_label.configure(background="white")
win1_label.grid(row=1, column=0,columnspan=1, padx=20, pady=10)

time = tk.Label(frame,font=("Courier", 10, 'bold'),pady=8,foreground='black')
time.configure(background="white")
time.grid(row=0,column=0,sticky="nw")
digital_time()

account_button = tk.Button(frame, text="Account", command=switch_to_account)
account_button.configure(background="white")
account_button.grid(row=1, column=0, sticky="nw")


button_frame = tk.Frame(win1, padx=5, pady=30)
button_frame.configure(background="pink")
button_frame.grid()

buttons1 = [
    ("Voice Assistant", switch_to_window12),
    ("Generate Image", switch_to_window13),
    ("  Translator  ", switch_to_window14),
    ("   Notepad    ", switch_to_window15),
    ("    Exit     ", win1.quit),
]

for i, (request1, command) in enumerate(buttons1):
    button1 = tk.Button(button_frame, text=request1, fg="black", font=("Courier", 12, "bold"), command=command)
    button1.configure(background="white")
    button1.grid(row=0, column=i, padx=5, pady=0)

# 11-Create the window2
def create_database_table():
    user_conn = sqlite3.connect('user_database.db')
    user_cursor = user_conn.cursor()
    user_cursor.execute('''CREATE TABLE IF NOT EXISTS conversation (
                 id INTEGER PRIMARY KEY,
                 user_query TEXT,
                 assistant_response TEXT,
                 mobile_number TEXT
                 )''')
    user_conn.commit()

def insert_conversation(user_query, assistant_response,mobile_number):
    user_conn = sqlite3.connect('user_database.db')
    user_cursor = user_conn.cursor()
    user_cursor.execute("INSERT INTO conversation (user_query, assistant_response, mobile_number) VALUES (?, ?, ?)",
              (user_query, assistant_response, mobile_number))
    user_conn.commit()


win2 = tk.Tk()
win2.title("Bunny_bot")
win2.resizable(False, False)
win2.geometry("830x545")
win2.configure(bg="pink")
win2.withdraw()

message_listbox = tk.Listbox(win2, height=10, width=50, font=("Courier", 12, "bold"), relief="solid")
message_listbox.configure(background="white")
message_listbox.grid(row=0, column=2, columnspan=1, pady=24, padx=0, sticky="e")

response_text = tk.Text(win2, height=10, width=50, font=("Courier", 12, "bold"), relief="solid")
response_text.configure(background="white")
response_text.grid(row=1, column=2, columnspan=1, pady=5, padx=0, sticky="e")

win2_label = tk.Label(win2, text="Voice Assistant", font=("Courier", 15, 'bold'), foreground='gray')
win2_label.configure(background="white")
win2_label.grid(row=0, column=0, padx=30, pady=30, sticky="e")


def listen():
    def process_audio():
        speech = sr.Recognizer()
        audio = ''

        with sr.Microphone() as source:
            response_text.delete("1.0", tk.END)
            response_text.insert(tk.END, "Listening...\n")
            win2.update_idletasks()
            audio = speech.listen(source)

        try:
            text = speech.recognize_google(audio, language="en-US")
            response_text.insert(tk.END, f"You said: {text}\n")
            response_text.insert(tk.END, "Processing...\n")
            win2.update_idletasks()

            response = chat_with_openai(text)
            response_text.insert(tk.END, f"Assistant: {response}\n")
            speak(response)
            message_listbox.insert(tk.END, f"You: {text}")
            message_listbox.insert(tk.END, f"Assistant: {response}\n")
            insert_conversation(text, response, user_mobile_number)

        except sr.UnknownValueError:
            response_text.insert(tk.END, "Sorry, I can't hear you.\n")

        except sr.RequestError as e:
            response_text.insert(tk.END, f"Could not request results; {str(e)}\n")

    threading.Thread(target=process_audio).start()


def chat_with_openai(user_query):
    chat_log.append({"role": "user", "content": user_query})
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=chat_log
    )
    assistant_response = response['choices'][0]['message']['content']
    chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})
    return assistant_response.strip("\n").strip()

def speak(text):
    voice = pyttsx3.init()
    voice.say(text)
    voice.runAndWait()


frame2 = tk.Frame(win2, padx=30, pady=30)
frame2.configure(background="pink")
frame2.grid(row=1, column=0, sticky="s")

listen_button2 = tk.Button(frame2, text="Listen", fg="black", font=("Courier", 12, "bold"), command=listen)
listen_button2.configure(background="white")
listen_button2.grid(row=0, column=0, padx=10, pady=20, sticky="s")

back_button2 = tk.Button(frame2, text=" Back ", fg="black", font=("Courier", 12, "bold"), command=switch_to_window21)
back_button2.configure(background="white")
back_button2.grid(row=1, column=0, padx=10, pady=20, sticky="s")

exit_button2 = tk.Button(frame2, text=" Exit ", fg="black", font=("Courier", 12, "bold"), command=win2.quit)
exit_button2.configure(background="white")
exit_button2.grid(row=2, column=0, padx=10, pady=20, sticky="s")

chat_log = []

create_database_table()

# 12-Create the window3
win3 = tk.Tk()
win3.title("Bunny_bot")
win3.resizable(False,False)
win3.geometry("830x545")
win3.configure(background="pink")
win3.withdraw()

def open_url():
    url = url_entry.get()
    webbrowser.open("https://www.google.com/search?q=" + url)

entry_frame3 = tk.Frame(win3)
entry_frame3.configure(background="pink")
entry_frame3.grid(row=0, column=0, padx=0, pady=0, sticky="w")

webbrowser_label=tk.Label(entry_frame3, text=" Web Browser ", font=("Courier", 20, "bold"),fg="gray")
webbrowser_label.configure(background='pink')
webbrowser_label.grid(row=0, column=1, padx=20, pady=20)

url_label = tk.Label(entry_frame3, text="Enter URL:", font=("Courier", 12, "bold"),fg="black")
url_label.configure(background='pink')
url_label.grid(row=1, column=0, padx=15, pady=0)

url_entry = tk.Entry(entry_frame3, width=31, font=("Courier", 12,"bold"),relief="solid")
url_entry.configure(background="white")
url_entry.grid(row=1, column=1, padx=77, pady=0)

open_button = tk.Button(entry_frame3, text="     Open     ", command=open_url, font=("Courier", 12,"bold"))
open_button.configure(background="white")
open_button.grid(row=1, column=2, padx=24, pady=30)

def generate_image():
    user_input = prompt_entry.get()

    response = openai.Image.create(
        prompt=user_input,
        n=1,
        size="1024x1024",
        api_key=apiKey
    )

    image_url = response.data[0].url
    result_label.config(text=image_url)
    view_image_button.config(state=tk.NORMAL)

def view_image():
    image_url = result_label.cget("text")
    webbrowser.open_new_tab(image_url)

prompt_frame3 = tk.Frame(win3)
prompt_frame3.configure(background="white")
prompt_frame3.grid(row=1, column=0, padx=0, pady=0, sticky="w")

generate_image_label=tk.Label(prompt_frame3, text=" Generate Image ", font=("Courier", 20, "bold"),fg="gray")
generate_image_label.configure(background='white')
generate_image_label.grid(row=0, column=1, padx=20, pady=20)

prompt_label = tk.Label(prompt_frame3, text="Enter your prompt:", font=("Courier", 12, "bold"))
prompt_label.configure(background="white")
prompt_label.grid(row=1, column=0, padx=15, pady=20, sticky="w")

prompt_entry = tk.Entry(prompt_frame3, width=30, font=("Courier", 12,"bold"),relief="solid")
prompt_entry.configure(background="white")
prompt_entry.grid(row=1, column=1, padx=5, pady=20)

result_label = tk.Label(prompt_frame3, text="",width=37, font=("Courier", 10))
result_label.configure(background="white")
result_label.grid(row=2, column=1, padx=5, pady=20, sticky="w")

generate_button = tk.Button(prompt_frame3, text="Generate Image", command=generate_image, font=("Courier", 12, "bold"))
generate_button.configure(background="white")
generate_button.grid(row=1, column=2, padx=100, pady=10)

view_image_button = tk.Button(prompt_frame3, text="  View Image  ", command=view_image, state=tk.DISABLED, font=("Courier", 12, "bold"))
view_image_button.configure(bg="white")
view_image_button.grid(row=2, column=2, padx=100, pady=30)

back_button3 = tk.Button(win3, text=" Back ", font=("Courier", 12, "bold"),command=switch_to_window31)
back_button3.configure(background="white")
back_button3.grid(row=2, column=0, padx=37, pady=75,sticky="w")

exit_button3 = tk.Button(win3, text=" Exit ", font=("Courier", 12, "bold"), command=win3.quit)
exit_button3.configure(background="white")
exit_button3.grid(row=2, column=0, padx=88, pady=75,sticky="e")


# 13-Create the window4
user_conn = sqlite3.connect('user_database.db')
user_cursor= user_conn.cursor()

user_cursor.execute('''CREATE TABLE IF NOT EXISTS Translate_history (
             source_text TEXT,
             source_language TEXT,
             translated_text TEXT,
             target_language TEXT,
             mobile_number TEXT
             )''')
user_conn.commit()

def translate_text():
    source_text = source_text_entry.get(1.0, "end-1c")
    source_language = source_language_var.get()
    target_language = target_language_var.get()


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Translate the following text from {source_language} to {target_language}: {source_text}"}
        ]
    )

    translated_text = response['choices'][0]['message']['content'].strip()

    output_text.delete(1.0, "end")
    output_text.insert(1.0, translated_text)


    user_cursor.execute("INSERT INTO Translate_history (source_text, source_language, translated_text, target_language, mobile_number) VALUES (?, ?, ?, ?, ?)",
                        (source_text, source_language, translated_text, target_language, user_mobile_number))
    user_conn.commit()



# 14-Create the window4
win4 = tk.Tk()
win4.title("Bunny_bot")
win4.resizable(False,False)
win4.geometry("830x545")
win4.configure(background="pink")
win4.withdraw()

win4_label = tk.Label(win4, text="Text Translate",fg="gray",font=("Courier", 20,"bold"))
win4_label.configure(background="white")
win4_label.grid(row=0, column=0, padx=5, pady=5,sticky="n")

source_text_entry = tk.Text(win4, width=37, height=13,font=("Courier", 12,"bold"),relief="solid")
source_text_entry.configure(background="white")
source_text_entry.grid(row=1, column=0, columnspan=3, padx=20, pady=20,sticky="e")

output_text = tk.Text(win4, wrap=tk.WORD, width=37, height=13,font=("Courier", 12,"bold"),relief="solid")
output_text.configure(background="white")
output_text.grid(row=1, column=3, columnspan=3, padx=20, pady=20,sticky="w")

source_language_label = tk.Label(win4, text="Source Language",font=("Courier", 12,"bold"))
source_language_label.configure(background="white")
source_language_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="s")

source_language_var = tk.StringVar(win4)
source_language_var.set("English")

source_language_menu = tk.OptionMenu(win4, source_language_var, "English","Spanish", "French", "German", "Chinese", "Persian","Korean", "Italian", "Russian")
source_language_menu.configure(background="white")
source_language_menu.grid(row=3, column=0, columnspan=3, padx=10, pady=10,sticky="s")

target_language_label = tk.Label(win4, text="Target Language",font=("Courier", 12,"bold"))
target_language_label.configure(background="white")
target_language_label.grid(row=2, column=4, columnspan=5, padx=10, pady=10, sticky="s")

target_language_var = tk.StringVar(win4)
target_language_var.set("Persian")

target_language_menu = tk.OptionMenu(win4, target_language_var, "English", "Spanish", "French", "German", "Chinese", "Persian","Korean", "Italian", "Russian")
target_language_menu.configure(background="white")
target_language_menu.grid(row=3, column=4, columnspan=5, padx=10, pady=10,sticky="s")

translate_button = tk.Button(win4, text="Translate",font=("Courier", 12,"bold"), command=translate_text)
translate_button.configure(background="white")
translate_button.grid(row=4, column=0, columnspan=9, padx=10, pady=10,sticky="n")

back_button4 = tk.Button(win4, text=" Back ",fg="black",font=("Courier", 12,"bold"), command=switch_to_window41)
back_button4.configure(background="white")
back_button4.grid(row=5, column=0,padx=30, pady=10,sticky="w")

exit_button4 = tk.Button(win4, text=" Exit ",fg="black",font=("Courier", 12,"bold"), command=win4.quit)
exit_button4.configure(background="white")
exit_button4.grid(row=5,column=5, padx=30, pady=10,sticky="e")


# 15-Create the window5
win5 = tk.Tk()
win5.title("Bunny_bot")
win5.resizable(False, False)
win5.geometry("830x545")
win5.configure(background="pink")
win5.withdraw()

win5_label = tk.Label(win5, text=" Notepad ", font=("Courier", 20, "bold"), fg="gray")
win5_label.configure(background="white")
win5_label.pack(padx=15, pady=15, anchor="w")

user_conn = sqlite3.connect("user_database.db")
user_cursor = user_conn.cursor()
user_cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        note TEXT NOT NULL,
        mobile_number TEXT
    )
''')
user_conn.commit()

def get_notes_by_mobile_number(mobile_number):
    cursor = user_conn.cursor()
    cursor.execute("SELECT * FROM notes WHERE mobile_number=?", (mobile_number,))
    notes = cursor.fetchall()
    return notes

def add_note():
    subject = subject_entry.get()
    note_text = note_text_widget.get(1.0, tk.END)
    if subject.strip() and note_text.strip():
        user_cursor.execute('INSERT INTO notes (subject, note, mobile_number) VALUES (?, ?, ?)',
                            (subject, note_text, user_mobile_number))
        user_conn.commit()
        load_notes()
        clear_text()
    else:
        messagebox.showerror("Error", "Subject and note text cannot be empty.")

def delete_note():
    selected_index = note_listbox.curselection()
    if selected_index:
        notes = get_notes_by_mobile_number(user_mobile_number)
        note_id, _, _, mobile_number = notes[selected_index[0]]
        if mobile_number == user_mobile_number:
            user_cursor.execute('DELETE FROM notes WHERE id=?', (note_id,))
            user_conn.commit()
            load_notes()
            clear_text()
        else:
            messagebox.showerror("Error", "You can only delete your own notes.")

def update_note():
    selected_index = note_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        subject = subject_entry.get()
        note_text = note_text_widget.get(1.0, tk.END)
        if subject.strip() and note_text.strip():
            selected_note_id = note_listbox.get(index).split(':')[0]
            user_cursor.execute('SELECT mobile_number FROM notes WHERE id=?', (selected_note_id,))
            result = user_cursor.fetchone()
            if result is None:
                messagebox.showerror("Error", "Note not found.")
                return
            note_owner_mobile_number = result[0]
            if note_owner_mobile_number == user_mobile_number:
                user_cursor.execute('UPDATE notes SET subject=?, note=? WHERE id=?',
                                    (subject, note_text, selected_note_id))
                user_conn.commit()
                load_notes()
                clear_text()
            else:
                messagebox.showerror("Error", "You can only edit your own notes.")
        else:
            messagebox.showerror("Error", "Subject and note text cannot be empty.")
    else:
        messagebox.showerror("Error", "No note selected.")

def load_notes():
    global notes
    note_listbox.delete(0, tk.END)
    notes = get_notes_by_mobile_number(user_mobile_number)
    for note in notes:
        note_listbox.insert(tk.END, f"{note[0]}: {note[1]}: {note[2]}")

def on_note_select(event):
    selected_index = note_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        selected_note = note_listbox.get(index)
        parts = selected_note.split(':')
        if len(parts) == 3:
            subject, note = parts[1], parts[2].strip()
            subject_entry.delete(0, tk.END)
            subject_entry.insert(tk.END, subject.strip())
            note_text_widget.delete(1.0, tk.END)
            note_text_widget.insert(tk.END, note.strip())
        else:
            messagebox.showerror("Error", "Invalid note format.")

def clear_text():
    subject_entry.delete(0, tk.END)
    note_text_widget.delete(1.0, tk.END)


subject_label = tk.Label(win5, text="Enter Subject:", font=("Courier", 10, "bold"))
subject_label.configure(background="white")
subject_label.pack()

subject_entry = tk.Entry(win5, font=("Courier", 10, "bold"))
subject_entry.configure(background="white")
subject_entry.pack(padx=5, pady=5)

note_frame5 = tk.Frame(win5, padx=20, pady=20)
note_frame5.configure(background="white")
note_frame5.pack(anchor="n")

note_listbox = tk.Listbox(note_frame5, width=30, height=18, relief="solid", selectmode=tk.SINGLE)
note_listbox.configure(background="pink")
note_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True, side="left")

note_text_widget = tk.Text(note_frame5, width=70, height=18, relief="solid", wrap=tk.WORD)
note_text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

button_frame5 = tk.Frame(win5, padx=5, pady=20)
button_frame5.configure(background="pink")
button_frame5.pack()

buttons5 = [
    ("   Back   ", switch_to_window51),
    ("  Delete  ", delete_note),
    ("   Edit   ", update_note),
    ("    Add   ", add_note),
    ("   Exit   ", win5.quit),
]

for i, (request5, command) in enumerate(buttons5):
    button5 = tk.Button(button_frame5, text=request5, fg="black", font=("Courier", 12, "bold"), command=command)
    button5.configure(background="white")
    button5.grid(row=0, column=i, padx=22, pady=0)

load_notes()

note_listbox.bind('<<ListboxSelect>>', on_note_select)



# 16-Create account_page
def get_records_by_mobile_number(mobile_number):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conversation WHERE mobile_number=?", (mobile_number,))
    records = cursor.fetchall()
    return records

def show_voice_assistant_history():
    mobile_number = user_mobile_number
    records = get_records_by_mobile_number(mobile_number)
    if records:
        account_history.delete(1.0, tk.END)
        for record in records:
            account_history.insert(tk.END, f"User: {record[1]} *** Assistant: {record[2]}      \n")
    else:
        account_history.delete(1.0, tk.END)
        account_history.insert(tk.END, "No records found for the given mobile number.")


def get_translate_history_by_mobile_number(mobile_number):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Translate_history WHERE mobile_number=?", (mobile_number,))
    records = cursor.fetchall()
    return records

def show_translate_history():
    mobile_number = user_mobile_number
    records = get_translate_history_by_mobile_number(mobile_number)
    if records:
        account_history.delete(1.0, tk.END)
        for record in records:
            account_history.insert(tk.END ,f"Source text: {record[0]} ///Source language: {record[1]} ///target text: {record[2]} ///target language: {record[3]}   \n" )
    else:
        account_history.delete(1.0, tk.END)
        account_history.insert(tk.END, "No Translate History found for the given mobile number.")


def get_user_profile_by_mobile_number(mobile_number):
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE mobile_number=?", (mobile_number,))
    user_profile = cursor.fetchone()
    return user_profile


def show_user_profile():
    mobile_number = user_mobile_number
    user_profile = get_user_profile_by_mobile_number(mobile_number)
    if user_profile:
        account_history.delete(1.0, tk.END)
        account_history.insert(tk.END, "User Profile:\n")
        account_history.insert(tk.END, f"Mobile Number: {user_profile[0]}\n")
        account_history.insert(tk.END, f"First Name: {user_profile[1]}\n")
        account_history.insert(tk.END, f"Last Name: {user_profile[2]}\n")
        account_history.insert(tk.END, f"Birth Date: {user_profile[3]}\n")
        account_history.insert(tk.END, f"Gender: {user_profile[4]}\n")
        account_history.insert(tk.END, f"Country: {user_profile[5]}\n")
        account_history.insert(tk.END, f"Email: {user_profile[6]}\n")
    else:
        account_history.delete(1.0, tk.END)
        account_history.insert(tk.END, "No user profile found for the given mobile number.")

account_page = tk.Tk()
account_page.title("Bunny_bot")
account_page.resizable(False, False)
account_page.geometry("830x545")
account_page.configure(background="pink")
account_page.withdraw()

account_label=tk.Label(account_page, text=" user Account ", font=("Courier", 18, 'bold'), foreground='silver')
account_label.configure(background="white")
account_label.grid(row=1, column=0, padx=40, pady=20)

account_history = tk.Text(account_page, width=65, height=15,font=("Courier", 10,"bold"),relief="solid")
account_history.configure(background="white")
account_history.grid(row=1, column=1,  padx=0, pady=20,sticky="e")

profile_button=tk.Button(account_page,text=" profile ",fg="white", font=("Courier", 12,'bold'), command=show_user_profile)
profile_button.configure(background="black")
profile_button.grid(row=0,column=0,padx=0, pady=0,sticky='nw')

buttons_account_page = [
    ("Voice Assistant History", show_voice_assistant_history),
    ("Text Translate History", show_translate_history),
    ("         Back         ",switch_to_win1),
    ("         Exit         ", account_page.quit)
]

for i, (request2, command) in enumerate(buttons_account_page):
    button6 = tk.Button(account_page, text=request2, fg="black", font=("Courier", 10,'bold'), command=command)
    button6.configure(background="white")
    button6.grid(row=i+2, column=1,padx=0, pady=10,sticky='n')


win2.mainloop()


