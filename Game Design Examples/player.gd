extends Node2D

func _input(event):
	if event is InputEventKey and event.key == KEY_Q:
		get_tree().quit()

func _ready():
	pass
	
func _process(delta):
	
	pass
