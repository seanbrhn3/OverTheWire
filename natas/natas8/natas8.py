import base64
import binhex
encodedSecret = "3d3d516343746d4d6d6c315669563362"
decoded_but_reversed = "==QcCtmMml1ViV3b"
print(base64.b64decode(decoded_but_reversed[::-1]))
