extends Node2D


func _input(event):
	if event is InputEventKey:
		var key_event = event as InputEventKey
		if key_event.keycode == KEY_Q and key_event.pressed:
			get_tree().quit()
