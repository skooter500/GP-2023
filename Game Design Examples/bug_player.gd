extends CharacterBody2D

@export var speed = 200

@export var bullet_scene:PackedScene

func _physics_process(delta):
	var r = get_viewport_rect()
	
	var f = Input.get_axis("left", "right")
	velocity.x = f * speed
	move_and_slide()

	if position.x > r.size.x - 25:
		position.x = r.size.x - 25
	if position.x < 25:
		position.x = 25
		
