class Library:
    dict = {}

    def add_tape(self, Tape):
        title = Tape.title
        self.dict[title] = Tape
        print(self.dict)

    def find_tape(self, title):
        if title in self.dict.keys():
            return self.dict[title]
        return None

    def delete_tape(self, title):
        if title in self.dict.keys():
            removed_tape = self.dict.pop(title)
            return removed_tape
        return None
