import pylsl

streams = pylsl.resolve_stream('name', 'Dummy')
inlet = pylsl.StreamInlet(streams[0])

while True:
    sample, timestamp = inlet.pull_sample()
    print(sample, timestamp)