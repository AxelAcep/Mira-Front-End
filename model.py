class AppState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppState, cls).__new__(cls)
            cls._instance.token = None
            cls._instance.nidn = None
            cls._instance.nama = None
            cls._instance.profil = None
        return cls._instance

    def set_auth(self, token, nidn, nama, profil):
        self.token = token
        self.nidn = nidn
        self.nama = nama
        self.profil = profil

    def clear(self):
        self.token = None
        self.nidn = None
        self.nama = None
        self.profil = None