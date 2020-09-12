# Argos Translate

Open source offline translation app written in Python. Uses OpenNMT for translations, SentencePiece for tokenization, Stanza for sentence boundary detection, and Tkinter for GUI.

Argos Translate supports installing model files which are a zip archive with an ".argosmodel" extension that contain an OpenNMT CTranslate model, a SentencePiece model, a Stanza tokenizer model, and metadata about the model. Pretrained models can be downloaded [here](https://drive.google.com/drive/folders/11wxM3Ze7NCgOk_tdtRjwet10DmtvFu3i). To install a model click "Install model" from the toolbar in the GUI and select your model file. By default models are stored in ~/.argos-translate, this can be changed in settings.py.

Argos Translate also manages automatically pivoting through intermediate languages to translate between languages that don't have a direct installation between installed for. For example, if you have a es -> en and en -> fr translation installed you are able to translate from es -> fr as if you had that translation installed. This allows for translating between a wide variety of languages at the cost of some loss of translation quality.

## Models
The models are a work in progress and are being trained using [this](https://github.com/argosopentech/onmt-models) training script. 

Currently there are models available to translate between:
- English
- Spanish

## Examples
### GUI
![Screenshot](/img/Screenshot.png)

### Python
```
>>> from argostranslate import package, translate
>>> package.install_from_path('en_es.argosmodel')
>>> installed_languages = translate.load_installed_languages()
>>> [str(lang) for lang in installed_languages]
['English', 'Spanish']
>>> translation_en_es = installed_languages[0].get_translation(installed_languages[1])
>>> translation_en_es.translate("Hello World!")
'¡Hola Mundo!'
```

## Installation
Argos Translate is being developed/tested to run on Linux. However since it is written in Python it should run with minimal modifications on other platforms.

### Python installation
#### Dependencies
Requires Python3 and Tkinter, to install on Ubuntu run:
```
sudo apt-get update
sudo apt-get install -y python3 python3-tk
```
#### Install
1. Clone this repo:
```
git clone https://github.com/argosopentech/argos-translate.git
cd argos-translate
```
2. Make a virtual environment to install it in (optional):
```
virtualenv env
source env/bin/activate
```
3. Install this package with pip:
```
python3 -m pip install --upgrade pip
python3 -m pip install .
```

### Snap installation
1. Install [snapd](https://snapcraft.io/docs/installing-snapd) if it isn't already installed.
2. Using snapd install snapcraft:
```
sudo snap install snapcraft
```
3. Clone this repo:
```
git clone https://github.com/argosopentech/argos-translate.git
cd argos-translate
```
4. From the root directory of this project build the snap package:
```
snapcraft
```
Any unzipped package files in package/ will be automatically included in the snap archive.
5. Install the snap package:
```
sudo snap install --devmode argos-translate_<version information>.snap
```
6. Run Argos Translate!
```
argos-translate
```

Dual licensed under the [MIT License](https://github.com/argosopentech/argos-translate/blob/master/LICENSE) and [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).
