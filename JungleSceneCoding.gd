extends Node2D

var dialogues = []
var current_dialogue_id = 0
var can_press = true
var check = "Yes"
var check2 = 0

func _ready():
	$CanvasLayer/ColorRect.visible = false
	$CanvasLayer/Panel2.visible = false
	$Pina.visible = false
	$Heal.visible = false
	$CanvasLayer/Panel/Pina.visible = false
	$Player.visible = false
	$CanvasLayer/Panel.visible = false
	$Player.position = Vector2(-24, -24)
	$Sprite.position = Vector2(-24, -24)
	$CanvasLayer/Tutorial.visible = true
	StartGame.emit_signal("start_scene")
	DialogueChecking.connect("finished_dialogue", self, "cutscene_before_battle")
	EnterZone.connect("entered_zone", self, "cutscene_after_battle")

func _input(event):
	
	if event.is_action_pressed("Accept") and can_press == true:
		next_line()
		check2 += 1
	
	if check2 == 1000:
		$CanvasLayer/Panel/Text.text = "someone...... help......?"
	elif check2 == 1001:
		$CanvasLayer/Panel/Text.text = "I can't die here......"
	elif check2 == 1002:
		$CanvasLayer/Panel.visible = false
		$AnimationPlayer.play("Fade2")
	elif check2 == 100:
		$CanvasLayer/Panel.visible = false
		$AnimationPlayer.play("NextScene")
	elif check2 == 10000:
		$CanvasLayer/Panel/Text.text = "I have to find someone to help carry him but I have to heal his wound first."
	elif check2 == 10001:
		$CanvasLayer/Panel.visible = false
		$AnimationPlayer.play("HealScene")
	
func next_line():
	if current_dialogue_id == 0:
		$CanvasLayer/Tutorial.visible = false
		$AnimationPlayer.play("FadeIn")
		can_press = false
		current_dialogue_id += 1
	elif current_dialogue_id == 8:
		can_press = false
		$AnimationPlayer.play("MoveToPool")
	current_dialogue_id += 1
	print(current_dialogue_id)
	if current_dialogue_id == 2:
		$CanvasLayer/Panel/Text.text = "ughhh......."
	elif current_dialogue_id == 3:
		$CanvasLayer/Panel/Text.text = "Where am I?"
	elif current_dialogue_id == 4:
		$CanvasLayer/Panel/Text.text = "and How did I get here?"
	elif current_dialogue_id == 5:
		$CanvasLayer/Panel/Text.text = "and why do I feel hurt right at my bottom?"
	elif current_dialogue_id == 6:
		$CanvasLayer/Panel/Text.text = "wait........."
	elif current_dialogue_id == 7:
		$CanvasLayer/Panel/Text.text = "A TAIL!!!! WHAT IS THIS?!?!"
	elif current_dialogue_id == 8:
		$CanvasLayer/Panel/Text.text = "CLAWS TOO!!!! I'VE BEEN TURNED INTO A MONSTER OR SOMETHING?"
	elif current_dialogue_id == 9:
		$CanvasLayer/Panel/Text.text = "AM I DREAMING?!?! A DOG?!?!"
	elif current_dialogue_id == 10:
		$CanvasLayer/Panel/Text.text = "AND HOW DID I GET HERE?!?! WHY CAN'T I REMEMBER ANYTHING?!?!"
	elif current_dialogue_id == 11:
		$CanvasLayer/Panel/Text.text = "clam down calm down....... sigh"
	elif current_dialogue_id == 12:
		$CanvasLayer/Panel/Text.text = "For now I guess there no point sitting around here."
	elif current_dialogue_id == 13:
		$CanvasLayer/Panel/Text.text = "Guess I just have to look around."
	elif current_dialogue_id == 14:
		$CanvasLayer/Panel/Text.text = "having a tail is so weird."
	if current_dialogue_id == 15:
		$CanvasLayer/Panel/Raiba_img.visible = false
		$CanvasLayer/Panel.visible = false
		StartGame.emit_signal("started_scene")
		$AnimationPlayer.play("Fade")
		return
	elif current_dialogue_id > 16:
		return

func finished_fading():
	$CanvasLayer/Panel/Raiba_img.visible = true
	$CanvasLayer/Panel.visible = true
	can_press = true

func finished_moving_to_pool():
	can_press = true

func finished_fade():
	$Player.visible = true
	$Sprite.visible = false
	$AnimationPlayer.play("FadeOut")

func finished_fade2():
	$Pina.visible = true
	$AnimationPlayer.play("FadeOut2")

func finished_fade_out2():
	$CanvasLayer/Panel.visible = true
	$CanvasLayer/Panel/Raiba_img.visible = false
	$CanvasLayer/Panel/Pina.visible = true
	$CanvasLayer/Panel/Name.text = "??? (Rabbit)"
	$CanvasLayer/Panel/Text.text = "huh?"
	check2 = 99

func finished_next_scene():
	$CanvasLayer/Panel.visible = true
	$CanvasLayer/Panel/Text.text = "oh no he's bleeding out"
	check2 = 9999

func finished_heal_scene():
	if check == "Yes":
		$AnimationPlayer.play("End")
		check = "No"
	$CanvasLayer/Panel2.visible = true

func cutscene_before_battle(checking):
	if checking == "No":
		$Player.visible = false
		$Sprite.position = Vector2(200, -568)
		$Sprite.visible = true
		$AnimationPlayer.play("MoveToBattle")

func finished_move_to_battle():
	DialogueChecking.emit_signal("started_dialogue")

func cutscene_after_battle():
	$Enemy.visible = false
	$Sprite.rotation_degrees = -90
	$Sprite.position = Vector2(248, -552)
	check2 = 999
	$CanvasLayer/Panel/Raiba_img.visible = true
	$CanvasLayer/Panel.visible = true
	$CanvasLayer/Panel/Text.text = "I'm bleeding if this go on I'll bleed out."



