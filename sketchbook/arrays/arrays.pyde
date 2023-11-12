def setup():
    size(500,500)
    global planets, aliens
    
    
    for planet in range(len(planets)):
        print(planet)
        
    for alien in range(len(aliens)):
        print(alien)
        
    for i in range (len(planets)):
        print(planets[i] + "\t" + str(aliens[i]))
        
    least_index=0
    for i in range(len(planets)):
        if aliens[i] < aliens[least_index]:
            least_index=i

    print("The planet with the least number of aliens is : " +str(planets[least_index]))

    
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]
aliens = [5,13,2,10,25,34,20,20,1]

def draw():
    pass
