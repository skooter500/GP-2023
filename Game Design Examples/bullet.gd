extends CharacterBody2D

@export var speed = 20

@export var explosion:PackedScene

func _ready():
	var tween = create_tween()
	var modulate_color : Color
	modulate_color.r = 0 # RGB is the color
	modulate_color.g = 255
	modulate_color.b = 255
	modulate_color.a = 0 # A is alpha aka transparency
	tween.tween_property(self, 'modulate', modulate_color, 2)

func _process(delta):
	velocity = -transform.y * speed
	var c =  move_and_collide(velocity * delta)
	if c:
		if c.get_collider().name.contains("block"):
			c.get_collider().queue_free()
			var e = explosion.instantiate()
			get_tree().get_root().add_child(e)
			e.global_position = self.global_position
			e.emitting = true
			self.queue_free()


func _on_timer_timeout():
	self.queue_free()
	pass # Replace with function body.
