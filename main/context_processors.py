def global_variables(request):
    """
    The context processor must return a dictionary.
    """
    return {
        "domain_name": "DreamRealty",
        "domain": "https://dreamrealty.onrender.com",
    }
