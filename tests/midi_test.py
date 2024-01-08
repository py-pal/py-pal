import mido

port = mido.open_output("test")
mid = mido.MidiFile("tests/pal1.mid")
for msg in mid.play():
    port.send(msg)
