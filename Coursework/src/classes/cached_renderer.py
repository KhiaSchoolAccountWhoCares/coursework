class CachedRenderer(RenderObject, Transformable):
    def __init__(self) -> None:
        super().__init__()
        self.__redraw_triggered = GameEvent(0)
        self.__tinted: bool = False
        self.__tint: Color = Color("white")
        self.__size = Vector2(256, 256)
        self.__render_target: Surface = Surface(self.__size, SRCALPHA)
        self.__rotated_target: Surface = Surface(self.get_container_size(), SRCALPHA)
        self.__tinted_target: Surface | None = None
        self.__last_delta: float = 0
    def get_container_size(self)->Vector2:
        bigger = max(self.__size.x, self.__size.y)
        return Vector2(bigger, bigger)
    #this creates the tint render target in case it is used.
    def prepare_tint(self)->None:
        #if tinted is true then we know the target has already been created and we can exit
        if self.__tinted:
            return
        self.__tinted_target = Surface(self.get_container_size(), SRCALPHA)
    def get_redraw_event(self)->GameEvent:
        return self.__redraw_triggered
    def get_tint(self)->Color:
        return self.__tint
    def set_tint(self, tint: Color)->None:
        if tint == self.__tint:
            #no change happened therefore we exit
            return
        self.__tint = tint
    def draw(self, surface: Surface, offset: Vector2, scale: Vector2, delta: float, tint: Color = Color("white"))-> None:
        self.__last_delta = delta
        super().draw(surface, offset, scale, delta)
        source_surface: Surface = self.__render_target
        #If tinted then we will draw the tinted surface
        if self.__tinted:
            source_surface = self.__tinted_target # type: ignore
        #if our transform is not neutral then we use the transform surface
        elif not self.get_rotation() != 0:
            source_surface = self.__rotated_target
        #and if we're neutral that means we can simply use the render target
        final_rect = source_surface.get_rect().scale_by(self.__scale).scale_by(scale).move(offset)
        if final_rect.colliderect(surface.get_rect()):
            pass
        surface.blit(source_surface, self.get_rect(self.__size).move(self.__position).scale_by(scale))
        pass
    def resize(self, size: Vector2)->None:
        if self.__size == size:
            return
        self.__render_target = Surface(size, SRCALPHA)
        if self.__tinted:
            self.__tinted = False
            self.prepare_tint()
        pass
    def redraw(self)->None:
        self.__redraw_triggered.fire()
        self.__render_target.fill(Color(0, 0, 0, 0))
        self._internal_draw(self.__render_target, self.__last_delta)
        if self.__tinted:
            self.__tinted_target = Surface(self.__size, SRCALPHA)
        pass
    #This is the function in which you're supposed to the drawing.
    def _internal_draw(self, surface: Surface, delta: float)->None:
        pass