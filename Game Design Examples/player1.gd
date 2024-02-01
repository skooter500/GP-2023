extends CharacterBody2D

@export var speed:float = 0
@export var rot_speed:float = 360

@export var bullet:PackedScene
@export var bullet_spawn:Node2D

func _ready():
	bullet = load("res://bullet.tscn")
	bullet_spawn = get_node("shoot_point")
	
	pass
	
func _physics_process(delta):
	var f = Input.get_axis("back", "forward")
	
	velocity = speed * -transform.y * f

	var r = Input.get_axis("left", "right")
	rotate(deg_to_rad(rot_speed) * delta * r)
	
	print("right: " + str(transform.x))
	print("up:" + str(transform.y))
	
	if Input.is_action_pressed("fire"):
		var b = bullet.instantiate()
		b.global_position = bullet_spawn.global_position
		b.global_rotation = bullet_spawn.global_rotation
		$"..".add_child(b) 
		
	move_and_slide()
	pass


func _on_timer_timeout():
	print("timer!!")
	pass # Replace with function body.
