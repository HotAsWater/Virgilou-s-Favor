import box


class BoxSpawner:
    def __init__(self, main):
        self.main = main
        self.boxes = []
        self.play_animation = []

        self.i = 0

    def spawn(self):
        n_box = box.Box(self.main)
        self.boxes.append(n_box)

    def loop(self):
        self.i += 1
        if self.i >= self.main.settings.difficulty * 90 + 20:
            self.i = 0
            self.spawn()

    def getBoxes(self):
        return self.boxes
