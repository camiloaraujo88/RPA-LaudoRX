import pyautogui
import time
import pyscreeze
pyscreeze.USE_OPENCV = True

# ALERTA!!!
pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")
time.sleep(5)

# Caminho para o diretório das imagens
image_path = 'C:/Users/inrad.projetos/Documents/Laudo/Laudo/Imagens/'

def verificar_imagem(nome_imagem, intervalo, timeout):
    try:
        imagem = None
        tempo_inicial = time.time()
        while time.time() - tempo_inicial < timeout:
            imagem = pyautogui.locateCenterOnScreen(image_path + nome_imagem, confidence=0.9)  # Ajuste da confiança
            if imagem:
                return imagem
            time.sleep(intervalo)
        return None
    except pyautogui.ImageNotFoundException:
        print(f"Imagem {nome_imagem} não encontrada na tela.")
        return None

def atualizar():
    atualiza = verificar_imagem('atualiza.png', 5, 60)
    if atualiza:
        pyautogui.click(atualiza)
        time.sleep(2)
        return True
    return False

def passo_1():
    print("Iniciando Passo 1.")
    flag = verificar_imagem('flag.png', 5, 60)
    if flag:
        pyautogui.click(flag, button='right')
        time.sleep(5)
        il = verificar_imagem('il.png', 5, 10)
        if il:
            pyautogui.click(il)
            time.sleep(7)
            passo_2()
        else:
            if atualizar():
                time.sleep(30)
                if not verificar_imagem('flag.png', 5, 60):
                    atualizar()
                    passo_1()
    else:
        if atualizar():
            passo_1()

def passo_2():
    print("[Passo 2] Movendo o mouse para o campo do laudo e clicando...")
    pyautogui.moveTo(1649, 287, duration=2)
    pyautogui.click()
    print("[Passo 2] Digitando texto do laudo...")
    pyautogui.write('Exame realizado para avaliacao pelo medico solicitante. Em caso de duvidas, entrar em contato com a equipe da radiologia.')
    time.sleep(3)
    passo_3()

def passo_3():
    print("Passo 3 iniciado.")
    time.sleep(3)
    validar_icon = pyautogui.locateCenterOnScreen(image_path + 'validar.png', confidence=0.9)
    if validar_icon:
        print("[Passo 3] Ícone Validar encontrado. Clicando...")
        pyautogui.click(validar_icon)
        time.sleep(5)
        passo_4()

def passo_4():
    print("Passo 4 iniciado.")
    time.sleep(5)

    # Loop 1: Aguarda o 'atualiza.png' e clica quando encontrado
    print("[Passo 4] Aguardando 'atualiza.png'...")
    atualiza = verificar_imagem('atualiza.png', 5, 60)
    
    if atualiza:
        pyautogui.click(atualiza)
        print("[Passo 4] 'atualiza.png' encontrado e clicado.")
        time.sleep(5)
    else:
        print("[Passo 4] 'atualiza.png' não encontrado. Verificando novamente...")

    # Verifica novamente a cada 5 segundos até 60 segundos
    tempo_inicial = time.time()
    while time.time() - tempo_inicial < 60:
        atualiza_nova = verificar_imagem('atualiza.png', 5, 60)
        if atualiza_nova:
            pyautogui.click(atualiza_nova)
            print("[Passo 4] 'atualiza.png' encontrado novamente e clicado.")
            time.sleep(5)  # Espera 5 segundos após clicar
            break
        else:
            print("[Passo 4] 'atualiza.png' não encontrado, verificando novamente...")

    passo_5()  # Chama o passo 5 para continuar

def passo_5():
    print("[Passo 5] Aguardando o 'atualiza.png' aparecer novamente para reiniciar o Passo 1...")
    
    # Verifica novamente a cada 5 segundos até 60 segundos
    tempo_inicial = time.time()
    while time.time() - tempo_inicial < 60:
        atualiza_nova = verificar_imagem('atualiza.png', 5, 60)
        if atualiza_nova:
            pyautogui.click(atualiza_nova)
            print("[Passo 5] 'atualiza.png' encontrado novamente e clicado.")
            time.sleep(5)  # Espera 5 segundos após clicar
            break
        else:
            print("[Passo 5] 'atualiza.png' não encontrado, verificando novamente...")

    passo_6()  # Chama o passo 6

def passo_6():
    print("Passo 6 iniciado.")
    time.sleep(5)

    print("[Passo 6] Aguardando 'atualiza.png' aparecer...")
    
    # Verifica novamente a cada 5 segundos até 60 segundos
    tempo_inicial = time.time()
    while time.time() - tempo_inicial < 60:
        atualiza = verificar_imagem('atualiza.png', 5, 60)
        if atualiza:
            print("[Passo 6] 'atualiza.png' encontrado.")
            time.sleep(5)  # Espera 5 segundos após clicar
            break
        else:
            print("[Passo 6] 'atualiza.png' não encontrado, verificando novamente...")

    passo_1()  # Chama o passo 1 para continuar

# Iniciar o processo
passo_1()