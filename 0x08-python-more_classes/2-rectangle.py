#!/usr/bin/python3

'''module: 2-rectangle
This is a Rectangle class.
'''


class Rectangle:
    '''class: Rectangle this is an empty class
    '''

    def _init_(self, width=0, height=0):
        '''method: _init_
        initialize instance of Rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: set_width getter
        '''
        if (not isinstance(self._width, int)) or isinstance(self._width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method: set_width setter
        '''
        if not isinstance(self._width, int) or isinstance(self._width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: set_height getter
        '''
        if (not isinstance(self._height, int)) or isinstance(self._height,
                                                              bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        '''method: set_height
        setter
        '''
        if not isinstance(self._height, int) or isinstance(self._height,
                                                            bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """
    Calculate area of Rectangle.
    """
    def area(self):
        return self._height * self._width

    """
    Calculate perimeter of Rectangle object.
    """
    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
