class Themes:
    themeIsDark = True 

    @classmethod
    def changeTheme(cls):
        cls.themeIsDark = not cls.themeIsDark
