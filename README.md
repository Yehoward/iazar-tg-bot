# İAZAR

Este un bot pentru telegram dezvoltat de echipa İAZARI în cadrul proiectului TekWill.
Funcția botului este de a transcrie mesaje vocale, audiouri, videouri înregistrate în grai Moldovenesc(Bricenesc). 
El îndeplinește aceasta cu ajutorul [versiunii antrenate](https://github.com/Yehoward/whisper-small-ro) a modelului [Whisper](https://openai.com/research/whisper).

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


# Dependențe

## telebot

Librărie pentru programarea boților telegram

https://pypi.org/project/pyTelegramBotAPI/

## transformers 

Librărie de la [HuggingFace](https://huggingface.co/) care oferă utilități pentru a lucra mai ușor cu modele AI.

https://huggingface.co/docs/transformers/index


## pytorch

Librărie folosită pentru învățarea automată a modelelor.

https://pytorch.org


## aiohttp

Pachet necesitat de transformers

https://pypi.org/project/aiohttp/
