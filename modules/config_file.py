import configparser
import os


def write_config_file(
    path_dir,
    data,
):
    """
    Crée un fichier de configuration pour un projet
    Params:
    - path_dir : chemin du projet sélectionner
    - data : donnée à mettre dans le fichier de configuration
    """
    config = configparser.ConfigParser(allow_no_value=True)
    config_object = {}
    for items in data:
        config_object[items] = None
    config["DEFAULT"] = {"path": path_dir}
    config["SELECTED"] = config_object
    with open(
        os.path.join(path_dir, "config.ini"), "w", encoding="utf-8"
    ) as configfile:
        config.write(configfile)


def read_config_file(path_dir):
    """
    Récupérer les configurations du projet
    Params:
    - path_dir : chemin du projet sélectionner
    """
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(os.path.join(path_dir, "config.ini"))
    all_file = list(config["SELECTED"])
    return all_file
