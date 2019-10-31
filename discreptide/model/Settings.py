

class Settings:
    MAIN = None

    def __init__(self, root_dir):
        self.observers = []
        self.options = dict()
        self.options['font'] = 'TkDefaultFont'
        self.options['font_size'] = 18
        self.options['css_path'] = ''
        self.options['last_workspace'] = None
        self.root_dir = root_dir

        self.load()
        Settings.MAIN = self

    def add_observer(self, item):
        self.observers.append(item)

    def save(self):
        with open(self.root_dir + '/settings.dat', 'w') as settings:
            for option in self.options:
                settings.write(option)
                settings.write(":")
                settings.write(str(self.options[option]))
                settings.write('\n')

        for observer in self.observers:
            observer.refresh()

    def load(self):
        try:
            with open(self.root_dir + '/settings.dat', 'r') as settings:
                for line in settings.read().splitlines():
                    self.options[line.split(':')[0]] = ":".join(line.split(':')[1:])
        except:
            pass

    def set(self, attr, value):
        self.options[attr] = value

    def get(self, attr):
        if attr in self.options:
            return self.options[attr]
        return None


