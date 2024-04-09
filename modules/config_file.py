import configparser
import os


def write_config_file(path_dir, data, category, default=False):
    """
    Crée un fichier de configuration pour un projet
    Params:
    - path_dir : chemin du projet sélectionner
    - data : donnée à mettre dans le fichier de configuration
    """
    config = configparser.ConfigParser(allow_no_value=True)
    config_object = {}
    if default == True:
        config[category] = data
    else:
        for items in sorted(data):
            if items.endswith(".tif"):
                config_object[items] = None
        config[category] = config_object

    with open(
        os.path.join(path_dir, "config.ini"), "a", encoding="utf-8"
    ) as configfile:
        config.write(configfile)


def read_config_file(path_dir, category):
    """
    Récupérer les configurations du projet
    Params:
    - path_dir : chemin du projet sélectionner
    """
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(os.path.join(path_dir, "config.ini"))
    all_file = list(config[category])
    return all_file
