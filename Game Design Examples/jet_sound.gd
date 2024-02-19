extends AudioStreamPlayer2D

@onready var player = $".."
# Called when the node enters the scene tree for the first time.
func _ready():
	play()
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var f = player.linear_velocity.length()
	print(f)
	volume_db = remap(f, 0, 400, -80, 20)
	pass
