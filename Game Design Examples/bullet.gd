extends CharacterBody2D

@export var speed = 20

func _process(delta):
	velocity = -transform.y * speed
	move_and_slide()
