def strip_url_params(url, params_to_strip = []):
    if '?' not in url:
        return url
    u, r = url.split('?')
    args = {}
    for t in r.split('&'):
        k, v = t.split('=')
        if k not in args and k not in params_to_strip:
            args[k] = v
    suffix = map(lambda y: '&'.join(y), [map(lambda x: '='.join(x), args.items())])
    return '{}?{}'.format(u, ''.join(suffix))
