<<<<<<< HEAD
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk # Import ttk for themed widgets
from threading import Thread
import queue

# --- Core Gemini Backend Logic ---
from google import genai
from google.genai.errors import APIError

class GeminiChatbot:
    """Manages the conversation and API calls with Gemini."""
    
    def __init__(self, system_instruction="You are a helpful, concise, and friendly chatbot."):
        
        # 🚨 WARNING: KEY IS HARDCODED TO FIX ENVIRONMENT ISSUE 🚨
        api_key = "AIzaSyANtbILttWX8T-MMU7ZPKVVhlwf7-t5IoI" 
        # --------------------------------------------------------

        if not api_key or "AIzaSy" not in api_key:
            raise ValueError("API Key is missing or invalid in the code.")

        try:
            self.client = genai.Client(api_key=api_key) 
            self.chat = self.client.chats.create(
                model="gemini-2.5-flash",
                config={"system_instruction": system_instruction}
            )

        except Exception as e:
            raise Exception(f"Failed to initialize Gemini Client: {e}")

    def send_message(self, prompt: str) -> str:
        """Sends a message to the Gemini API and returns the response text."""
        try:
            response = self.chat.send_message(prompt)
            return response.text
        except APIError as e:
            return f"Error: Failed to get response from Gemini API: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

# --- Enhanced Tkinter GUI Frontend Logic ---

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Gemini Chat Assistant")
        master.geometry("600x550") # Set a slightly larger window size
        master.resizable(True, True)

        # Apply a theme (Windows/Mac users will see a native theme)
        style = ttk.Style()
        style.theme_use('clam') # 'clam' or 'alt' often look better than default

        try:
            self.chatbot = GeminiChatbot()
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Fatal Setup Error: {e}")
            master.destroy() 
            return
            
        self.response_queue = queue.Queue() 
        
        # 1. Main Frame (to hold all widgets and provide padding)
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 2. Conversation Display Area (Now uses a more professional font)
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, 
            state='disabled', 
            wrap=tk.WORD, 
            font=('Segoe UI', 10), # Better font choice
            padx=5, 
            pady=5
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # 3. Input Frame (uses ttk.Frame)
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X)
        
        # 4. User Input Field (ttk.Entry)
        self.user_input = ttk.Entry(input_frame, font=('Segoe UI', 11))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5) # Added ipady for height
        self.user_input.focus_set() 
        self.user_input.bind("<Return>", lambda event=None: self.start_message_thread())

        # 5. Send Button (ttk.Button)
        self.send_button = ttk.Button(
            input_frame, 
            text="Send", 
            command=self.start_message_thread, 
            style='Send.TButton' # Custom style for emphasis
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 0))

        # Define custom button style for the Send button
        style.configure('Send.TButton', font=('Segoe UI', 10, 'bold'))

        # Initial message and queue check
        self.display_message("Bot", "Initialization successful! How can I help you today?", color='#006400')
        self.master.after(100, self.check_queue) 

    def display_message(self, sender: str, message: str, color: str = 'black'):
        """Appends a message to the chat display with better line breaks."""
        self.chat_display.config(state='normal')
        
        tag_name = sender.lower()
        if tag_name not in self.chat_display.tag_names():
             self.chat_display.tag_config(tag_name, foreground=color, font=('Segoe UI', 10, 'bold'))
        
        # Use simple text insertion for cleaner output formatting
        self.chat_display.insert(tk.END, f"{sender}: ", tag_name)
        self.chat_display.insert(tk.END, f"{message}\n\n") # Double newline for spacing
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END) 

    def start_message_thread(self):
        """Prepares the GUI and starts a new thread for the API call."""
        prompt = self.user_input.get().strip()
        if not prompt:
            return
            
        self.display_message("You", prompt, color='#000080') # Dark blue for user
        self.user_input.delete(0, tk.END)
        self.send_button.config(state='disabled') 
        
        t = Thread(target=self.get_gemini_response, args=(prompt,))
        t.start()

    def get_gemini_response(self, prompt: str):
        """Worker function (runs in a separate thread) to call the API."""
        response_text = self.chatbot.send_message(prompt)
        self.response_queue.put(response_text) 
        
    def check_queue(self):
        """Checks the queue for responses from the worker thread."""
        try:
            response = self.response_queue.get(block=False)
            
            self.display_message("Bot", response, color='#006400') # Dark green for bot
            
            self.send_button.config(state='normal')
            self.user_input.focus_set()

        except queue.Empty:
            pass 
        
        self.master.after(100, self.check_queue)

# --- Application Entry Point ---
if __name__ == '__main__':
    root = tk.Tk()
    app = ChatApp(root)
=======
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk # Import ttk for themed widgets
from threading import Thread
import queue

# --- Core Gemini Backend Logic ---
from google import genai
from google.genai.errors import APIError

