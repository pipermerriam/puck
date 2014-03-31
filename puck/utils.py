def fancy_import(name):
    """
    This takes a fully qualified object name, like 'accounts.models.ProxyUser'
    and turns it into the accounts.models.ProxyUser object.
    """
    import_path, import_me = name.rsplit('.', 1)
    imported = __import__(import_path, globals(), locals(), [import_me], -1)
    return getattr(imported, import_me)
