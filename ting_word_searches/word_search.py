import re


def get_object(need_content, i, line):
    if need_content:
        return {
            "linha": i + 1,
            "conteudo": line}
    else:
        return {"linha": i + 1}


def get_match_data(word, instance, need_content):
    result = []
    word_lower = word.lower()
    for file in instance._data:
        lines = []
        for i, line in enumerate(file["linhas_do_arquivo"]):
            line_lower = line.lower()
            if re.search(word_lower, line_lower):
                content = get_object(need_content, i, line)
                lines.append(content)
        if len(lines) > 0:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": lines
                }
            )
    return result


def exists_word(word, instance):
    result = get_match_data(word, instance, need_content=False)
    return result


def search_by_word(word, instance):
    result = result = get_match_data(word, instance, need_content=True)
    return result
