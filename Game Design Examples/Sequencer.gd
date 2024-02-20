extends Node

var samples:Array



# Called when the node enters the scene tree for the first time.
func _ready():
	# Set the path to the folder containing the WAV files
	var folder_path = "res://sounds/"

	# List all files in the folder
	var dir = Directory.new()
	if dir.open(folder_path) == OK:
		dir.list_dir_begin()
		var file_name = dir.get_next()
		while file_name != "":
			# Check if the file is a WAV file
			if file_name.extension_to_lower() == "wav":
				# Load the WAV file as an AudioStreamSample
				var audio_stream = load(folder_path + file_name) as AudioStreamWAV
				if audio_stream != null:
					# Print the name of the WAV file
					print("Loaded WAV file: ", file_name)
					
					# Do something with the audio stream, such as playing it
					# For example:
					# $AudioStreamPlayer.play(audio_stream)
			file_name = dir.get_next()
		dir.list_dir_end()
	else:
		print("Failed to open directory:", folder_path)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
