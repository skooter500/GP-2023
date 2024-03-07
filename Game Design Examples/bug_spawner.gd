extends Node2D

var bug_scene:PackedScene

func _ready():
	bug_scene = load("res://bug.tscn")

func _on_timer_timeout():
	var s = get_viewport().size
	var bug = bug_scene.instantiate()
	bug.position.x = randf_range(20, s.x - 20)
	bug.position.y = randf_range(20, s.x - 20)
	get_tree().root.add_child(bug)
	pass # Replace with function body.
