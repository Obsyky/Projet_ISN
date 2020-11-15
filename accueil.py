#Entete de classes.py
import pygame as pg
from constantes import *
import yahtzee
import de

pg.init()

#Mise en place de la fenetre
ecran= pg.display.set_mode(fen)
pg.display.set_caption(nomEcran_accueil)

#Images

    #Background
background = pg.image.load(image_background).convert()
background = pg.transform.scale(background, fen)

    #Background 2
background2 = pg.Surface(fen)
background2.fill((226, 226, 224))

    #Bouton Jouer
bouton_jouer = pg.image.load(image_jouer).convert_alpha()
bouton_jouer = pg.transform.scale(bouton_jouer, (LHbouton_jouer))

    #Bouton Crédit
bouton_credit = pg.image.load(image_credit).convert_alpha()
bouton_credit = pg.transform.scale(bouton_credit, (LHbouton_credit))

    #Bouton Retour
bouton_retour = pg.image.load(image_retour).convert_alpha()
bouton_retour = pg.transform.scale(bouton_retour, (LHbouton_retour))

    #Bouton Yahtzee
bouton_yahtzee = pg.image.load(bouton_yahtzee).convert_alpha()
bouton_yahtzee = pg.transform.scale(bouton_yahtzee, (LHbouton_yahtzee))

    #Bouton mario
mario = pg.image.load(mario).convert_alpha()
mario = pg.transform.scale(mario, (LHbouton_mario))

    #Bouton Simude
bouton_simude = pg.image.load(bouton_simude).convert_alpha()
bouton_simude = pg.transform.scale(bouton_simude, (LHbouton_simude))

    #Bulle
bulle = pg.image.load(bulle).convert_alpha()
bulle = pg.transform.scale(bulle, (LHbouton_bulle))

    #Fond crédit
fond_credit = pg.image.load(fond_credit).convert_alpha()
fond_credit = pg.transform.scale(fond_credit, (fen))


#Boucle infinie
principal = True
accueila = True
play = False
credit = False
while principal:  
  
    #Boucle accueil
    while accueila:
        
        ecran.blit(background, (0, 0))
        ecran.blit(bouton_jouer, (xyzone_bouton_jouer))
        ecran.blit(bouton_credit, (xyzone_bouton_credit))
        pg.display.flip()
    
        for event in pg.event.get():

            if event.type == pg.QUIT :
                pg.quit()
                quit()
        
            if event.type == pg.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if (xzone_bouton_jouer <= pos[0] < (xzone_bouton_jouer + Lbouton_jouer)) and (yzone_bouton_jouer <= pos[1] < (yzone_bouton_jouer + Hbouton_jouer)):
                        accueila = False
                        play = True    
                    if (xzone_bouton_credit <= pos[0] < (xzone_bouton_credit + Lbouton_credit)) and (yzone_bouton_credit <= pos[1] < (yzone_bouton_credit + Hbouton_credit)):
                        accueila = False
                        credit = True
    
    #Boucle jouer                
    while play:
        
        ecran.blit(background2, (0, 0))
        ecran.blit(bouton_retour, (xyzone_bouton_retour))
        ecran.blit(bouton_yahtzee, (xyzone_bouton_yahtzee))
        ecran.blit(mario, (xyzone_bouton_mario))
        ecran.blit(bouton_simude, (xyzone_bouton_simude))
        ecran.blit(bulle, (xyzone_bouton_bulle))
        pg.display.flip()
    
        for event in pg.event.get():

            if event.type == pg.QUIT :
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                        accueila = True
                        play = False
                    if (xzone_bouton_yahtzee <= pos[0] < (xzone_bouton_yahtzee + Lbouton_yahtzee)) and (yzone_bouton_yahtzee <= pos[1] < (yzone_bouton_yahtzee + Hbouton_yahtzee)):
                        yahtzee.yams()
                    if (xzone_bouton_simude <= pos[0] < (xzone_bouton_simude + Lbouton_simude)) and (yzone_bouton_simude <= pos[1] < (yzone_bouton_simude + Hbouton_simude)):
                        de.simu()
    
    #Boucle credit       
    while credit:
    
        ecran.blit(background2, (0, 0))
        ecran.blit(bouton_retour, (xyzone_bouton_retour))
        ecran.blit(fond_credit, (0,0))
        pg.display.flip()
    
        for event in pg.event.get():

            if event.type == pg.QUIT :
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                    pos = event.pos
                    if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                        credit = False
                        accueila = True

            
pg.quit()
quit()