extends Control

var check = 0
var check2 = "No"
var check3 = "No"
var check4 = 1

func _ready():
	$Background/TestingBoss.visible = true
	visible = false
	$Background.visible = false
	EventHandler.connect("battle_started", self, "init")
	pass

func init(character_name, lvl):
	visible = true
	$ColorRect.visible = true
	$AnimationPlayer.play("FadeIn")
	get_tree().paused = true
	pass

func _input(event):
	if check == 100000:
		$Background/Scrip/Text.text = "What do you want with me?"
	if check == 100001:
		$Raiba.visible = false
		$Nalozgo.visible = true
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.text = "It's none of your business."
	if check == 100002:
		$Raiba.visible = true
		$Nalozgo.visible = false
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.text = "I guess there is no other choice other than fight."
	if check == 100003:
		$Raiba.visible = false
		$Background/Scrip.visible = false
		$Background/Panel.visible = true
		$Background/Panel/Text_While_Fight.text = "Select your action!!"
		if check2 == "No":
			$Background/Panel/Fight_Button.grab_focus()
			check2 = "Yes"
	if check == 10000:
		$Background/Scrip/System.visible = false
		$Raiba.visible = true
		$Background/Scrip/Text.visible = true
		$Background/Scrip/Name.visible = true
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.text = "WHAT!! I CAN DO THAT!!!"
	if check == 10001:
		$Raiba.visible = false
		$Nalozgo.visible = true
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.text = "......"
	if check == 10002:
		$Nalozgo.visible = false
		$Background/Scrip/Text.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Scrip/System.visible = true
		$Background/Scrip/System.text = "You are attacked by villain"
		if check3 == "No":
			$AnimationPlayer.play("EnemyAttack")
			check3 = "Yes"
	if check == 10003:
		$Background/Scrip/System.visible = false
		$Raiba.visible = true
		$Background/Scrip/Text.visible = true
		$Background/Scrip/Name.visible = true
		$Background/Scrip/Text.text = "Och!!! that hurts. I need to be more careful."
	if check == 10004:
		$Raiba.visible = false
		$Background/Scrip.visible = false
		if check2 == "Yes":
			$Background/Panel.visible = true
			$Background/Panel/Fight_Button.grab_focus()
			check2 = "No"
	if check == 1000:
		$Background/Scrip/System.visible = false
		$Raiba.visible = true
		$Background/Scrip/Name.visible = true
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.visible = true
		$Background/Scrip/Text.text = "I CAN DO THAT TOO!!! This is amazing!!!"
	if check == 1001:
		$Raiba.visible = false
		$Nalozgo.visible = true
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.text = "tch.... You're getting on my nerves...."
	if check == 1002:
		$Raiba.visible = true
		$Nalozgo.visible = false
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.text = "Oh no!!! I think I'm in a very bad position!!!"
	if check == 1003:
		$Background/Scrip.visible = false
		$Raiba.visible = false
		if check2 == "No":
			$Background/Panel.visible = true
			$Background/Panel/Fight_Button.grab_focus()
			check2 = "Yes"
	if check == 100:
		$Background/Scrip/System.text = "You are attacked by villain"
		if check3 == "Yes":
			$AnimationPlayer.play("EnemyAttack")
			check3 = "No"
	if check == 101:
		$Background/Scrip/System.visible = false
		$Raiba.visible = true
		$Background/Scrip/Name.visible = true
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.visible = true
		$Background/Scrip/Text.text = "Well that's help but it's still hurt though."
	if check == 102:
		$Nalozgo.visible = true
		$Raiba.visible = false
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.text = "It's time to end this."
	if check == 103:
		$Raiba.visible = true
		$Nalozgo.visible = false
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.text = "What!! What are you going to do?!?!"
	if check == 104:
		$Raiba.visible = false
		$Nalozgo.visible = true
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.text = "You'll see soon enough."
	if check == 105:
		$Nalozgo.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Scrip/Text.visible = false
		$Background/Scrip/System.visible = true
		$Background/Scrip/System.text = "Enemy using 'FireBall'"
		if check3 == "No":
			$AnimationPlayer.play("EnemySkill")
			check3 = "Yes"
	if check == 106:
		$Background/Scrip/System.visible = false
		$Raiba.visible = true
		$Background/Scrip/Name.visible = true
		$Background/Scrip/Name.text = "Raiba"
		$Background/Scrip/Text.visible = true
		$Background/Scrip/Text.text = "ugh..... not good....."
	if check == 107:
		$Raiba.visible = false
		$Nalozgo.visible = true
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.text = "Good bye"
		if check3 == "Yes":
			$AnimationPlayer.play("EnemyCharge")
			check3 = "No"
	if check == 108:
		$Nalozgo.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Scrip/Text.visible = false
		$Background/Scrip/System.visible = true
		$Background/Scrip/System.text = "suddenly the villain stop mid way when they're about to attack."
	if check == 109:
		$Background/Scrip/System.visible = false
		if check3 == "No":
			$AnimationPlayer.play("EnemyBreak")
			check3 = "Yes"
		$Nalozgo.visible = true
		$Background/Scrip/Name.visible = true
		$Background/Scrip/Name.text = "???"
		$Background/Scrip/Text.visible = true
		$Background/Scrip/Text.text = "ugh..... what?! how is this-"
	if check == 110:
		if check3 == "Yes":
			$AnimationPlayer.play("EnemyDisapear")
			check3 = "No"
		$Nalozgo.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Scrip/Text.visible = false
		$Background/Scrip/System.visible = true
		$Background/Scrip/System.text = "The villain retreat."
	if check == 111:
		if check3 == "No":
			$AnimationPlayer.play("FadeIn2")
			check3 = "Yes"
	if event.is_action_pressed("Accept"):	
		check += 1

