extends Node2D

@export var s:Sprite2D

func _ready():
	$HSlider.value = 1
	pass
	
func _process(delta):
	var a:float
	var b
	
	a = 1
	b = 6.6
	
	a = b + 10
	
	
	# && || !	
	
	if a == 10:
		print("a is 10")
	else:
		print("a is not 10")
	
	if a == 10 && b > 7:
		print("something")	
		
	for i in range(10):
		print(i)
		
	for i in range(5, 10):
		print(i)

func _on_button_pressed():
	$AudioStreamPlayer2D.play()
	pass # Replace with function body.


func _on_h_slider_changed():
	
	# var pitch:AudioEffectPitchShift = AudioServer.get_bus_effect(0, 0)
	
	# pitch.pitch_scale = $HSlider.value
	pass # Replace with function body.


func _on_h_slider_value_changed(value):
	var pitch:AudioEffectPitchShift = AudioServer.get_bus_effect(0, 1)
	
	pitch.pitch_scale = $HSlider.value
	
	pass # Replace with function body.


func _on_low_pass_value_changed(value):
	# var low:AudioEffectLowPassFilter = AudioServer.get_bus_effect(0, 0)
	# low.cutoff_hz = value

	var reverb:AudioEffectReverb = AudioServer.get_bus_effect(0, 0)
	# low.cutoff_hz = value
	reverb.room_size = value
	pass # Replace with function body.


func _on_timer_timeout():
	$AudioStreamPlayer2D.play()
	pass # Replace with function body.


func _on_timer_2_timeout():
	$AudioStreamPlayer2D3.play()
	pass # Replace with function body.
