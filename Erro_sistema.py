class ErroSistema(Exception):
    pass

class BilheteNaoEncontradoError(ErroSistema):
    pass

class DadosInvalidosError(ErroSistema):
    pass
