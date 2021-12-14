extends KinematicBody2D

export var walk_speed = 4.0
const TILE_SIZE = 16

signal hitting_enemy_signal

onready var anim_tree = $AnimationTree
onready var anim_state = anim_tree.get("parameters/playback")
onready var ray = $BlockingRayCast2D
onready var enemy_ray = $EnemyRayCast2D
onready var zone_ray = $ZoneRayCast2D

var initial_position = Vector2(0, 0)
var input_direction = Vector2(1, 0)
var is_moving = false
var percent_move_to_next_tile = 0.0
var is_pause = true
var check = 0

enum PlayerState { IDLE, WALKING, TURNING }
enum FacingDirection { LEFT, RIGHT, UP, DOWN }

var player_state = PlayerState.IDLE
var facing_direction = FacingDirection.DOWN

func _ready():
	anim_tree.active = true
	initial_position = position
	anim_tree.set("parameters/Idle/blend_position", input_direction)
	anim_tree.set("parameters/Walk/blend_position", input_direction)
	anim_tree.set("parameters/Turn/blend_position", input_direction)
	started()
	
func _physics_process(delta):
	if player_state == PlayerState.TURNING or is_pause == true:
		return
	if is_moving == false:
		is_pause = false
		process_player_input()
	elif input_direction != Vector2.ZERO:
		is_pause = false
		anim_state.travel("Walk")
		move(delta)
	else:
		anim_state.travel("Idle")
		is_moving = false

func process_player_input():
	if input_direction.y == 0.0:
		input_direction.x = int(Input.is_action_pressed("ui_right")) - int(Input.is_action_pressed("ui_left"))
	if input_direction.x == 0.0:
		input_direction.y = int(Input.is_action_pressed("ui_down")) - int(Input.is_action_pressed("ui_up"))
	
	if input_direction != Vector2.ZERO:
		anim_tree.set("parameters/Idle/blend_position", input_direction)
		anim_tree.set("parameters/Walk/blend_position", input_direction)
		anim_tree.set("parameters/Turn/blend_position", input_direction)
		
		if need_to_turn():
			player_state = PlayerState.TURNING
			anim_state.travel("Turn")
		else:	
			initial_position = position
			is_moving = true
	else:
		anim_state.travel("Idle")

func need_to_turn():
	var new_facing_direction
	if input_direction.x < 0:
		new_facing_direction = FacingDirection.LEFT
	elif input_direction.x > 0:
		new_facing_direction = FacingDirection.RIGHT
	elif input_direction.y < 0:
		new_facing_direction = FacingDirection.UP
	elif input_direction.y > 0:
		new_facing_direction = FacingDirection.DOWN
	
	if facing_direction != new_facing_direction:
		facing_direction = new_facing_direction
		return true
	facing_direction = new_facing_direction
	return false

func finished_turning():
	player_state = PlayerState.IDLE

func move(delta):
	var desired_step = input_direction * TILE_SIZE / 2
	ray.cast_to = desired_step
	ray.force_raycast_update()
	
	enemy_ray.cast_to = desired_step
	enemy_ray.force_raycast_update()
	
	zone_ray.cast_to = desired_step
	zone_ray.force_raycast_update()
	
	if enemy_ray.is_colliding():
		emit_signal("hitting_enemy_signal")
		is_moving = false
		position = initial_position + TILE_SIZE * input_direction * percent_move_to_next_tile
	elif zone_ray.is_colliding():
		fade_in()
	elif !ray.is_colliding():
		percent_move_to_next_tile += walk_speed * delta
		if percent_move_to_next_tile >= 1.0:
			position = initial_position + TILE_SIZE * input_direction
			percent_move_to_next_tile = 0.0
			is_moving = false
		else:
			position = initial_position + TILE_SIZE * input_direction * percent_move_to_next_tile
	else:
		is_moving = false

func started():
	print("started")
	is_pause = true
	StartGame.connect("started_scene", self, "finished_start")

func finished_start():
	print("finished_start")
	if check < 1:
		is_pause = false
		check += 1
	return

func fade_in():
	$AnimationPlayer.play("FadeIn")

func change_position():
	print("change_postion")
	$AnimationPlayer.play("FadeOut")
	position = Vector2(200, -568)
	initial_position = position
	is_moving = false
	anim_tree.set("parameters/Idle/blend_position", Vector2(1, 0))
	is_pause = true
	DialogueChecking.emit_signal("finished_dialogue", "No")

