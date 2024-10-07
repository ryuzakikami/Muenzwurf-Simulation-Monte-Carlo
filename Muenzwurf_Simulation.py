import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
import numpy as np

class Muenzwurf:
    def __init__(self):
        self.kopf = 1
        self.zahl = 0
        self.anzahl_kopf = 0
        self.anzahl_zahl = 0

    def werfen(self, anzahl):
      
        ergebnisse = np.random.choice([self.kopf, self.zahl], size=anzahl)
        self.anzahl_kopf += np.sum(ergebnisse == self.kopf)
        self.anzahl_zahl += np.sum(ergebnisse == self.zahl)

def update_progress(progress_bar, ergebnis_label, i, gesamt_wuerfe):
    progress_bar['value'] = (i / gesamt_wuerfe) * 100
    if i % 100 == 0:  
        ergebnis_label.config(text=f"Berechnet: {i}/{gesamt_wuerfe} Würfe")

def run_simulation(gesamt_wuerfe, progress_bar, ergebnis_label, ladefenster):
    wurf = Muenzwurf()
    
    anteil_kopf = []
    anteil_zahl = []
    
    
    schritte = 1  
    x_wuerfe = []

    for i in range(0, gesamt_wuerfe, schritte):
        anzahl = min(schritte, gesamt_wuerfe - i)
        wurf.werfen(anzahl)
        
       
        anteil_kopf.append(wurf.anzahl_kopf / (i + anzahl))
        anteil_zahl.append(wurf.anzahl_zahl / (i + anzahl))
        x_wuerfe.append(i + anzahl)  
        
        update_progress(progress_bar, ergebnis_label, i + anzahl, gesamt_wuerfe)


    ladefenster.destroy()

 
    plt.figure(figsize=(14, 8))


    plt.subplot(2, 1, 1)
    plt.bar(['Kopf', 'Zahl'], [wurf.anzahl_kopf, wurf.anzahl_zahl], color=['blue', 'orange'], alpha=0.7)
    plt.ylabel("Anzahl der Würfe")
    plt.title("Streuung der Münzwürfe")
    plt.grid(axis='y', linestyle='--')

   
    plt.subplot(2, 1, 2)
    plt.plot(x_wuerfe, anteil_kopf, label='Anteil Kopf', color='blue')
    plt.plot(x_wuerfe, anteil_zahl, label='Anteil Zahl', color='orange')
    plt.axhline(0.5, color='gray', linestyle='--')
    plt.xlabel("Anzahl der Würfe")
    plt.ylabel("Anteil")
    plt.title("Grenzverhalten der Anteile")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

def start_simulation(gesamt_wuerfe):
    global ladefenster
    ladefenster = tk.Toplevel(root)
    ladefenster.title("Ladebalken")

    progress_bar = ttk.Progressbar(ladefenster, orient='horizontal', length=300, mode='determinate')
    progress_bar.pack(pady=20)

    ergebnis_label = tk.Label(ladefenster, text="", font=("Arial", 12))
    ergebnis_label.pack(pady=10)

    run_simulation(gesamt_wuerfe, progress_bar, ergebnis_label, ladefenster)

def eingabe_zahl():
    global root
    root = tk.Tk()
    root.withdraw()
    gesamt_wuerfe = simpledialog.askinteger("Eingabe", "Geben Sie die Anzahl der Wiederholungen ein (z.B. 1000, 10000):")
    if gesamt_wuerfe is not None:
        start_simulation(gesamt_wuerfe)

if __name__ == "__main__":
    eingabe_zahl()
