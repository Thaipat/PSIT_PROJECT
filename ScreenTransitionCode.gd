extends Control

func _ready():
	visible = false
	EnterZone.connect("change_screen", self, "screen_transition")
	pass

func screen_transition():
	visible = true
	print("yes")
	$AnimationPlayer.play("FadeIn")

func finished_fading():
	EnterZone.emit_signal("entered_zone")
	$AnimationPlayer.play("FadeOut")
