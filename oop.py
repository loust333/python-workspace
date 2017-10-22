class Music:
    def notes(self, note):
        self.data = note

    def display(self):
        print self.data

x = Music()
y = Music()

x.notes("0 my what a day")
y.notes('Rock n roll is still king')

x.display()
y.display()

class Musician(Music):
    def display(self):
        print 'The notes are = "%s"' % self.data

mashrur = Musician()
mashrur.notes("I don't know how to sing")

mashrur.display()
