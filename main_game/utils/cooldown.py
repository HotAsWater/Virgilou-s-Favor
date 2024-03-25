import time


class Cooldown:
    def __init__(self, main, cooldown_id):
        self.main = main
        self.end_time = time.time()
        self.id = cooldown_id

    def set_cooldown(self, seconds):
        self.end_time = time.time() + seconds

    def is_on_cooldown(self):
        return self.end_time >= time.time()


class CooldownManager:
    def __init__(self, main):
        self.main = main
        self.cooldowns = {}

    def add_cooldown(self, cooldown_id):
        cooldown = Cooldown(self.main, cooldown_id)
        self.cooldowns[cooldown_id] = cooldown
        return cooldown

    def remove_cooldown(self, cooldown_id):
        del self.cooldowns[cooldown_id]

