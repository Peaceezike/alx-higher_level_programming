#!/usr/bin/python3

'''module: 5-rectangle
this module contains the class Rectangle ...
'''


class Rectangle:
    '''class: Rectangle
    this is an empty class, further additions in subsequent assignments
    '''

    def _init_(self, width=0, height=0):
        '''method: _init_
        initialize instance of class Rectangle
        '''
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''method: set_width
        getter
        '''
        if (not isinstance(self._width, int)) or isinstance(self._width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        '''method: set_width
        setter
        '''
        if not isinstance(self._width, int) or isinstance(self._width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        '''method: set_height
        getter
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

    def area(self):
        '''method: area
          return area of rectangle
        '''
        return self._height * self._width

    def perimeter(self):
        '''method: perimeter
        return perimeter of perimeter
        '''
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def _str_(self):
        '''method: _str_
        return: nice string representation of rectangle
        '''
        ret_str = ""
        if self._height == 0 or self._width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += '#' * self.width
            if idx + 1 < self.__height:
                ret_str += '\n'
        return ret_str

    def _repr_(self):
        '''method: _repr_
         return: representation of rectangle that can be used by eval() to
                create new object
        '''
        ret_str = "Rectangle(" + str(self.__width) + ","
        ret_str += str(self.__height) + ")"
        return ret_str

    def _del_(self):
        '''method: _del_
           deletes instance of Rectangle class, and prints "bye" message
        '''
        print("Bye rectangle...")
