extends CharacterBody2D

@export var speed = 200

@export var bullet_scene:PackedScene
@export var explosion_scene:PackedScene

func _physics_process(delta):
	var r = get_viewport_rect()
	
	var f = Input.get_axis("left", "right")
	velocity.x = f * speed
	move_and_slide()

	if position.x > r.size.x - 25:
		position.x = r.size.x - 25
	if position.x < 25:
		position.x = 25
		


func _on_area_2d_area_entered(area):
	var explosion = explosion_scene.instantiate()
	explosion.global_position = global_position
	queue_free()	
	pass # Replace with function body.
