"""Creates example BayEOS Frames."""

from bayeosframe import BayEOSFrame

# Data Frames, simple
data_frame_simple = BayEOSFrame.factory(0x1)
data_frame_simple.create(values=(2, 4), value_type=0x22)  # Data Type Integer
print data_frame_simple.parse()
data_frame_simple.to_string()
print data_frame_simple.get_name()
print data_frame_simple.get_payload()
print BayEOSFrame.parse_frame(data_frame_simple.frame)

# Data Frame with Channel Offset
data_frame_offset = BayEOSFrame.factory()  # 0x1 is default
data_frame_offset.create([2.3, 4.5], value_type=0x01, offset=2)  # Data Type float
data_frame_offset.to_string()
 
# Data Frame with Channel Indices
data_frame_indices = BayEOSFrame.factory()
data_frame_indices.create(([3, 1], [2, 5]), value_type=0x41)  # Data Type float
data_frame_indices.to_string()

data_frame_indices2 = BayEOSFrame.factory()
data_frame_indices2.create(((3, 1), (2, 5)), value_type=0x42)  # Data Type Integer
data_frame_indices2.to_string()
 
# Message Frames
message_frame = BayEOSFrame().factory(0x4)
message_frame.create(message="This is an important message.")
message_frame.to_string()
print message_frame.get_payload()
 
error_message_frame = BayEOSFrame().factory(0x5)
error_message_frame.create("This is an ERROR message.")
error_message_frame.to_string()
 
# Origin Frame
origin_frame = BayEOSFrame.factory(0xb)
origin_frame.create(origin="My Origin", nested_frame=data_frame_simple.frame)
origin_frame.to_string()
print "Nested frame: " + str(BayEOSFrame.parse_frame(origin_frame.nested_frame))
 
# Binary Frame
binary_frame = BayEOSFrame.factory(frame_type=0xa)
binary_frame.create("This a message to be packed as binary data.")
binary_frame.to_string()

# Delayed Frame
delayed_frame = BayEOSFrame.factory(0x7)
delayed_frame.create(nested_frame=data_frame_simple.frame)
delayed_frame.to_string()

# Timestamp Frames
timestamp_frame_sec = BayEOSFrame.factory(0x9)
timestamp_frame_sec.create(data_frame_simple.frame)
timestamp_frame_sec.to_string()
 
timestamp_frame_msec = BayEOSFrame.factory(0xc)
timestamp_frame_msec.create(data_frame_simple.frame)
timestamp_frame_msec.to_string()