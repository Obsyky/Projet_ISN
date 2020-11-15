#Entete de classes.py
import random
import time
import pygame as pg
from constantes import *
pg.init()

#Mise en place de la fenetre
ecran= pg.display.set_mode(fen)
pg.display.set_caption(nomEcran_de)

#Images

    #Background
background_de = pg.Surface(fen)
background_de.fill((236, 185, 185))

     #Bouton Retour
bouton_retour = pg.image.load(image_retour).convert_alpha()
bouton_retour = pg.transform.scale(bouton_retour, (LHbouton_retour))

    #Bouton 1
bouton_1 = pg.image.load(bouton1).convert_alpha()
bouton_1 = pg.transform.scale(bouton_1, (LHbouton_1))

    #Bouton 2
bouton_2 = pg.image.load(bouton2).convert_alpha()
bouton_2 = pg.transform.scale(bouton_2, (LHbouton_2))

    #Bouton 3
bouton_3 = pg.image.load(bouton3).convert_alpha()
bouton_3 = pg.transform.scale(bouton_3, (LHbouton_3))

    #Bouton txt
bouton_txt = pg.image.load(txt).convert_alpha()
bouton_txt = pg.transform.scale(bouton_txt, (LHbouton_txt))

    #Bouton Lancer
bouton_lancer = pg.image.load(bouton_lancer).convert_alpha()
bouton_lancer = pg.transform.scale(bouton_lancer, (LHbouton_lancer))

    #Bouton home
bouton_home = pg.image.load(bouton_home).convert_alpha()
bouton_home = pg.transform.scale(bouton_home, (LHbouton_home))
    
