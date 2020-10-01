# Argos Translate
[Docs](https://argos-translate.readthedocs.io) | [Website](https://www.argosopentech.com)

Open source offline translation app written in Python. Uses OpenNMT for translations, SentencePiece for tokenization, Stanza for sentence boundary detection, and PyQt for GUI. Designed to be used either as a GUI application, or as a Python library.

Argos Translate supports installing model files which are a zip archive with an ".argosmodel" extension that contain an OpenNMT CTranslate model, a SentencePiece tokenization model, a Stanza tokenizer model for sentence boundary detection, and metadata about the model. Pretrained models can be downloaded [here](https://drive.google.com/drive/folders/11wxM3Ze7NCgOk_tdtRjwet10DmtvFu3i). To install a model click "Manage packages" from the toolbar in the GUI and select your model file. By default models are stored in ~/.argos-translate, this can be changed in settings.py or by setting the value of the `$ARGOS_TRANSLATE_PACKAGES_DIR` environment variable. When running from a snap package models can be pre-packaged with the snap package or installed after installation to `$SNAP_USER_DATA`.

Argos Translate also manages automatically pivoting through intermediate languages to translate between languages that don't have a direct translation between them installed. For example, if you have a es -> en and en -> fr translation installed you are able to translate from es -> fr as if you had that translation installed. This allows for translating between a wide variety of languages at the cost of some loss of translation quality.

## Models
The models are a work in progress and are being trained using [this](https://github.com/argosopentech/onmt-models) training script. 

Models available for downlad [here](https://drive.google.com/drive/folders/11wxM3Ze7NCgOk_tdtRjwet10DmtvFu3i).

Currently there are models available to translate between:
- English
- Spanish
- French

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
Requires Python3 to install on Ubuntu run:
```
sudo apt-get update
sudo apt-get install -y python3
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
snapcraft clean && SNAPCRAFT_BUILD_ENVIRONMENT_MEMORY=4G snapcraft
```
Any *unzipped* package files in package/ will be automatically included in the snap archive (and won't be able to be deleted by users of the snap).

Note, the build won't run with Snapcraft's default build memory of 2GB so you need to set the SNAPCRAFT_BUILD_ENVIRONMENT environment variable. [More on Snapcraft forum](https://forum.snapcraft.io/t/snapcraft-configuration-of-multipass-vm-arguments/9761)

5. Install the snap package:
```
sudo snap install --devmode argos-translate_<version information>.snap
```
### Run Argos Translate!
```
argos-translate
```

When installing with snap a .desktop file should also be installed which will make Argos Translate available from the desktop menu.

## Contributing
Contributions are welcome! 

## License
Dual licensed under the [MIT License](https://github.com/argosopentech/argos-translate/blob/master/LICENSE) and [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/).

