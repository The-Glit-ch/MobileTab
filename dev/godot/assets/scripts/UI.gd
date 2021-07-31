extends Node

#Get our UI stuff
onready var OutText:Label = $"Out"
onready var IPInput:TextEdit = $"IP_Input"
onready var PortInput:TextEdit = $"Port_Input"
onready var ConnectButton:Button = $"Connect_B"

func _ready():
	#We first check for any errors
	if Global.is_error:
		OutText.text = Global.error_msg
	
	IPInput.connect("text_changed",self,"_IPInput_Text_Changed")
	PortInput.connect("text_changed",self,"_PortInput_Text_Changed")
	ConnectButton.connect("pressed",self,"_connect")


#Connections
func _IPInput_Text_Changed():
	Global.websocket_url = IPInput.text.replace(" ","")

func _PortInput_Text_Changed():
	Global.websocket_port = PortInput.text.replace(" ","")

func _connect():
	get_tree().change_scene("res://assets/scenes/Draw.tscn")
