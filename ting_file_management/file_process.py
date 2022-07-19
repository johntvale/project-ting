from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_already_exist = False
    item_to_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }
    for item in instance._data:
        if item["nome_do_arquivo"] == path_file:
            file_already_exist = True
            break
    if not file_already_exist:
        instance.enqueue(item_to_process)
    print(item_to_process)
    


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
