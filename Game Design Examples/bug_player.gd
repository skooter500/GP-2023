extends CharacterBody2D

@export var speed = 200

@export var bullet_scene:PackedScene
@export var explosion_scene:PackedScene

@onready var laser:Node2D=$laser

@onready var bug:Node2D=$"../bug"

func _ready():
	laser.visible = false

func _process(delta):
	if Input.is_action_pressed("fire"):
		laser.visible = true
		var to_bug = laser.global_position.y - bug.global_position.y 
		var p = laser.get_point_position(0)
		p.y = - to_bug
		laser.set_point_position(1, p)
	else:
		laser.visible = false
	
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
	explosion.emitting = true
	get_tree().root.add_child(explosion)
	queue_free()	
	pass # Replace with function body.
