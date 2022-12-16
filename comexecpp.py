import os
import shutil
import subprocess

from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Cria a aplicação
app = QApplication([])

# Cria a janela principal
window = QWidget()
window.setWindowTitle("Compile and Run C++ program")

# Cria o campo de entrada de texto para o nome do programa
program_name_field = QLineEdit()
program_name_field.setPlaceholderText("Enter program name")

# Cria o botão para selecionar o arquivo
select_file_button = QPushButton("Select file")
select_file_button.clicked.connect(
    lambda: program_name_field.setText(
        QFileDialog.getOpenFileName(filter="*.cpp")[0]
    )
)

# Cria o botão para compilar e executar o programa
compile_and_run_button = QPushButton("Compile and run")
compile_and_run_button.clicked.connect(compile_and_run)

# Cria o layout vertical para os widgets
layout = QVBoxLayout()
layout.addWidget(program_name_field)
layout.addWidget(select_file_button)
layout.addWidget(compile_and_run_button)
window.setLayout(layout)

# Mostra a janela
window.show()

# Executa a aplicação
app.exec_()

def compile_and_run():
    # Obtém o nome do programa digitado pelo usuário
    program_name = program_name_field.text()

    # Verifica se o usuário digitou o nome do programa
    if not program_name:
        QMessageBox.warning(None, "Error", "No program name provided")
        return

    # Verifica se o arquivo existe
    if not os.path.exists(program_name):
        QMessageBox.warning(None, "Error", "File does not exist")
        return

    # Exclui o arquivo caso exista
    if os.path.exists(program_name):
        os.remove(program_name)

    # Compila o programa
    result = subprocess.run(["g++", program_name + ".cpp", "-o", program_name])

    # Verifica se ocorreu um erro ao compilar o programa
    if result.returncode != 0:
        QMessageBox.warning(None, "Error", "Error compiling program")
        return

    # Executa o programa
    subprocess.run(["./" + program_name])