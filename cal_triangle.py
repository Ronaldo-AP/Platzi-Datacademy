from modulos.def_triangle import *
from modulos.empty_triangle import Triangle as T

def run():
    
    welcome()

    base, height = init_arguments()
    triangle = T(base, height)
    triangle.T_area()

    continue_question()

    side_a, side_c = init_sides(triangle)
    triangle.T_type(side_a, side_c)

if __name__ == '__main__':
    run()