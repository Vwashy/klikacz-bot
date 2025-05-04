FROM python:3.11-slim

# Instalacja zależności systemowych i Google Chrome
RUN apt-get update && apt-get install -y \
    wget gnupg2 curl unzip \
    fonts-liberation libappindicator3-1 libasound2 \
    libatk-bridge2.0-0 libatk1.0-0 libcups2 \
    libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 \
    libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    xdg-utils libgbm1 libgtk-3-0

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -f -y

# Ustawienie katalogu roboczego
WORKDIR /app
COPY . .

# Instalacja zależności Pythona
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Domyślne polecenie
CMD ["python", "bot.py"]
