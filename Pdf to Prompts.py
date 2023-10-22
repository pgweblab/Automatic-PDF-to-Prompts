#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nome del file: Automatic PDF to Prompts ChatGPT4
Autore: Piergiorgio Concari
Email: pgweblab@gmail.com
Data di creazione: 22 Ottobre 2023
Versione: 1.0
Descrizione: Automatic PDF to Prompts for ChatGPT4 Automation
"""

from PyPDF2 import PdfReader
import time
import random
import clipboard
import mouse
import keyboard
import winsound # ELIMINARE per LINUX e Merdintosh - Remove for Linux and Mac

# Configurare in base alle coordinate X ed Y relative all'area di immissione del Prompt in ChatGPT4 - Configure based on the X and Y coordinates relative to the ChatGPT4 prompt input area.
x = 1110
y = 1322
# Configurare in base a coordinate in area di riposo. - Configure based on coordinates in the rest area
rel_x = 500
rel_y = 500

def estrai_testo_da_pdf(pdf_path):
    blocchi = []
    
    with open(pdf_path, 'rb') as file:
        lettore_pdf = PdfReader(file)      
        testo_completo = ""     
        for i in range(len(lettore_pdf.pages)):
            pagina = lettore_pdf.pages[i]
            testo_completo += pagina.extract_text()        
        parole = testo_completo.split()     
        i = 0
        while i < len(parole):
            blocco = ' '.join(parole[i:i+500])         
            ultimo_punto = blocco.rfind('.')          
            if ultimo_punto != -1:
                blocco = blocco[:ultimo_punto + 1]           
            i += len(blocco.split())           
            blocchi.append(blocco)   
    numero_blocchi = len(blocchi)
    return blocchi, numero_blocchi

def autopromptgpt(prompts):
    print("Esecuzione del blocco: for prompt in prompts.split('\\n'):")
    for prompt in prompts.split('\n'):
        time.sleep(5)
        print("Esecuzione del blocco: # Attesa di 5 secondi")
        testo = f"{prompt}"
        clipboard.copy(testo)
        time.sleep(0.1)
        mouse.move(x, y, duration=random.uniform(2, 3))
        time.sleep(0.1)
        mouse.click(button='left')
        time.sleep(0.5)
        keyboard.press_and_release('ctrl+v')
        time.sleep(0.5)
        keyboard.press_and_release('enter')
        time.sleep(1)
        mouse.move(rel_x, rel_y, duration=random.uniform(2, 3))
        time.sleep(1)
        time.sleep(25) # Aumentare il tempo in base alla lunghezza del PDF per non superare il limite dei 50 messaggi in 3 ore, attualmente disponibili con ChatGPT4 - Increase the time based on the length of the PDF to not exceed the limit of 50 messages in 3 hours, currently available with ChatGPT4.
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION) # ELIMINARE per LINUX e Merdintosh - Remove for Linux and Mac

# Percorso del file PDF
pdf_path = "./Example.pdf" 
prompts = ""
blocchi_di_testo, numero_blocchi  = estrai_testo_da_pdf(pdf_path)
prompts += f"Nei sucessivi {numero_blocchi} prompt ti fornisco un testo al termine del quale ti varrà chiesto di effettuare alcune analisi ed altre operazioni in relazione ai contenuti forniti nei prompts, in un ottica di semplificazione dei contenuti in ambito scolastico, allo scopo di ottenere rielaborazioni semplificate in Markdown in finestre di tipo Code. Non elaborare risposte o contenuti prima delle istruzioni successive al termine dei {numero_blocchi} prompts successivi.\n"
prompts += '\n'.join(blocchi_di_testo)
prompts += "\n Istruzione successiva N. 1 \n"
prompts += "\n Istruzione successiva N. 2 \n"
prompts += "\n Istruzione successiva N. 3 \n"
autopromptgpt(prompts)
