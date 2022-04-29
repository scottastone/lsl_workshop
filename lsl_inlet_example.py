import pylsl

# Check if there are any streams available named 'Dummy'
# NOTE: lsl_outlet_example.py must be running for this to work!
streams = pylsl.resolve_stream('name', 'Dummy')
inlet = pylsl.StreamInlet(streams[0])

# Run forever:
while True:
    # Check if there's any data available
    sample, timestamp = inlet.pull_sample()
    # Print to the console
    print(sample, timestamp)