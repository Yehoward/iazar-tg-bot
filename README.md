# İAZAR

Este un bot pentru telegram dezvoltat de echipa İAZARI în cadrul proiectului TekWill.
Funcția botului este de a transcrie mesaje vocale, audiouri, videouri înregistrate în grai Bricenesc. 
El îndeplinește aceasta cu ajutorul modelului [Whisper](https://openai.com/research/whisper).

# Instalare

Clonați:

```sh
git clone https://github.com/Yehoward/iazar-tg-bot.git
```
Instalați (în mediu virtual):

```sh
pipenv install
```

Veți avea nevoie de un [telegram jeton(token)](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).
Care-l plasați în fișierul `.env`

```sh
KEY="Cheia-voastră"
```
Derulați (în mediu virtual):

```sh
pipenv run python main.py
```

