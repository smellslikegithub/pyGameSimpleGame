class Player:

    def __init__(self, x_position, y_position, width, height):
        print("Constructor Ran")
        self._x_position = x_position
        self._y_position = y_position
        self._width = width
        self._height = height
        self._is_jump = False
        self._jump_count = 10
        self._jump_ceiling = -10

    def print_position(self):
        return [self.x_position, self.y_position]

    def jump(self):
        # if the player is jumping
        if self._is_jump:
            print("here")
            if self._jump_count >= self._jump_ceiling:
                self._y_position -= (self._jump_count * abs(self._jump_count)) * 0.30
                self._jump_count -= 2
            else:
                self._jump_count = 10
                self._is_jump = False

    @property
    def is_jump(self):
        return self._is_jump

    @is_jump.setter
    def set_is_jump(self, flag):
        self._is_jump = flag

    @property
    def x_position(self):
        return self._x_position

    @property
    def jump_count(self):
        return self._jump_count

    @x_position.setter
    def set_x_position(self, x_position):
        self._x_position = x_position

    @property
    def y_position(self):
        return self._y_position

    @y_position.setter
    def set_y_position(self, y_postion):
        self._y_position = y_postion

    @property
    def width(self):
        return self._width

    @width.setter
    def set_width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def set_width(self, height):
        self._height = height
