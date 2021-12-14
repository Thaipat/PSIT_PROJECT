extends Area2D

export var character_name : String = ""
export var lvl : String = ""

func _ready():
	pass

func _on_Enemy_body_entered(body):
	if body.is_in_group("Player"):
		EventHandler.emit_signal("battle_started", character_name, lvl)
	pass
