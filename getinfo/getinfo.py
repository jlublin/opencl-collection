import pyopencl as cl

platforms = cl.get_platforms()
pi = 0

for platform in platforms:
	pi += 1

	print("Platform %d" % (pi))
	print("Name: %s" % (platform.get_info(cl.platform_info.NAME)))
	print("Vendor: %s" % (platform.get_info(cl.platform_info.VENDOR)))
	print("Version: %s" % (platform.get_info(cl.platform_info.VERSION)))
	print("Profile: %s" % (platform.get_info(cl.platform_info.PROFILE)))
	print("Extensions: %s" % (platform.get_info(cl.platform_info.EXTENSIONS)))

	devices = platform.get_devices()
	di = 0
	
	for device in devices:
		di += 1
		print("\nDevice %d" % (di))
		print("Name: %s" % (device.get_info(cl.device_info.NAME)))
		print("Vendor: %s" % (device.get_info(cl.device_info.VENDOR)))
		print("Version: %s" % (device.get_info(cl.device_info.VERSION)))
		print("Max clock frequency(?): %s" % (device.get_info(cl.device_info.MAX_CLOCK_FREQUENCY)))
		print("Compute units: %s" % (device.get_info(cl.device_info.MAX_COMPUTE_UNITS)))
		print("Max mem alloc: %s" % (device.get_info(cl.device_info.MAX_MEM_ALLOC_SIZE)))
		print("Local mem size: %s" % (device.get_info(cl.device_info.LOCAL_MEM_SIZE)))
		print("Local mem type: %s" % (device.get_info(cl.device_info.LOCAL_MEM_TYPE)))
		print("Address bits: %s" % (device.get_info(cl.device_info.ADDRESS_BITS)))
		print("Global mem size: %s" % (device.get_info(cl.device_info.GLOBAL_MEM_SIZE)))
		print("Max work group size: %s" % (device.get_info(cl.device_info.MAX_WORK_GROUP_SIZE)))
		print("Max work item dimension: %s" % (device.get_info(cl.device_info.MAX_WORK_ITEM_DIMENSIONS)))
		print("Max work item sizes: %s" % (device.get_info(cl.device_info.MAX_WORK_ITEM_SIZES)))
		print("Max constant args: %s" % (device.get_info(cl.device_info.MAX_CONSTANT_ARGS)))
		print("Max constant buffer size: %s" % (device.get_info(cl.device_info.MAX_CONSTANT_BUFFER_SIZE)))
		
