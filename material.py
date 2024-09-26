from MathLib import reflectVector
from lights import *
OPAQUE = 0
REFLECTIVE = 1
TRANSPARENT = 2

class  Material(object):
    def  __init__(self, diffuse, spec = 1.0, ks = 0.0, matType = OPAQUE):
        self.diffuse = diffuse
        self.spec = spec
        self.ks = ks
        self.matType = matType


    def GetSurfaceColor(self, intercept, renderer, recursion = 0):
        lightColor = [0,0,0]
        reflectColor = [0,0,0]
        finalColor = self.diffuse


        for light in renderer.light:
            shadowIntercept = None

            if light.lightType == "Directional":
                lightDir = [-i for i in light.direction] 
                shadowIntercept = renderer.glCastRay(intercept.point,lightDir,intercept.obj, )

            if shadowIntercept == None:
                lightColor = [(lightColor[i] + light.GetSpecularColor(intercept, renderer.camera.translate)[i])for i in range(3)]
                
                if self.matType == OPAQUE:
                     lightColor = [(lightColor[i] + light.GetLightColor(intercept)[i]) for i in range(3)]
                else:
                    reflectColor = renderer.clearColor




        if self.matType == REFLECTIVE:
            rayDir = [-i for i in intercept.rayDirection] 
            reflect = reflectVector(intercept.normal, rayDir)
            reflectIntercept = renderer. glCastRay(intercept.point, reflect, intercept.obj, recursion + 1 )
            if reflectIntercept !=  None:
                reflectColor = reflectIntercept.obj.material.GetSurfaceColor(reflectIntercept, renderer, recursion + 1  )
            else:
                reflectColor = renderer.glEnvMapColor(intercept.point, reflect)

        finalColor = [(finalColor[i] * (lightColor[i] + reflectColor[i])) for i in range(3)]
        finalColor = [min(1,finalColor[i]) for i in range(3)]
        return finalColor
