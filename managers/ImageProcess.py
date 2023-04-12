import cv2 
import managers.Equirec2Perspec as E2P
import base64

class ImageProcess():
    def __init__(self, file_path) -> None:
        self.equirec = E2P.Equirectangular(file_path)
    
    def get_image(self, FOV, theta, phi, height, width):
        image = self.equirec.GetPerspective(FOV, theta, phi, height, width)
        retval, buffer = cv2.imencode('.jpg', image)
        jpg_as_text = base64.b64encode(buffer).decode("utf-8") 
        return jpg_as_text


