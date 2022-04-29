import pylsl

info = pylsl.StreamInfo(name='Dummy', type='Markers', channel_count=1,
                        channel_format=pylsl.cf_string, source_id='Dummy')
outlet = pylsl.StreamOutlet(info)

while True:
    outlet.push_sample(['Dummy'])