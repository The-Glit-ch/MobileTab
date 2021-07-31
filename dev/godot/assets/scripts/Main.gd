extends Node2D

#Websocket stuff
var _client = WebSocketClient.new()

#Vars
var touch_position:Vector2 = Vector2(0,0)
var prev_touch_position:Vector2 = Vector2(0,0)
var connected:bool = false

func _ready():
	#Reset our global
	Global.is_error = false
	Global.error_msg = "None"
	
	#Make Connections
	_client.connect("connection_closed", self, "_closed")
	_client.connect("connection_error", self, "_closed")
	_client.connect("connection_established", self, "_connected")

	# Initiate connection to the given URL.
	var err = _client.connect_to_url("ws://" + Global.websocket_url + ":" + Global.websocket_port)
	if err != OK:
		Global.is_error = true
		Global.error_msg = "Error Connecting. Make sure you did not add any extra lines or spaces when entering the IP and Port"
		get_tree().change_scene("res://assets/scenes/Connect.tscn")
		set_process(false)

func _process(delta):
	_client.poll()

func _input(event):
	if event is InputEventScreenDrag:
		touch_position = Vector2(clamp(event.position.x + prev_touch_position.x,0,1920),clamp(event.position.y + prev_touch_position.y,0,1080))
		prev_touch_position = event.position
		if connected:
			sendData(touch_position)

#Custom
func sendData(data):
	_client.get_peer(1).put_packet(String(data).to_utf8())

#Connects
func _closed(was_clean = false):
	Global.is_error = true
	Global.error_msg = "Connection Closed"
	get_tree().change_scene("res://assets/scenes/Connect.tscn")

func _connected(proto = ""):
	$"Out".text = "Connected"
	connected = true
