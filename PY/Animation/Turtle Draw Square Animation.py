import turtle
ttl = turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')    
ttl.pencolor('light blue')      
ttl.pensize(6)      
ttl.speed(1.2)     
ttl.shape('turtle')     
ttl.forward(120)
ttl.right(90)
ttl.forward(120)
ttl.right(90)
ttl.forward(120)
ttl.right(90)
ttl.forward(120)
ttl.penup()  
ttl.setpos(-100,90)  
ttl.pendown()  
ttl.pencolor('white')  
ttl.write('Square Animation', font=("Arial", 20, "bold"))  
ttl.penup()  
ttl.ht()