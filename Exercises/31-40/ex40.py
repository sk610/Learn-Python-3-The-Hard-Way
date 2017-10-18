'''

mystuff = {'apple': "I AM APPLES"} - mystuff is a dictionary, and 'apple' is a key, and the last string is a key value of that dictionary. 
print(mystuff['apple'])

'''

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(['Happy Birthday to you', 'I don\'t want to get sued', 'So i\'ll stop right there'])

bulls_on_parade = Song(['They rally around the family', 'With pockets full of shells'])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()