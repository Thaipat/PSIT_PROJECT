extends Area2D

func _ready():
	pass

func _on_Scene_Zone_body_entered(body):
	if body.is_in_group("Player"):
		print("emit_change_screen")
		EnterZone.emit_signal("change_screen")
		done()
	pass

func done():
	queue_free()
