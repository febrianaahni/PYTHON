import PySimpleGUI as sg
window = sg.Window(title="Profile",
layout=[[sg.Text("NPM : 2210010367 ")],
[sg.Text("Nama : Febriana Ahni H.N ")],
[sg.Text("Kelas : 5A Non-Regular Banjarmasin ")],
[sg.Text("Matkul : Pemrograman Visual 3  ")]
],
size=(400,200),)
window()
window.close()