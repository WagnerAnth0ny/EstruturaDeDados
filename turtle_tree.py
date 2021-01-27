import turtle as t

def construct_tree(arvore, l):
    if(arvore != None):
        t.forward(l)
        t.color("light green")
        t.circle(5)
        t.color("purple")
        t.left(30)
        construct_tree(arvore.left, 3*l/4)
        t.right(60)
        construct_tree(arvore.right, 3 * l / 4)
        t.left(30)
        t.backward(l)

def define_t(arvore, l):
    t.Turtle._screen = None  # force recreation of singleton Screen object
    t.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition
    wn = t.Screen()
    t.speed(100000)
    t.pensize(2)
    t.left(90)
    t.bgcolor("black")
    t.backward(160)
    t.color("purple")
    construct_tree(arvore, l)
    
