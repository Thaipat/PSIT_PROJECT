extends CanvasLayer

var dialogue = []
var current_dialogue = -1
var order = "No"

func _ready():
	DialogueChecking.connect("started_dialogue", self, "play")
	$Panel.visible = false

func play():
	print("Test")
	order = "Yes"
	$Panel.visible = true
	$Panel/Text.visible = true
	$shiba.visible = true
	$Nalozgo.visible = false
	$Panel/Name.text = "Raiba"
	$Panel/Text.text = "Hmmmm?"
func _input(event):
	if event.is_action_pressed("Accept"):
		if order == "Yes":
			next_line()

func next_line():
	current_dialogue += 1
	if current_dialogue >= 8:
		$Panel.visible = false
		$shiba.visible = false
		$Nalozgo.visible = false
		EventHandler.emit_signal("battle_started", "Nalozgo", "???")
		return
	elif current_dialogue == 0:
		$shiba.visible = true
		$Nalozgo.visible = false
		$Panel/Name.text = "Raiba"
		$Panel/Text.text = "OOCHH!!! HEY WHAT AR-"
	elif current_dialogue == 1:
		$shiba.visible = false
		$Nalozgo.visible = true
		$Panel/Name.text = "???"
		$Panel/Text.text = "You're special....."
	elif current_dialogue == 2:
		$shiba.visible = true
		$Nalozgo.visible = false
		$Panel/Name.text = "Raiba"
		$Panel/Text.text = "What?....."
	elif current_dialogue == 3:
		$shiba.visible = false
		$Nalozgo.visible = true
		$Panel/Name.text = "???"
		$Panel/Text.text = "You're a threat to my plan."
	elif current_dialogue == 4:
		$shiba.visible = false
		$Nalozgo.visible = true
		$Panel/Name.text = "???"
		$Panel/Text.text = "and that mean you need to be eliminated."
	elif current_dialogue == 5:
		$shiba.visible = false
		$Nalozgo.visible = true
		$Panel/Name.text = "???"
		$Panel/Text.text = "tch...."
	elif current_dialogue == 6:
		$shiba.visible = true
		$Nalozgo.visible = false
		$Panel/Name.text = "Raiba"
		$Panel/Text.text = "what was that?"
	elif current_dialogue == 7:
		$shiba.visible = false
		$Nalozgo.visible = true
		$Panel/Name.text = "???"
		$Panel/Text.text = "guess I have to do the hard way huh?"

