
class Myprint:

    def __init__(self, name):
        self.name = name
        self.mound = []
    # blueprint 接收一组参数 用 add_url_rule 的方法将试图参数注册进blueprint
    # Myprint 也要这么做

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = '/' + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)

