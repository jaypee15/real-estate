
def global_variables(request):
    """
      The context processor must return a dictionary.
    """
    return {
        'domain_name': 'Real-Lest',
        'domain': "https://real-lest.onrender.org",
    }