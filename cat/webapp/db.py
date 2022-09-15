class DB:
    cat = ''

    @staticmethod
    def get_image(cat):
        if cat.state == 'fury':
            return "images/fury.png"
        elif cat.state == 'happy':
            return "images/happy.png"
        elif cat.state == 'overfed':
            return "images/overfed.png"
        elif cat.state == 'sad':
            return "images/sad.png"
        elif cat.state == 'sleep':
            return "images/sleep.png"
        elif cat.state == 'hungry':
            return "images/hungry.png"
