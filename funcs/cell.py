from funcs.graphics import Point, Line, Window

class Cell:
    def __init__(self, win: Window | None = None):
        self.directions = {"left": True, "right": True, "top": True, "bottom": True}
        self.x1 = -1
        self.y1 = -1
        self.x2 = -1
        self.y2 = -1
        self.win = win
        self.visited = False
        
    def __repr__(self):
        return f"Cell: {Point(self.x1, self.y1)}, {Point(self.x2, self.y2)}"
        
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        top_left = Point(x1, y1)
        top_right = Point(x2, y1)
        bottom_left = Point(x1, y2)
        bottom_right = Point(x2, y2)
        if self.win is None:
            return
        self.win.draw_line(Line(top_left, bottom_left), "black" if self.directions["left"] else "white")
        self.win.draw_line(Line(top_right, bottom_right), "black" if self.directions["right"] else "white")
        self.win.draw_line(Line(top_left, top_right), "black" if self.directions["top"] else "white")
        self.win.draw_line(Line(bottom_left, bottom_right), "black" if self.directions["bottom"] else "white")
    
    def midpoint(self):
        return Point(self.x1, self.y1) + ((Point(self.x1, self.y1) - Point(self.x2, self.y2))/2)
            
    def draw_move(self, to_cell: "Cell", undo=False): 
        if self.win is None:
            return
        colour = "red"
        if undo:
            colour = "grey"
        self.win.draw_line(Line(self.midpoint(), to_cell.midpoint()), colour)
        
       
        