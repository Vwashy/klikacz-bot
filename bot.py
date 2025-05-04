from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Importujemy webdriver_manager
import time

# Używamy webdriver_manager do automatycznego pobrania odpowiedniego chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Zmieniliśmy tutaj

# Opcje Chrome
options = Options()
options.add_argument("--headless")  # Uruchom Chrome w trybie headless
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Przypisz opcje do instancji drivera
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)  # Zmieniliśmy tutaj

# Odwiedź stronę logowania na Disboard
driver.get('https://disboard.org/pl/dashboard/servers?')  # Zmiana tutaj

# Czekaj na załadowanie strony
time.sleep(3)

# Dodaj ciasteczka (wklej ciasteczka, które skopiowałeś)
cookies = [
    {"name": "__cf_bm", "value": "Sqpcfs4SfL252RMjt2xPxJIbTWcHI44PC7Q8uOZlDPc-1746366639-1.0.1.1-kBqf5DwdBINY40fe5KfAv2DSoRXSLPwf.MddR0sltZRfkzSBSW6BRtLnEaGYZOWbyUnJjvIVkym2EQQibScm3CP6rw2jg12x_VcUfgI.c8I"},
    {"name": "_cfuvid", "value": "ZriEsKPfBrvJ2Tw_xTMtK1eKgG.RvXRuc3whqODHbUE-1745934585290-0.0.1.1-604800000"},
    {"name": "_csrf", "value": "49ede7e3fd0179ae5992de22591bd6d3a7bbdb8bb3a032adf7c23d91800681f9a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%222HUG9XoiwhjV5vqxm2fF1A8JOG9ChiuU%22%3B%7D"},
    {"name": "_disboard", "value": "265b5d2ed01869d3b2fb1acacdaac8b6abe8b18b8240b0c3622d8393bf6df523a%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_disboard%22%3Bi%3A1%3Bs%3A68%3A%22%5B%221040351864870408252%22%2C%229Wvcq44wjl0kzUl6khprRJNd1Kfg5Hz2%22%2C315360000%5D%22%3B%7D"},
    {"name": "cf_clearance", "value": "zxiA9ZjijPcQqXBS14_OlqC8iAy74xY4_SN71zFc0.0-1746366639-1.2.1.1-mKTcftbE0HvwuiSqdxCQBT6Lgtv45GNEm0j9218XOFjQ40k0kr6usDK2bztLrj.S2Qr4jMcXKzRDbFOBCeO4t4NPD9Mn9VqcYnWmUIeyl2HCe6bQK6HqTUJ8DubMfWskrCvFGkCyiE2xDSlDoYU6G4WdPxL0oxx2.2spuoFRswhgGV4fjwYGxmavD.qQobuTWYJ_uBb.0VfHMZxZOwgkylmJjSj8PEIoNAW3iKe3QBijlVLNiFfRCoZMVScn5qglGSiHsnVTKSWUv6EsC5U5eFVKdHFPewaf7XzQQrX9FkSschLFyDzCj5lC3k96gb0665rFVtbbphvx31vKP798kfaIjRobtFg_M28Mf49z2z4"},
    {"name": "PHPSESSID", "value": "nkb18rr3iti6kpi8ak4aikkjnf"}
]

# Załaduj ciasteczka do przeglądarki
for cookie in cookies:
    driver.add_cookie(cookie)

# Odśwież stronę, aby ciasteczka zostały załadowane
driver.refresh()

# Czekaj chwilę, aby strona się wczytała
time.sleep(3)

# Zlokalizuj przycisk "Bump" (za pomocą selektora CSS)
button = driver.find_element(By.CSS_SELECTOR, "a.button.button-bump.is-dark")

# Jeśli przycisk jest dostępny (nie jest zablokowany), kliknij go
if button.is_enabled():
    button.click()
    print("Kliknięto przycisk 'Bump'!")

# Poczekaj chwilę, aby upewnić się, że wszystko zostało wykonane
time.sleep(5)

# Zakończ działanie bota
driver.quit()
