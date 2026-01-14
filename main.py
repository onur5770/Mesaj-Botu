import customtkinter as ctk
import tkinter as tk  # Bazı yan özellikler için gerekli
from tkinter import messagebox
import pyautogui
import time
import threading
import keyboard

# --- AYARLAR ---
ctk.set_appearance_mode("Dark")  # Temayı "Karanlık" yap
ctk.set_default_color_theme("blue")  # Ana renk teması (Mavi)

# Global değişkenler
stop_flag = threading.Event()
is_running = False

# --- MANTIK KISMI ---
def send_message_thread(message, delay):
    global is_running
    
    # Geri Sayım
    for i in range(3, 0, -1):
        if stop_flag.is_set(): break
        status_label.configure(text=f"⏳ {i} saniye içinde başlıyor...", text_color="orange")
        time.sleep(1)

    if not stop_flag.is_set():
        status_label.configure(text="🚀 Gönderiliyor...", text_color="#2ecc71") # Açık Yeşil
    
    while not stop_flag.is_set():
        try:
            keyboard.write(message)
            pyautogui.press('enter')
            time.sleep(delay)
        except Exception as e:
            print(f"Hata: {e}")
            break

    is_running = False
    start_button.configure(state="normal", fg_color="#27ae60") # Tekrar yeşil yap
    status_label.configure(text="⛔ Durduruldu / Hazır", text_color="#e74c3c") # Kırmızı

def start_process():
    global is_running
    if is_running: return

    message = message_entry.get()
    delay_str = delay_entry.get()

    if not message:
        tk.messagebox.showwarning("Eksik Bilgi", "Lütfen bir mesaj yazın.")
        return
    
    try:
        delay = float(delay_str)
        if delay < 0.1: raise ValueError
    except ValueError:
        tk.messagebox.showwarning("Hata", "Geçerli bir süre giriniz (Örn: 0.5)")
        return

    stop_flag.clear()
    is_running = True
    
    start_button.configure(state="disabled", fg_color="gray")
    
    t = threading.Thread(target=send_message_thread, args=(message, delay))
    t.daemon = True
    t.start()

def stop_process():
    if is_running:
        stop_flag.set()
        status_label.configure(text="Durduruluyor...", text_color="orange")
    else:
        status_label.configure(text="Zaten çalışmıyor.", text_color="white")

app = ctk.CTk()
app.title("Ultra Mesaj Botu")
app.geometry("400x450")

title_label = ctk.CTkLabel(app, text="OTOMATİK MESAJ BOTU", font=("Roboto", 20, "bold"))
title_label.pack(pady=20)

frame = ctk.CTkFrame(app)
frame.pack(pady=10, padx=20, fill="both", expand=True)


ctk.CTkLabel(frame, text="Gönderilecek Mesaj:", font=("Roboto", 14)).pack(pady=(15, 5), padx=10, anchor="w")
message_entry = ctk.CTkEntry(frame, placeholder_text="Mesajınızı buraya yazın...", width=300, height=35)
message_entry.pack(pady=5, padx=10)


ctk.CTkLabel(frame, text="Gecikme (Saniye):", font=("Roboto", 14)).pack(pady=(10, 5), padx=10, anchor="w")
delay_entry = ctk.CTkEntry(frame, placeholder_text="1.0", width=300, height=35)
delay_entry.insert(0, "1.0")
delay_entry.pack(pady=5, padx=10)


status_label = ctk.CTkLabel(frame, text="Hazır", font=("Roboto", 14, "bold"), text_color="gray")
status_label.pack(pady=15)


btn_frame = ctk.CTkFrame(app, fg_color="transparent") 
btn_frame.pack(pady=10)

start_button = ctk.CTkButton(btn_frame, text="BAŞLAT", command=start_process, 
                             font=("Roboto", 14, "bold"), 
                             fg_color="#27ae60", hover_color="#2ecc71", ı
                             width=140, height=40, corner_radius=20)
start_button.pack(side="left", padx=10)

stop_button = ctk.CTkButton(btn_frame, text="DURDUR", command=stop_process, 
                            font=("Roboto", 14, "bold"), 
                            fg_color="#c0392b", hover_color="#e74c3c", 
                            width=140, height=40, corner_radius=20)
stop_button.pack(side="left", padx=10)

footer = ctk.CTkLabel(app, text="Başlat'a basınca 3 saniye sayar.", font=("Roboto", 10), text_color="gray")
footer.pack(side="bottom", pady=10)

app.mainloop()
