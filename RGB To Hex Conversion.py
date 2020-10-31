'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
'''

def rgb(r, g, b):
    def dec_to_hex(x):
        if x <= 0:
            if len(hex(0).lstrip('0x').upper()) >= 2:
                return hex(0).lstrip('0x').upper()
            else:
                return '00' + hex(0).lstrip('0x').upper()
        elif x > 255:
            return hex(255).lstrip('0x').upper()
        else:
            if len(hex(x).lstrip('0x').upper()) >= 2:
                return hex(x).lstrip('0x').upper()
            else:
                return '0' + hex(x).lstrip('0x').upper()

    return dec_to_hex(r) + dec_to_hex(g) + dec_to_hex(b)




