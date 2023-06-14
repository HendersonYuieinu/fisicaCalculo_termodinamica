import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

R = 8.0

def W():
    P = float(input_Press.get()) * 10 ** 6
    DV = float(input_VolumB.get())*(10**-3) - float(input_VolumA.get())*10**-3

    W = P * DV
    result_W.config(text=f'W = {W:.0f}J')
    return W

def DU():
    N = float(input_Mols.get())
    
    DT = float(input_TempB.get()) - float(input_TempA.get())

    DU = (3 / 2) * N * R * DT
    result_DU.config(text=f'∆U = {DU:.0f}J')
    return DU

def Q(W, DU):
    Q = W + DU
    
    result_Q.config(text=f'Q = {Q:.0f}J')
    return Q

def calculo():
    W()
    DU()
    Q(W(), DU())


Y = [1, 1]
X = [1, 3]

Ax = [1, 1]
Ay = [0, 1]

Bx = [3, 3]
By = [0, 1]

coisax = [0, 1]
coisay = [1, 1]

janela = tk.Tk()
janela.title('Fisicia')

figura = plt.figure(figsize=(10, 5), dpi=60)
grafico = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura, janela)
canva.get_tk_widget().pack()

plt.plot(X, Y)
plt.plot(Ax, Ay, '--', color='orange')
plt.plot(Bx, By, '--',color='orange')
plt.plot(coisax, coisay, '--', color='orange')
plt.annotate('B', xy=(3,1))
plt.annotate('A', xy=(1,1))
plt.xlabel('V (10-³m³)')
plt.ylabel('P (10^6)')
plt.legend()

mainframe = tk.Frame(janela, pady=10, height=50)
mainframe.pack(side='left')

frame = tk.Frame(mainframe, padx=5)
frame.pack(side='left')

frame1 = tk.Frame(mainframe, padx=50)
frame1.pack(side='left')

frame2 = tk.Frame(mainframe, padx=10)
frame2.pack(side='right')

info = tk.Label(frame, text='''T(A) = 300K\nT(B) = 900K\nN = 0.4 mols\nR = 8''', font=('Arial', 15))
info.pack(side='left')

text = tk.Label(frame1, text='Temp(A)')
text.pack()
input_TempA = tk.Entry(frame1, width=5)
input_TempA.pack()

text1 = tk.Label(frame1, text='Temp(B)')
text1.pack()
input_TempB = tk.Entry(frame1, width=5)
input_TempB.pack()

text4 = tk.Label(frame1, text='Nº mols ')
text4.pack()
input_Mols = tk.Entry(frame1, width=5)
input_Mols.pack()

text2 = tk.Label(frame2, text='Volume(A)')
text2.pack()
input_VolumA = tk.Entry(frame2, width=5)
input_VolumA.pack()

text3 = tk.Label(frame2, text='Volume(B)')
text3.pack()
input_VolumB = tk.Entry(frame2, width=5)
input_VolumB.pack()

text5 = tk.Label(frame2, text='Pressao')
text5.pack()
input_Press = tk.Entry(frame2, width=5)
input_Press.pack()

REALIZAR_CALCULO = tk.Button(janela, text='Calcular', command=calculo, width=20, height=2)
REALIZAR_CALCULO.pack()

result_W = tk.Label(janela, text='', font=('Arial', 12))
result_W.pack()
result_DU = tk.Label(janela, text='', font=('Arial', 12))
result_DU.pack()
result_Q = tk.Label(janela, text='', font=('Arial', 12))
result_Q.pack()

janela.mainloop()

