import os
import textwrap
from PIL import Image


def is_valid_image(dossier_source, file_name):
    try:
        file_path = os.path.join(dossier_source, file_name)
        Image.open(file_path).verify()
        return True
    except (IOError, SyntaxError):
        return False


def truncate_text(text, max_lines=2):
    """
    Permet de fractionner un texte en plusieurs ligne et de recupérer un certain nombre de ligne.
    Params:
    - text : Chaine de caractères. (string)
    - max_lines: Nombre de ligne. (int)
    """
    wrapper = textwrap.TextWrapper(width=12)
    wrapped_text = wrapper.wrap(text)
    truncated_text = "\n".join(wrapped_text[:max_lines])
    return truncated_text
