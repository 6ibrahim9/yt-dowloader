import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp as ydl


def download_video():
    url = entry.get()
    if not url:
        messagebox.showwarning("Attention", "Veuillez entrer une URL YouTube valide.")
        return
    
    try:
       
        ydl_opts = {
            'format': 'best',  
            'outtmpl': '{}/%(title)s.%(ext)s', 
        }

       
        folder = filedialog.askdirectory(title="Choisir un dossier pour télécharger")
        if not folder:
            messagebox.showinfo("Annulé", "Aucun dossier sélectionné. Téléchargement annulé.")
            return

       
        ydl_opts['outtmpl'] = folder + "/%(title)s.%(ext)s"
        
        
        with ydl.YoutubeDL(ydl_opts) as ydl_instance:
            ydl_instance.download([url])

        messagebox.showinfo("Succès", "Vidéo téléchargée avec succès!")
    
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")


root = tk.Tk()
root.title("YouTube Downloader avec yt-dlp")
root.geometry("500x200")


label = tk.Label(root, text="Entrez l'URL de la vidéo :", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)


button = tk.Button(root, text="Télécharger", command=download_video, bg="blue", fg="white")
button.pack(pady=20)


root.mainloop()