class GeminiChatbot:
    """Manages the conversation and API calls with Gemini."""
    
    def __init__(self, system_instruction="You are a helpful, concise, and friendly chatbot."):
        
        # 🚨 WARNING: KEY IS HARDCODED TO FIX ENVIRONMENT ISSUE 🚨
        api_key = "AIzaSyANtbILttWX8T-MMU7ZPKVVhlwf7-t5IoI" 
        # --------------------------------------------------------

        if not api_key or "AIzaSy" not in api_key:
            raise ValueError("API Key is missing or invalid in the code.")

        try:
            self.client = genai.Client(api_key=api_key) 
            self.chat = self.client.chats.create(
                model="gemini-2.5-flash",
                config={"system_instruction": system_instruction}
            )

        except Exception as e:
            raise Exception(f"Failed to initialize Gemini Client: {e}")

    def send_message(self, prompt: str) -> str:
        """Sends a message to the Gemini API and returns the response text."""
        try:
            response = self.chat.send_message(prompt)
            return response.text
        except APIError as e:
            return f"Error: Failed to get response from Gemini API: {e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

# --- Enhanced Tkinter GUI Frontend Logic ---

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Gemini Chat Assistant")
        master.geometry("600x550") # Set a slightly larger window size
        master.resizable(True, True)

        # Apply a theme (Windows/Mac users will see a native theme)
        style = ttk.Style()
        style.theme_use('clam') # 'clam' or 'alt' often look better than default

        try:
            self.chatbot = GeminiChatbot()
        except Exception as e:
            messagebox.showerror("Initialization Error", f"Fatal Setup Error: {e}")
            master.destroy() 
            return
            
        self.response_queue = queue.Queue() 
        
        # 1. Main Frame (to hold all widgets and provide padding)
        main_frame = ttk.Frame(master, padding="10 10 10 10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 2. Conversation Display Area (Now uses a more professional font)
        self.chat_display = scrolledtext.ScrolledText(
            main_frame, 
            state='disabled', 
            wrap=tk.WORD, 
            font=('Segoe UI', 10), # Better font choice
            padx=5, 
            pady=5
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        # 3. Input Frame (uses ttk.Frame)
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X)
        
        # 4. User Input Field (ttk.Entry)
        self.user_input = ttk.Entry(input_frame, font=('Segoe UI', 11))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5) # Added ipady for height
        self.user_input.focus_set() 
        self.user_input.bind("<Return>", lambda event=None: self.start_message_thread())

        # 5. Send Button (ttk.Button)
        self.send_button = ttk.Button(
            input_frame, 
            text="Send", 
            command=self.start_message_thread, 
            style='Send.TButton' # Custom style for emphasis
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 0))

        # Define custom button style for the Send button
        style.configure('Send.TButton', font=('Segoe UI', 10, 'bold'))

        # Initial message and queue check
        self.display_message("Bot", "Initialization successful! How can I help you today?", color='#006400')
        self.master.after(100, self.check_queue) 

    def display_message(self, sender: str, message: str, color: str = 'black'):
        """Appends a message to the chat display with better line breaks."""
        self.chat_display.config(state='normal')
        
        tag_name = sender.lower()
        if tag_name not in self.chat_display.tag_names():
             self.chat_display.tag_config(tag_name, foreground=color, font=('Segoe UI', 10, 'bold'))
        
        # Use simple text insertion for cleaner output formatting
        self.chat_display.insert(tk.END, f"{sender}: ", tag_name)
        self.chat_display.insert(tk.END, f"{message}\n\n") # Double newline for spacing
        
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END) 

    def start_message_thread(self):
        """Prepares the GUI and starts a new thread for the API call."""
        prompt = self.user_input.get().strip()
        if not prompt:
            return
            
        self.display_message("You", prompt, color='#000080') # Dark blue for user
        self.user_input.delete(0, tk.END)
        self.send_button.config(state='disabled') 
        
        t = Thread(target=self.get_gemini_response, args=(prompt,))
        t.start()

    def get_gemini_response(self, prompt: str):
        """Worker function (runs in a separate thread) to call the API."""
        response_text = self.chatbot.send_message(prompt)
        self.response_queue.put(response_text) 
        
    def check_queue(self):
        """Checks the queue for responses from the worker thread."""
        try:
            response = self.response_queue.get(block=False)
            
            self.display_message("Bot", response, color='#006400') # Dark green for bot
            
            self.send_button.config(state='normal')
            self.user_input.focus_set()

        except queue.Empty:
            pass 
        
        self.master.after(100, self.check_queue)

# --- Application Entry Point ---
if __name__ == '__main__':
    root = tk.Tk()
    app = ChatApp(root)
>>>>>>> fe5b7b4d1ab83a894567fdd8d720be1b422f5b96
    root.mainloop()