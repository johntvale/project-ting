import re


def exists_word(word, instance):
    result = []
    word_lower = word.lower()
    for file in instance._data:
        lines = []
        for i, line in enumerate(file["linhas_do_arquivo"]):
            line_lower = line.lower()
            if re.search(word_lower, line_lower):
                lines.append(
                    {"linha": i + 1}
                )
        if len(lines) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": lines
                }
            )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
