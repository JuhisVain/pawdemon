import vertex


class Abstract_sector:
    def __init__(self, v0, v1, v2):
        
        # Initially only hold minimum amount to form triangle
        self.vertices = [v0, v1, v2]
        # Can't find object field accessor overloading anywhere...
        self.__ffs__inverted_sector = False  # If set to true with invert(), asector is inverted
        
        side_num = (v1.x - v0.x)*(v2.y - v0.y) - (v2.x - v0.x)*(v1.y - v0.y)
        if side_num > 0:  # v2 on left of line0/1
            self.vertices.reverse()
        elif side_num == 0:  # v2 in line with line0/1
            print("WARNING : Formed line instead of triangle.")

    def add_vertex(self, vertexn, between1, between2):
        # Add a new vertex between vertices between1 & between2
        # Return True if success
        if vertexn == between1 or vertexn == between2 or between1 == between2:
            print("ERROR : goofy arguments for add_vertex.")
            return False  # throwing exceptions is for scrubs

        b1_index = -1
        b2_index = -1

        for i in range(len(self.vertices)):
            if vertexn == self.vertices[i]:  # vertex == has been overloaded
                print("WARNING : add_vertex: vertex already in abstract sector.")
                return False
            elif between1 == self.vertices[i]:
                if b1_index >= 0:
                    print("ERROR : duplicate vertices in abstract sector.")
                    return False
                b1_index = i
            elif between2 == self.vertices[i]:
                if b2_index >= 0:
                    print("ERROR : duplicate vertices in abstract sector.")
                    return False
                b2_index = i

        if b1_index >= 0 and b2_index >= 0:
            if b1_index+1 == b2_index:
                self.vertices.insert(b2_index, vertexn)
            elif b1_index == len(self.vertices-1) and b2_index == 0:
                self.vertices.append(vertexn)
            else:
                print("ERROR : There is no such line in abstract sector.")
                return False

        return True

    def invert(self):
        if not self.__ffs__inverted_sector:
            self.__ffs__inverted_sector = True
        else:
            self.__ffs__inverted_sector = False
        self.vertices.reverse()
