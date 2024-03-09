extends Area2D

@export var bomb_spawn:Node2D
@export var bomb_scene:PackedScene
@export var explosion_scene:PackedScene

var target_pos:Vector2

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	global_position = lerp(global_position, target_pos, delta)
	pass


func _on_timer_timeout():
	var offset = randf_range(-100, 100)
	target_pos = position
	target_pos.x += offset
	if target_pos.x < 20:
		target_pos.x = 20
	var w = get_viewport_rect().size.x
	if target_pos.x > w - 20:
		target_pos.x = w - 20 
	target_pos.y += 20
	if randi_range(0, 2) == 0:
		$AudioStreamPlayer2D.play()
	
		drop_bomb()
	
	pass # Replace with function body.


func drop_bomb():
	var bomb = bomb_scene.instantiate()
	bomb.global_position = bomb_spawn.global_position 
	get_tree().root.add_child(bomb)
	pass # Replace with function body.


func _on_area_entered(area):
	if area.name == "laser":
		var explosion = explosion_scene.instantiate()
		explosion.global_position = global_position
		explosion.emitting = true
		get_tree().root.add_child(explosion)
		# self.queue_free()		
pass
