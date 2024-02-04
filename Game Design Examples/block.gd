extends Sprite2D

func _input(event):
	if event is InputEventMouseButton:	
		# scale = Vector2.ZERO
		var tween = create_tween()
		tween.tween_property(self, "global_position", event.position, 2.0)

func _ready():
	scale = Vector2.ZERO
	var tween = create_tween().set_trans(Tween.TRANS_QUAD)
	tween.tween_property(self, "scale", Vector2.ONE * 500, 2.0)
