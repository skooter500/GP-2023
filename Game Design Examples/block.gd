extends Node2D

func _ready():
	scale = Vector2.ZERO
	var tween = create_tween().set_trans(Tween.TRANS_SINE)
	tween.tween_property(self, "scale", Vector2.ONE, 0.5)
