from numpy import isclose

def data_print(title, data):
    out_line = '+' + '-' * 34 + '+'
    out_data = f'| {title}'.ljust(7,' ') + '|' + f' {data} |'.rjust(28, ' ')
    out = '\n' + out_line + '\n' + out_data + '\n' + out_line + '\n'
    return print(out)


def type_triangle(T):
    area = T.area
    s = (T.side_a + T.side_b + T.side_c)*0.5
    h_area = (s * (s - T.side_a) * (s - T.side_b) * (s - T.side_c)) ** (1 / 2)
    if not isclose(area, h_area, atol=0.01):
        print('¿Es el mismo triángulo? Su área no concuerda con la del anterior')
        exit()
    
    if T.side_a == T.height or T.side_c == T.height:
        ttype_angle = 'Rectángulo'
    elif T.side_a < T.base and T.side_c < T.base:
        ttype_angle = 'Acutángulo'
    else:
        ttype_angle = 'Obtusángulo'

    if T.side_a == T.base == T.side_c:
        ttype_sides = 'equilátero'
    elif T.side_a == T.base or T.side_a == T.side_c or T.base == T.side_c:
        ttype_sides = 'isósceles'
    else:
        ttype_sides = 'escaleno'
    
    return ttype_angle + ' ' + ttype_sides


class Triangle:
    
    def __init__(self, base = None, height = None):
        self.base = base
        self.height = height


    def T_area(self):
        self.area = self.base * self.height * 0.5

        data_print('AREA', self.area)
    

    def T_type(self, side_a, side_c):
        
        self.side_a = side_a
        self.side_b = self.base
        self.side_c = side_c

        self.ttype = type_triangle(self)
        data_print('TIPO', self.ttype)

            





