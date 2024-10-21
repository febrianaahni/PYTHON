import PySimpleGUI as sg
sg.theme("DarkTeal")
sg.theme_text_color("#E3CF57")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010367 ")],
[sg.Text("Nama : Febriana Ahni Herlima Nita ")],
[sg.Text("Kelas : 5A Non-Reguler Banjarmasin ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()