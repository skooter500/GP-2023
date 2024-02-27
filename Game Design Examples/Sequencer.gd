extends Node

var samples:Array
var pads:Dictionary

@export var path_str = "res://sounds" 
@export var pad_scene:PackedScene
@export var sample_scene:PackedScene

@export var num_pads = 8

# Called when the node enters the scene tree for the first time.
func _ready():
	# Set the path to the folder containing the WAV files
	var folder_path = "res://sounds/"	
	# make_pads()
	load_samples()
	make_samplees()

func make_pads():
	var w
	var g
	for i in range(num_pads):
		var pad = pad_scene.instantiate()
		var ww:ColorRect = pad.get_node("rect")
		w = ww.get_size().x
		g = w * 0.1
		
		var p = Vector2((i * (w + g)), 0)
		pad.position = p
		add_child(pad)
		
func play_sample(i):
	
	var p:AudioStreamWAV = samples[i]
	$AudioStreamPlayer.stream = p
	$AudioStreamPlayer.play()

func make_samplees():
	for i in range(samples.size()):
		var sample = sample_scene.instantiate()
		var b:Button = sample.get_node("Button")
		b.connect("pressed", play_sample.bind(i))
		var h = b.get_size().y
		
		var p = Vector2(0, h * i * 1.1)
		sample.position = p
		
<<<<<<< HEAD
		b.set_text(samples[i].resource_name)
		add_child(sample)
=======
		patch.find_child("RichTextLabel", true).set_text(samples[i].resource_name)
		patch.find_child("AudioStreamPlayer2D").stream = samples[i]
		add_child(patch)
>>>>>>> 5aba331cda6c5ff34f33281103c3260f8e86df11
		
func load_samples():
	var dir = DirAccess.open(path_str)
	if dir:
		dir.list_dir_begin()
		var file_name = dir.get_next()
		while file_name != "":
			if dir.current_is_dir():
				print("Found directory: " + file_name)
			elif file_name.ends_with(".wav"):				
				var stream
				var file = FileAccess.open(path_str + "/" + file_name, FileAccess.READ)
				var buffer = file.get_buffer(file.get_length())
				stream = AudioStreamWAV.new()
				stream.format = AudioStreamWAV.FORMAT_16_BITS		
				stream.data = buffer
				stream.stereo = true
				stream.resource_name = file_name
				file.close() 
				samples.push_back(stream)
			file_name = dir.get_next()	
