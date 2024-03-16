from vimba import *

with Vimba.get_instance() as vimba:
    interfaces = vimba.get_all_interfaces()
    with interfaces[0] as interface:
        for feat in interface.get_all_features():

            if interface.get_name('Old one camera name'):
                # get_name(self) -> str: #\vimba\interface.py from 139~
                print('New one camera name')

            elif interface.get_model('Old one camera model'):
                # get_type(self) -> InterfaceType:
                print('New one camera model')

            elif interface.get_id('Old one camera id'):
                # get_id(self) -> str:
                print('New one camera id')

            elif interface.get_serial('Old one camera serial'):
                # get_serial(self) -> str: #\vimba\interface.py until ~149 (or 161)
                print('New one camera serial')

            elif interface.get_interface_id('Old one camera interface_id'):
                # discover_interface(id_: str) -> Interface: #\vimba\interface.py -385 (or 397)
                print('New one camera interface_id')

            else:
                print(feat)