func finished_fading():
	$AnimationPlayer.play("FadeOut")
	$Background.visible = true
	$Background/Scrip.visible = true
	$Raiba.visible = true
	$Background/Scrip/Name.text = "Raiba"
	$Background/Scrip/Text.text = "This is bad. I don't have any combat skill. How am I gonna get out of this?"
	check = 99999

func finished_fading2():
	EnterZone.emit_signal("entered_zone")
	$Background.visible = false
	$AnimationPlayer.play("FadeOut")

func _on_Run_Button_pressed():
	$Background/Panel/Text_While_Fight.text = "You can't run away from this situation"


func _on_Fight_Button_pressed():
	if check4 == 1:
		$Background/Panel.visible = false
		$Background/Scrip.visible = true
		$Background/Scrip/Text.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Scrip/System.text = "You hit the villain with your sword"
		$AnimationPlayer.play("PlayerAttack")
		check = 9999
		check4 = 2
	elif check4 == 2:
		$Background/Panel/Text_While_Fight.text = "'Fight' isn't appropriate for this situation."
	elif check4 == 3:
		$Background/Panel/Text_While_Fight.text = "'Fight' isn't appropriate for this situation."

func _on_Guard_Button_pressed():
	if check4 == 1:
		$Background/Panel/Text_While_Fight.text = "'Guard' isn't appropriate for this situation."
	elif check4 == 2:
		$Background/Panel/Text_While_Fight.text = "'Guard' isn't appropriate for this situation."
	elif check4 == 3:
		$Background/Scrip/Text.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Panel.visible = false
		$Background/Scrip.visible = true
		$Background/Scrip/System.visible = true
		$Background/Scrip/System.text = "You brace yourself for impact."
		$AnimationPlayer.play("PlayerGuard")
		check = 99
		check4 = 4


func _on_Skill_Button3_pressed():
	if check4 != 2:
		$Background/Panel/Text_While_Fight.text = "You don't have enought stamina"
	elif check4 == 2:
		$Background/Scrip/Text.visible = false
		$Background/Scrip/Name.visible = false
		$Background/Panel.visible = false
		$Background/Scrip.visible = true
		$Background/Scrip/System.visible = true
		$Background/Scrip/System.text = "You swing your sword pushing a sharp blade made of air hitting the enemy"
		$AnimationPlayer.play("PlayerSkill")
		check = 999
		check4 = 3
	
