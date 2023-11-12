class Planet:
    alien_count = 0
    name = ""
    
    # Constructor
    def __init__(self, alien_count, name):
        self.alien_count = alien_count
        self.name = name
    
    def print_alien(self):
        print(self.alien_count)
        print(self.name)
        
        
        
    def __str__(self):
        return self.name + str(self.alien_count)

def setup():
    size(500,500, P3D)
    colorMode(HSB)
    global planets, aliens
    
    mars = Planet(10, "Mars")
    mars.print_alien()

    for planet in range(len(planets)):
        print(planet)
        
    for alien in range(len(aliens)):
        print(alien)
        
    for i in range (len(planets)):
        print(planets[i] + "\t" + str(aliens[i]))
        
    for planet in solar_system:
        print(planet)
        
    
    for i in range(len(planets)):
        if aliens[i] < aliens[least_index]:
            least_index=i

        print("The planet with the least number of aliens is : " +str(planets[least_index]))
            
    most_index=0
    for i in range(len(planets)):
        print(i)
        if aliens[i] > aliens[most_index]:
            most_index=i
            print("most_index: " + str(i))

    print("The planet with the most number of aliens is : " +str(planets[most_index]))
    
    sum = 0
    for i in range(len(planets)):
        sum = sum + aliens[i]
    
    average = sum / len(planets)
    
    print("Total Aliens: " + str(sum))
    print("Average Aliens: " + str(average))
    
    
solar_system = [Planet(10, "Mercury"), Planet(10, "Venus"), Planet(9, "Earth"), Planet(19, "Mars")]
    
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
aliens = [50,130,20,100,250,340,200,200,10]

def draw():
    global planets, aliens
    
    background(0)
    w = width / float(len(planets))
    #stroke(255)
    for i in range(len(planets)):
        x = w * i
        fill((i / float(len(planets))) * 255, 255, 255)
    
        rect(x, height, w, - aliens[i])
        textAlign(CENTER, CENTER)
        fill(255)
        text(planets[i], x + (w * 0.5), height - 20)
        
        
