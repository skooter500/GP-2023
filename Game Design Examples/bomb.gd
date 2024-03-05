extends Area2D

var speed = 300

func  _physics_process(delta):
	position.y += speed * delta


func _on_area_entered(area):
	
	print(area)
	
	pass # Replace with function body.