def simu():    

    principal = True
    choix = True
    choix1 = False
    choix2 = False
    choix3 = False

    while principal :
        
            while choix :
            
                ecran.blit(background_de, (0, 0))
                ecran.blit(bouton_1, (xyzone_bouton_1))
                ecran.blit(bouton_2, (xyzone_bouton_2))
                ecran.blit(bouton_3, (xyzone_bouton_3))
                ecran.blit(bouton_retour, (xyzone_bouton_retour))
                ecran.blit(bouton_txt, (xyzone_bouton_txt))
                pg.display.flip()
            
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()    
                    if event.type == pg.MOUSEBUTTONDOWN:
                        pos = event.pos
                        if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                            return()
                        if (xzone_bouton_1 <= pos[0] < (xzone_bouton_1 + Lbouton_1)) and (yzone_bouton_1 <= pos[1] < (yzone_bouton_1 + Hbouton_1)):
                            choix = False
                            choix1 = True
                            choix1_depart = 1
                        if (xzone_bouton_2 <= pos[0] < (xzone_bouton_2 + Lbouton_2)) and (yzone_bouton_2 <= pos[1] < (yzone_bouton_2 + Hbouton_2)):
                            choix = False
                            choix2 = True
                            choix2_depart = 1
                        if (xzone_bouton_3 <= pos[0] < (xzone_bouton_3 + Lbouton_3)) and (yzone_bouton_3 <= pos[1] < (yzone_bouton_3 + Hbouton_3)):
                            choix = False
                            choix3 = True
                            choix3_depart = 1
                            
            while choix1 :
                if choix1_depart == 1:         
                    ecran.blit(background_de, (0, 0))
                    ecran.blit(bouton_retour, (xyzone_bouton_retour))
                    choix1_depart = 0     
                    
                ecran.blit(bouton_retour, (xyzone_bouton_retour))
                ecran.blit(bouton_home, (xyzone_bouton_home))    
                ecran.blit(bouton_lancer, (xyzone_bouton_lancer))                    
                pg.display.flip()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        pos = event.pos
                        
                        if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                            choix1 = False
                            choix = True

                        if (xzone_bouton_home <= pos[0] < (xzone_bouton_home + Lbouton_home)) and (yzone_bouton_home <= pos[1] < (yzone_bouton_home + Hbouton_home)):
                            return()
                            
                        if (xzone_bouton_lancer <= pos[0] < (xzone_bouton_lancer + Lbouton_lancer)) and (yzone_bouton_lancer <= pos[1] < (yzone_bouton_lancer + Hbouton_lancer)):
                                taille = 25
                                m = 538                    
                                m2 = 360                
                                l = 468                 
                                t = 301               
                                r = 608                
                                b = 419                      
                                tour = 20                   
                                fond = (236,185,185)          
                                couleur_cercle = (0,127,127)           
                                 
                                d = pg.display.set_mode((1080, 800))
                                
                                 
                                for i in range(tour):            
                                    n=random.randint(1,6)                   
                                    d.fill(fond)                          
                                    if n % 2 == 1:
                                        pg.draw.circle(d,couleur_cercle,(m,m2),taille)  
                                    if n==2 or n==3 or n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l,b),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r,t),taille)  
                                    if n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l,t),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r,b),taille)  
                                    if n==6:
                                        pg.draw.circle(d,couleur_cercle,(m,b),taille)  
                                        pg.draw.circle(d,couleur_cercle,(m,t),taille)  
                                 
                                    pg.display.flip()
                                    time.sleep(0.2)
            
            while choix2 :
                if choix2_depart == 1:         
                    ecran.blit(background_de, (0, 0))
                    ecran.blit(bouton_retour, (xyzone_bouton_retour))
                    choix2_depart = 0     
                    
                ecran.blit(bouton_retour, (xyzone_bouton_retour))
                ecran.blit(bouton_home, (xyzone_bouton_home))    
                ecran.blit(bouton_lancer, (xyzone_bouton_lancer))                    
                pg.display.flip()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        pos = event.pos
                        
                        if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                            choix2 = False
                            choix = True
                        
                        if (xzone_bouton_home <= pos[0] < (xzone_bouton_home + Lbouton_home)) and (yzone_bouton_home <= pos[1] < (yzone_bouton_home + Hbouton_home)):
                            return()

                        if (xzone_bouton_lancer <= pos[0] < (xzone_bouton_lancer + Lbouton_lancer)) and (yzone_bouton_lancer <= pos[1] < (yzone_bouton_lancer + Hbouton_lancer)):
                                taille = 25
                                m = 257                    
                                m2 = 360                
                                l = 187                 
                                t = 301                
                                r = 327                
                                b = 419

                                m_1 = 797                    
                                m2_1 = 360                
                                l_1 = 727                 
                                t_1 = 301                
                                r_1 = 867                
                                b_1 = 419                      
                                
                                tour = 17                   
                                fond = (236,185,185)          
                                couleur_cercle = (0,127,127)           
                                 
                                d = pg.display.set_mode((1080, 800))
                                
                                 
                                for i in range(tour):            
                                    n=random.randint(1,6)                   
                                    d.fill(fond)                          
                                    if n % 2 == 1:
                                        pg.draw.circle(d,couleur_cercle,(m,m2),taille)  
                                    if n==2 or n==3 or n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l,b),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r,t),taille)  
                                    if n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l,t),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r,b),taille)  
                                    if n==6:
                                        pg.draw.circle(d,couleur_cercle,(m,b),taille)  
                                        pg.draw.circle(d,couleur_cercle,(m,t),taille)  
                                    n=random.randint(1,6)                                           
                                    if n % 2 == 1:
                                        pg.draw.circle(d,couleur_cercle,(m_1,m2_1),taille)  
                                    if n==2 or n==3 or n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l_1,b_1),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r_1,t_1),taille)  
                                    if n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l_1,t_1),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r_1,b_1),taille)  
                                    if n==6:
                                        pg.draw.circle(d,couleur_cercle,(m_1,b_1),taille)  
                                        pg.draw.circle(d,couleur_cercle,(m_1,t_1),taille)

                                    pg.display.flip()
                                    time.sleep(0.2) 

            while choix3 :
                if choix3_depart == 1:         
                    ecran.blit(background_de, (0, 0))
                    ecran.blit(bouton_retour, (xyzone_bouton_retour))
                    choix3_depart = 0     
                    
                ecran.blit(bouton_retour, (xyzone_bouton_retour))
                ecran.blit(bouton_home, (xyzone_bouton_home))    
                ecran.blit(bouton_lancer, (xyzone_bouton_lancer))                    
                pg.display.flip()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        quit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        pos = event.pos
                        
                        if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                            choix3 = False
                            choix = True

                        if (xzone_bouton_home <= pos[0] < (xzone_bouton_home + Lbouton_home)) and (yzone_bouton_home <= pos[1] < (yzone_bouton_home + Hbouton_home)):
                            return()
                            
                        if (xzone_bouton_lancer <= pos[0] < (xzone_bouton_lancer + Lbouton_lancer)) and (yzone_bouton_lancer <= pos[1] < (yzone_bouton_lancer + Hbouton_lancer)):
                                taille = 25
                                m = 197                    
                                m2 = 360                
                                l = 127                 
                                t = 301                
                                r = 267                
                                b = 419

                                m_1 = 857                    
                                m2_1 = 360                
                                l_1 = 787                 
                                t_1 = 301                
                                r_1 = 927                
                                b_1 = 419

                                m_2 = 538                    
                                m2_2 = 360                
                                l_2 = 468                 
                                t_2 = 301                
                                r_2 = 608                
                                b_2 = 419                      
                                
                                tour = 17                   
                                fond = (236,185,185)          
                                couleur_cercle = (0,127,127)           
                                 
                                d = pg.display.set_mode((1080, 800))
                                
                                 
                                for i in range(tour):            
                                    
                                    n=random.randint(1,6)                   
                                    d.fill(fond)                          
                                    if n % 2 == 1:
                                        pg.draw.circle(d,couleur_cercle,(m,m2),taille)  
                                    if n==2 or n==3 or n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l,b),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r,t),taille)  
                                    if n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l,t),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r,b),taille)  
                                    if n==6:
                                        pg.draw.circle(d,couleur_cercle,(m,b),taille)  
                                        pg.draw.circle(d,couleur_cercle,(m,t),taille)  
                                    
                                    n=random.randint(1,6)                                           
                                    if n % 2 == 1:
                                        pg.draw.circle(d,couleur_cercle,(m_1,m2_1),taille)  
                                    if n==2 or n==3 or n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l_1,b_1),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r_1,t_1),taille)  
                                    if n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l_1,t_1),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r_1,b_1),taille)  
                                    if n==6:
                                        pg.draw.circle(d,couleur_cercle,(m_1,b_1),taille)  
                                        pg.draw.circle(d,couleur_cercle,(m_1,t_1),taille)
                                    
                                    n=random.randint(1,6)                                           
                                    if n % 2 == 1:
                                        pg.draw.circle(d,couleur_cercle,(m_2,m2_2),taille)  
                                    if n==2 or n==3 or n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l_2,b_2),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r_2,t_2),taille)  
                                    if n==4 or n==5 or n==6:
                                        pg.draw.circle(d,couleur_cercle,(l_2,t_2),taille)  
                                        pg.draw.circle(d,couleur_cercle,(r_2,b_2),taille)  
                                    if n==6:
                                        pg.draw.circle(d,couleur_cercle,(m_2,b_2),taille)  
                                        pg.draw.circle(d,couleur_cercle,(m_2,t_2),taille)

                                    pg.display.flip()
                                    time.sleep(0.2)                              