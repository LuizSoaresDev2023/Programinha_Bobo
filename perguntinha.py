import tkinter as tk
from tkinter import messagebox
import pygame
import random

def click_sim():
    messagebox.showinfo("Resposta", f"Mas que dificuldade, hein... acho que é porque você na verdade é VASCÃO! kkkk, {nome}!")

def click_nao():
    messagebox.showinfo("Resposta", "Eu já sabia que vc era VASCÃO! kkkk")

def mover_botao_sim(event):
    global sim_pos
    sim_pos = (random.randint(50, 250), random.randint(50, 100))
    button_sim.place(x=sim_pos[0], y=sim_pos[1])

def exibir_pergunta():
    global nome
    nome = entry_nome.get()
    pergunta = f"{nome}, qual seu time de coração?"
    label_pergunta.config(text=pergunta)
    button_sim.config(state=tk.NORMAL)
    button_nao.config(state=tk.NORMAL)

janela = tk.Tk()
janela.title("Programinha")
janela.geometry("300x150")

label_nome = tk.Label(janela, text="Digite seu nome:")
label_nome.pack()

entry_nome = tk.Entry(janela)
entry_nome.pack()

button_iniciar = tk.Button(janela, text="Iniciar", command=exibir_pergunta)
button_iniciar.pack()

label_pergunta = tk.Label(janela, text="")
label_pergunta.pack()

button_sim = tk.Button(janela, text="Fla", state=tk.DISABLED, command=click_sim)
button_sim.pack(side=tk.LEFT, padx=10)

button_nao = tk.Button(janela, text="Vas", state=tk.DISABLED, command=click_nao)
button_nao.pack(side=tk.LEFT, padx=10)

sim_pos = (50, 25)
button_sim.place(x=sim_pos[0], y=sim_pos[1])

pygame.init()
pygame.display.set_mode((1, 1))
pygame.mouse.set_visible(True)

button_sim.bind("<Enter>", mover_botao_sim)

janela.mainloop()
