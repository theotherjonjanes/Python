#!/usr/bin/osascript

script greenMachineGo
	tell application "Terminal"
		do script "greenmachine"
	end tell
end script

script greenMachineEnd
	tell application "Terminal"
		quit
	end tell
end script

on greenMachine(gm)
	run greenMachineGo
	delay 10
	run gm
end greenMachine

greenMachine(greenMachineEnd)