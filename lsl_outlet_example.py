import pylsl

# Create a new stream info
info = pylsl.StreamInfo(name='Dummy', type='Markers', channel_count=1,
                        channel_format=pylsl.cf_string, source_id='Dummy')
# Create the outlet
outlet = pylsl.StreamOutlet(info)

# Run forever:
while True:
    # Push the data to LSL - a string that says 'Dummy'
    outlet.push_sample(['Dummy'])