class Rectangle() :
    _nbrrectangles = 0
    def __init__(self, longueur = 1, largeur = 2):
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._nbrrectangles += 1
    
    def getLongueur(self) :
        return self._longueur
    
    def setLongueur(self, longueur) :
        if longueur > 0:
            return longueur
        else :
            print("La longueur doit être positive")

    def getLargeur(self) :
        return self._largeur
    
    def setLargeur(self, largeur) :
        if largeur > 0:
            return largeur
        else :
            print("La largeur doit être positive")

    def getNbrrectangles(self) :
        return Rectangle._nbrrectangles
    
    def equals(self, R) :
        if self.getLargeur() == R.getLargeur() and self.getLongueur() == R.getLongueur() :
            return True
        else :
            return False
    
    def perimetre(self) :
        return (self.getLargeur() + self.getLongueur())*2
    
    def Surface(self) :
        return self.getLargeur() * self.getLongueur()
    
    def ToString(self) :
        return "Longueur : ", self.setLongueur(self._longueur), "Largeur : ", self.setLargeur(self._largeur), "surface de rectangle : ", self.Surface(), "perimetre de rectangle : ", self.perimetre(), "nombre de rectangles : ", Rectangle._nbrrectangles
    
class parallelepipede(Rectangle) :
    def __init__(self, hauteur = 3) :
        super().__init__()
        self._hauteur = hauteur

    def getHauteur(self) :
            return self._hauteur
    
    def setHauteur(self, hauteur) :
        if hauteur > 0:
                self._hauteur = hauteur
        else :
            print("La hauteur doit être positive")
    
    def Volume(self):
        return super().Surface()*self.getHauteur()
    
    def Surface(self):
        return super().Surface()*4
    
    def ToString(self):
        return super().ToString(), "Surface : ", self.Surface(), "volume : ", self.Volume()






rec1 = Rectangle(2,3)
print(rec1.ToString())
paral1 = parallelepipede(5)
print(paral1.ToString())