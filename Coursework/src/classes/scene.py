class Scene:
    def update(self, delta: float)->None:
        pass
    def draw(self, delta: float)->None:
        pass
    def on_activate(self, data: dict | None)->None:
        pass
    def on_deactivate(self)->dict | None:
        pass