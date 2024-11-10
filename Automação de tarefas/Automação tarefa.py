#Programa de automacao de acesso ao instagram e acessar Reels
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import getpass
from cryptography.fernet import Fernet
import os

# Variável global para contar tentativas de login
count = 0

# Cria ou lê a chave para criptografia
def load_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    return key

# Funções de criptografia e descriptografia
def encrypt_data(data, key):
    return Fernet(key).encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    return Fernet(key).decrypt(encrypted_data).decode()

# Função para salvar credenciais criptografadas
def save_credentials(username, password):
    key = load_key()
    encrypted_username = encrypt_data(username, key)
    encrypted_password = encrypt_data(password, key)
    with open("credentials.txt", "wb") as cred_file:
        cred_file.write(encrypted_username + b"\n" + encrypted_password)

# Função para carregar credenciais descriptografadas
def load_credentials():
    key = load_key()
    with open("credentials.txt", "rb") as cred_file:
        encrypted_username, encrypted_password = cred_file.read().splitlines()
    username = decrypt_data(encrypted_username, key)
    password = decrypt_data(encrypted_password, key)
    return username, password

# Função para login
def login(driver, username, password):
    global count
    driver.get("https://www.instagram.com/")
    time.sleep(3)
    
    # Preenche campos de login
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    
    # Verifica se o login foi bem-sucedido ou houve erro
    try:
        driver.find_element(By.XPATH, "//p[contains(text(), 'incorrect')]")
        print("Usuário ou senha incorretos. Tente novamente.")
        count += 1
        return False
    except NoSuchElementException:
        print("Login realizado com sucesso!")
        return True

# Inicializa o ChromeOptions e driver
driver = webdriver.Chrome()

# Loop para solicitar credenciais até conseguir fazer login
success = False
while not success:
    try:
        # Solicita credenciais do usuário
        username = input("Digite seu usuário: ")
        password = getpass.getpass("Digite sua senha: ")
        success = login(driver, username, password)

    except Exception as e:
        print(f"Erro durante o login: {e}")
        success = False

# Salva credenciais se o login foi bem-sucedido
if success:
    save_credentials(username, password)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Agora não')]").click()
    except NoSuchElementException:
        pass

# Aguarda a página carregar e localiza o ícone de Reels
try:
    # Clique no ícone dos Reels na barra de navegação
    reels_icon = driver.find_element(By.XPATH, "//a[contains(@href, '/reels/')]")
    reels_icon.click()
    time.sleep(3)
    print("Acessou a seção de Reels com sucesso!")

    # Seleciona o primeiro Reel
    first_reel = driver.find_element(By.XPATH, "//div[contains(@class, 'reel')]")
    first_reel.click()
    print("Clicou no primeiro Reel!")

except Exception as e:
    print("Erro ao acessar o Reel:", e)

# Finaliza o processo
time.sleep(5)
# Fechar driver após o login
driver.quit()