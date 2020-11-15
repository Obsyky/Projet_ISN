#Entete de classes.py
import random
import  pygame as pg
from pygame.locals import *
from constantes import *
pg.init()
    
    
#Mise en place de la fenetre
ecran = pg.display.set_mode(fen)
pg.display.set_caption(nomEcran_yahtzee)
    
    
myfont = pg.font.SysFont("time_new_roman.ttf", 32)
finalfont = pg.font.SysFont("time_new_roman.ttf", 100)
    
    
#Images***********************************************************************************************************************************

    #Paramètres Background accueil
background_acyams = pg.Surface(fen)
background_acyams.fill((109, 111, 115))

    #Paramètres Background Jouer
background_playyams = pg.Surface(fen)
background_playyams.fill((181, 180, 179))

    #Paramètres Background regles
background_rgyams = pg.image.load(image_bg_regles).convert_alpha()
background_rgyams = pg.transform.scale(background_rgyams, fen)



    #Bouton jouer 
bouton_jouer_yams = pg.image.load(image_jouer_yams).convert_alpha()
bouton_jouer_yams = pg.transform.scale(bouton_jouer_yams, (LHbouton_jouer_yams))

    #Bouton rejouer 
bouton_rejouer = pg.image.load(image_rejouer).convert_alpha()
bouton_rejouer = pg.transform.scale(bouton_rejouer, (LHrejouer))

    #Bouton règles
bouton_regles = pg.image.load(image_regles).convert_alpha()
bouton_regles = pg.transform.scale(bouton_regles, (LHbouton_regles))
    #Bouton retour 
bouton_retour = pg.image.load(image_retour).convert_alpha()
bouton_retour = pg.transform.scale(bouton_retour, (LHbouton_retour))

    #Titre 
titre_yams = pg.image.load(image_titre_yams).convert_alpha()
titre_yams = pg.transform.scale(titre_yams, (LHtitre_yams))

    #Ecran final
phrase_final_1 = pg.image.load(image_fin_1).convert_alpha()
phrase_final_1 = pg.transform.scale(phrase_final_1, (LHphrase_fn_1))

phrase_final_2 = pg.image.load(image_fin_2).convert_alpha()
phrase_final_2 = pg.transform.scale(phrase_final_2, (LHphrase_fn_2))

    #Grille
grille = pg.image.load(image_grille).convert_alpha()
grille = pg.transform.scale(grille, (LHgrille))

    #Bouton Lancer
blancer = pg.image.load(image_lancer).convert_alpha()
blancer = pg.transform.scale(blancer, (LHlancer))

    #Bouton Marquer
bmarquer = pg.image.load(image_marquer).convert_alpha()
bmarquer = pg.transform.scale(bmarquer, (LHmarquer))

    #Des
        #De 1
de_1 = pg.image.load(image_de1).convert_alpha()
de_1 = pg.transform.scale(de_1, (LHdes))

de_1_lock = pg.image.load(image_de1_lock).convert_alpha()
de_1_lock = pg.transform.scale(de_1_lock, (LHdes))

        #De 2
de_2 = pg.image.load(image_de2).convert_alpha()
de_2 = pg.transform.scale(de_2, (LHdes))

de_2_lock = pg.image.load(image_de2_lock).convert_alpha()
de_2_lock = pg.transform.scale(de_2_lock, (LHdes))

        #De 3
de_3 = pg.image.load(image_de3).convert_alpha()
de_3 = pg.transform.scale(de_3, (LHdes))

de_3_lock = pg.image.load(image_de3_lock).convert_alpha()
de_3_lock = pg.transform.scale(de_3_lock, (LHdes))

        #De 4
de_4 = pg.image.load(image_de4).convert_alpha()
de_4 = pg.transform.scale(de_4, (LHdes))

de_4_lock = pg.image.load(image_de4_lock).convert_alpha()
de_4_lock = pg.transform.scale(de_4_lock, (LHdes))

        #De 5
de_5 = pg.image.load(image_de5).convert_alpha()
de_5 = pg.transform.scale(de_5, (LHdes))

de_5_lock = pg.image.load(image_de5_lock).convert_alpha()
de_5_lock = pg.transform.scale(de_5_lock, (LHdes))

        #De 6
de_6 = pg.image.load(image_de6).convert_alpha()
de_6 = pg.transform.scale(de_6, (LHdes))

de_6_lock = pg.image.load(image_de6_lock).convert_alpha()
de_6_lock = pg.transform.scale(de_6_lock, (LHdes))

    #Case
case_score = pg.Surface(LHzone_tt)
case_score.fill((255,255,255))

case = pg.Surface(LHzone)
case.fill((255, 255, 255))

valide = pg.image.load(image_valide).convert_alpha()
valide = pg.transform.scale(valide, (LHvalide))

croix = pg.image.load(image_croix).convert_alpha()
croix = pg.transform.scale(croix, (LHcroix))
    
    
    
    
    
    
#Fonction au départ de l'accueil *********************************************************************************************************************
def yams(): 

#boucle infini *********************************************************************************************************************
    principal_yams =True
    accueil_yams = True
    Jouer_yams = False
    regles_yams = False
    while principal_yams :
        
#*****************   Boucle accueil   *******************************************************************************************************************************     
        while accueil_yams :
            ecran.blit(background_acyams,(0,0))
            ecran.blit(titre_yams, (xyzone_titre_yams))
            ecran.blit(bouton_jouer_yams, (xyzone_bouton_jouer_yams))
            ecran.blit(bouton_regles, (xyzone_bouton_regles))
            ecran.blit(bouton_retour,(xyzone_bouton_retour))
            pg.display.flip()
            
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    quit()
                
                if event.type == MOUSEBUTTONDOWN:
                    pos = event.pos
                    if (xzone_bouton_jouer_yams <= pos[0] < (xzone_bouton_jouer_yams + Lbouton_jouer_yams)) and (yzone_bouton_jouer_yams <= pos[1] < (yzone_bouton_jouer_yams + Hbouton_jouer_yams)):
                        accueil_yams = False
                        j=0
                        Jouer_yams = True
                        
                        
                    if (xzone_bouton_regles <= pos[0] < (xzone_bouton_regles + Lbouton_regles)) and (yzone_bouton_regles <= pos[1] < (yzone_bouton_regles + Hbouton_regles)):
                        accueil_yams = False
                        regles_yams = True
                        
                    if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                        return()
                    
                    
                            
                    
              
#*****************   Boucle jouer *********************************************************************************************************************************     
        while Jouer_yams : 
            if j==0:
                ecran.blit(background_playyams,(0,0))
                ecran.blit(grille, (xyzone_grille))
                ecran.blit(bouton_retour,(xyzone_bouton_retour))
                ecran.blit(blancer,(xyzone_lancer))
                
                de1 = 1
                de1_c = de_1
                ecran.blit(de1_c,(position1))
                
                de2 = 2
                de2_c = de_2
                ecran.blit(de2_c,(position2))
                
                de3 = 3
                de3_c = de_3
                ecran.blit(de_3,(position3))
    
                de4 = 4
                de4_c = de_4            
                ecran.blit(de_4,(position4))
                
                de5 = 5
                de5_c = de_5           
                ecran.blit(de_5,(position5))
                
                
                
                sz1 = 0
                sz1_display = myfont.render(str(sz1), 1, (0,0,0))
                sz1_c = sz1_display
                
                sz2 = 0
                sz2_display = myfont.render(str(sz2), 1, (0,0,0))
                sz2_c = sz2_display
                
                sz3 = 0
                sz3_display = myfont.render(str(sz3), 1, (0,0,0))
                sz3_c = sz3_display
                
                sz4 = 0
                sz4_display = myfont.render(str(sz4), 1, (0,0,0))
                sz4_c = sz4_display
                
                sz5 = 0
                sz5_display = myfont.render(str(sz5), 1, (0,0,0))
                sz5_c = sz5_display
                
                sz6 = 0
                sz6_display = myfont.render(str(sz6), 1, (0,0,0))
                sz6_c = sz6_display
                
                szbr = 0
                szbr_display = myfont.render(str(szbr), 1, (0,0,0))
                szbr_c = szbr_display
                
                szcr = 0
                szcr_display = myfont.render(str(szcr), 1, (0,0,0))
                szcr_c = szcr_display
                
                szps = 0
                szps_display = myfont.render(str(szps), 1, (0,0,0))
                szps_c = szps_display
                
                szgs = 0
                szgs_display = myfont.render(str(szgs), 1, (0,0,0))
                szgs_c = szgs_display
                
                szfl = 0
                szfl_display = myfont.render(str(szfl), 1, (0,0,0))
                szfl_c = szfl_display
                                      
                szyam = 0
                szyam_display = myfont.render(str(szyam), 1, (0,0,0))
                szyam_c = szyam_display
                                      
                szch = 0
                szch_display = myfont.render(str(szch), 1, (0,0,0))
                szch_c = szch_display
                
                
                pg.display.flip()
                
            
                j = j+1
                score = 0
                soustotal = 0
                nb_lancer = 0
                marquer = 0
                droit_marquer = 0
                droit_clicker = 0
                
                z1 = 0
                z2 = 0
                z3 = 0
                z4 = 0
                z5 = 0
                z6 = 0
                zbr = 0
                zcr = 0
                zps = 0
                zgs = 0
                zfl = 0
                zyam = 0
                zch = 0
                
                bonus = 0
                droit_bonus = 0
            
            
#Affichage Score    
            
            if z1 == 0 or z2 == 0 or z3 == 0 or z4 == 0 or z5 == 0 or z6 == 0 or zbr == 0 or zcr == 0 or zps == 0 or zgs == 0 or zfl == 0 or zyam == 0 or zch == 0  :        
                score_display = myfont.render(str(score), 1, (0,0,0))  
                soustotal_display = myfont.render(str(soustotal), 1, (0,0,0))
                bonus_display = myfont.render(str(bonus), 1, (0,0,0))
                
                ecran.blit(case_score, (xyzone_tt))
                ecran.blit(score_display, (xyzone_score))
                
                ecran.blit(case, (xyzone_st))
                ecran.blit(soustotal_display, (xyzone_soustotal))
                        
                ecran.blit(case, (xyzone_bs))
                ecran.blit(bonus_display, (xyzone_bonus))   
            
            
                if soustotal > 63 :
                    if droit_bonus == 0:
                        bonus = 35
                        droit_bonus = 1
                        score = score + bonus  
                    
                
                pg.display.flip()
                
                
                
                
        
                for event in pg.event.get():    
                    if event.type == QUIT:
                        pg.quit()
                        quit()
                        
                    if event.type == MOUSEBUTTONDOWN:
                        pos = event.pos
                        if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                            Jouer_yams = False
                            accueil_yams = True
                            
        
#*******************************************     Bouton Lancer    ******************************************************************************************
                            
                        if (xzone_lancer <= pos[0] < (xzone_lancer + Llancer)) and (yzone_lancer <= pos[1] < (yzone_lancer + Hlancer)):
                            if nb_lancer < 3 :
                                if de1 < 7 :
                                    de1 = random.randint(1,6)
                                    if de1 == 1:
                                        de1_c = de_1
                                    if de1 == 2:
                                        de1_c = de_2
                                    if de1 == 3:
                                        de1_c = de_3
                                    if de1 == 4:
                                        de1_c = de_4
                                    if de1 == 5:
                                        de1_c = de_5
                                    if de1 == 6:
                                        de1_c = de_6
                                    
                                if de2 < 7 :
                                    de2 = random.randint(1,6)
                                    if de2 == 1:
                                        de2_c = de_1
                                    if de2 == 2:
                                        de2_c = de_2
                                    if de2 == 3:
                                        de2_c = de_3
                                    if de2 == 4:
                                        de2_c = de_4
                                    if de2 == 5:
                                        de2_c = de_5
                                    if de2 == 6:
                                        de2_c = de_6
                                    
                                if de3 < 7 :
                                    de3 = random.randint(1,6)
                                    if de3 == 1:
                                        de3_c = de_1
                                    if de3 == 2:
                                        de3_c = de_2
                                    if de3 == 3:
                                        de3_c = de_3
                                    if de3 == 4:
                                        de3_c = de_4
                                    if de3 == 5:
                                        de3_c = de_5
                                    if de3 == 6:
                                        de3_c = de_6  
                                        
                                if de4 < 7 :
                                    de4 = random.randint(1,6)
                                    if de4 == 1:
                                        de4_c = de_1
                                    if de4 == 2:
                                        de4_c = de_2
                                    if de4 == 3:
                                        de4_c = de_3
                                    if de4 == 4:
                                        de4_c = de_4
                                    if de4 == 5:
                                        de4_c = de_5
                                    if de4 == 6:
                                        de4_c = de_6   
                                        
                                if de5 < 7 :
                                    de5 = random.randint(1,6)
                                    if de5 == 1:
                                        de5_c = de_1
                                    if de5 == 2:
                                        de5_c = de_2
                                    if de5 == 3:
                                        de5_c = de_3
                                    if de5 == 4:
                                        de5_c = de_4
                                    if de5 == 5:
                                        de5_c = de_5
                                    if de5 == 6:
                                        de5_c = de_6       
                                        
                                        
                                nb_lancer = nb_lancer + 1  
                                droit_marquer = 1
                                droit_clicker = 1
                                ecran.blit(de1_c,(position1))
                                ecran.blit(de2_c,(position2))
                                ecran.blit(de3_c,(position3))
                                ecran.blit(de4_c,(position4))
                                ecran.blit(de5_c,(position5))
                                ecran.blit(bmarquer,(xyzone_marquer))
                                pg.display.flip()
                            
#*******************************************     De 1    ******************************************************************************************                  
                        if (xp1 <= pos[0] < (xp1 + Ldes)) and (yp1 <= pos[1] < (yp1 + Hdes)):
                            if droit_clicker == 1 :
                                if nb_lancer > 0 :
                                    if de1 == 1:
                                        de1_c = de_1_lock
                                        de1 = de1 + 6
                                    else:
                                        if de1 == 2:
                                            de1_c = de_2_lock
                                            de1 = de1 + 6
                                        else :  
                                            if de1 == 3:
                                                de1_c = de_3_lock
                                                de1 = de1 + 6
                                            else:
                                                if de1 == 4:
                                                    de1_c = de_4_lock
                                                    de1 = de1 + 6
                                                else :
                                                    if de1 == 5:
                                                        de1_c = de_5_lock
                                                        de1 = de1 + 6
                                                    else:
                                                        if de1 == 6:
                                                            de1_c = de_6_lock
                                                            de1 = de1 + 6
                                                        else:
                                                            if de1 == 7 :
                                                                de1_c = de_1
                                                                de1 = de1 - 6
                                                            else:
                                                                if de1 == 8 :
                                                                    de1_c = de_2
                                                                    de1 = de1 - 6
                                                                else:
                                                                    if de1 == 9 :
                                                                        de1_c = de_3
                                                                        de1 = de1 - 6
                                                                    else:
                                                                        if de1 == 10 :
                                                                            de1_c = de_4
                                                                            de1 = de1 - 6
                                                                        else:
                                                                            if de1 == 11 :
                                                                                de1_c = de_5
                                                                                de1 = de1 - 6
                                                                            else:
                                                                                de1_c = de_6
                                                                                de1 = de1 - 6
                                ecran.blit(de1_c,(position1))
                                pg.display.flip()
                                
#*******************************************     De 2    ******************************************************************************************    
         
                        if (xp2 <= pos[0] < (xp2 + Ldes)) and (yp2 <= pos[1] < (yp2 + Hdes)):
                            if droit_clicker == 1 :
                                if nb_lancer > 0 :
                                    if de2 == 1:
                                        de2_c = de_1_lock
                                        de2 = de2 + 6
                                    else:
                                        if de2 == 2:
                                            de2_c = de_2_lock
                                            de2 = de2 + 6
                                        else :  
                                            if de2 == 3:
                                                de2_c = de_3_lock
                                                de2 = de2 + 6
                                            else:
                                                if de2 == 4:
                                                    de2_c = de_4_lock
                                                    de2 = de2 + 6
                                                else :
                                                    if de2 == 5:
                                                        de2_c = de_5_lock
                                                        de2 = de2 + 6
                                                    else:
                                                        if de2 == 6:
                                                            de2_c = de_6_lock
                                                            de2 = de2 + 6
                                                        else:
                                                            if de2 == 7 :
                                                                de2_c = de_1
                                                                de2 = de2 - 6
                                                            else:
                                                                if de2 == 8 :
                                                                    de2_c = de_2
                                                                    de2 = de2 - 6
                                                                else:
                                                                    if de2 == 9 :
                                                                        de2_c = de_3
                                                                        de2 = de2 - 6
                                                                    else:
                                                                        if de2 == 10 :
                                                                            de2_c = de_4
                                                                            de2 = de2 - 6
                                                                        else:
                                                                            if de2 == 11 :
                                                                                de2_c = de_5
                                                                                de2 = de2 - 6
                                                                            else:
                                                                                de2_c = de_6
                                                                                de2 = de2 - 6
                                ecran.blit(de2_c,(position2))
                                pg.display.flip()
                           
                
                         
#*******************************************     De 3    ******************************************************************************************    
         
                        if (xp3 <= pos[0] < (xp3 + Ldes)) and (yp3 <= pos[1] < (yp3 + Hdes)):
                            if droit_clicker == 1 :
                                if nb_lancer > 0 :
                                    if de3 == 1:
                                        de3_c = de_1_lock
                                        de3 = de3 + 6
                                    else:
                                        if de3 == 2:
                                            de3_c = de_2_lock
                                            de3 = de3 + 6
                                        else :  
                                            if de3 == 3:
                                                de3_c = de_3_lock
                                                de3 = de3 + 6
                                            else:
                                                if de3 == 4:
                                                    de3_c = de_4_lock
                                                    de3 = de3 + 6
                                                else :
                                                    if de3 == 5:
                                                        de3_c = de_5_lock
                                                        de3 = de3 + 6
                                                    else:
                                                        if de3 == 6:
                                                            de3_c = de_6_lock
                                                            de3 = de3 + 6
                                                        else:
                                                            if de3 == 7 :
                                                                de3_c = de_1
                                                                de3 = de3 - 6
                                                            else:
                                                                if de3 == 8 :
                                                                    de3_c = de_2
                                                                    de3 = de3 - 6
                                                                else:
                                                                    if de3 == 9 :
                                                                        de3_c = de_3
                                                                        de3 = de3 - 6
                                                                    else:
                                                                        if de3 == 10 :
                                                                            de3_c = de_4
                                                                            de3 = de3 - 6
                                                                        else:
                                                                            if de3 == 11 :
                                                                                de3_c = de_5
                                                                                de3 = de3 - 6
                                                                            else:
                                                                                de3_c = de_6
                                                                                de3 = de3 - 6
                                ecran.blit(de3_c,(position3))
                                pg.display.flip()
                           
                
                         
#*******************************************     De 4    ******************************************************************************************    
         
                        if (xp4 <= pos[0] < (xp4 + Ldes)) and (yp4 <= pos[1] < (yp4 + Hdes)):
                            if droit_clicker == 1 :
                                if nb_lancer > 0 :
                                    if de4 == 1:
                                        de4_c = de_1_lock
                                        de4 = de4 + 6
                                    else:
                                        if de4 == 2:
                                            de4_c = de_2_lock
                                            de4 = de4 + 6
                                        else :  
                                            if de4 == 3:
                                                de4_c = de_3_lock
                                                de4 = de4 + 6
                                            else:
                                                if de4 == 4:
                                                    de4_c = de_4_lock
                                                    de4 = de4 + 6
                                                else :
                                                    if de4 == 5:
                                                        de4_c = de_5_lock
                                                        de4 = de4 + 6
                                                    else:
                                                        if de4 == 6:
                                                            de4_c = de_6_lock
                                                            de4 = de4 + 6
                                                        else:
                                                            if de4 == 7 :
                                                                de4_c = de_1
                                                                de4 = de4 - 6
                                                            else:
                                                                if de4 == 8 :
                                                                    de4_c = de_2
                                                                    de4 = de4- 6
                                                                else:
                                                                    if de4 == 9 :
                                                                        de4_c = de_3
                                                                        de4 = de4 - 6
                                                                    else:
                                                                        if de4 == 10 :
                                                                            de4_c = de_4
                                                                            de4 = de4 - 6
                                                                        else:
                                                                            if de4 == 11 :
                                                                                de4_c = de_5
                                                                                de4 = de4 - 6
                                                                            else:
                                                                                de4_c = de_6
                                                                                de4 = de4 - 6
                                ecran.blit(de4_c,(position4))
                                pg.display.flip()
                               
                
                         
#*******************************************     De 5   ******************************************************************************************    
         
                        if (xp5 <= pos[0] < (xp5 + Ldes)) and (yp5 <= pos[1] < (yp5 + Hdes)):
                            if droit_clicker == 1 :
                                if nb_lancer > 0 :
                                    if de5 == 1:
                                        de5_c = de_1_lock
                                        de5 = de5 + 6
                                    else:
                                        if de5 == 2:
                                            de5_c = de_2_lock
                                            de5 = de5 + 6
                                        else :  
                                            if de5 == 3:
                                                de5_c = de_3_lock
                                                de5 = de5 + 6
                                            else:
                                                if de5 == 4:
                                                    de5_c = de_4_lock
                                                    de5 = de5 + 6
                                                else :
                                                    if de5 == 5:
                                                        de5_c = de_5_lock
                                                        de5 = de5 + 6
                                                    else:
                                                        if de5 == 6:
                                                            de5_c = de_6_lock
                                                            de5 = de5 + 6
                                                        else:
                                                            if de5 == 7 :
                                                                de5_c = de_1
                                                                de5 = de5 - 6
                                                            else:
                                                                if de5 == 8 :
                                                                    de5_c = de_2
                                                                    de5 = de5 - 6
                                                                else:
                                                                    if de5 == 9 :
                                                                        de5_c = de_3
                                                                        de5 = de5 - 6
                                                                    else:
                                                                        if de5 == 10 :
                                                                            de5_c = de_4
                                                                            de5 = de5 - 6
                                                                        else:
                                                                            if de5 == 11 :
                                                                                de5_c = de_5
                                                                                de5 = de5 - 6
                                                                            else:
                                                                                de5_c = de_6
                                                                                de5 = de5 - 6
                                ecran.blit(de5_c,(position5))
                                pg.display.flip()
                                
                                
                       
                                

#*******************************************     Marquer   ******************************************************************************************                       
                        if droit_marquer == 1 :        
                            if (xzone_marquer <= pos[0] < (xzone_marquer + Lmarquer)) and (yzone_marquer <= pos[1] < (yzone_marquer + Hmarquer)):
                                
                                droit_clicker = 0
                                ecran.blit(background_playyams,(0,0))
                                ecran.blit(grille, (xyzone_grille))
                                ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                ecran.blit(blancer,(xyzone_lancer))
                                ecran.blit(de1_c,(position1))
                                ecran.blit(de2_c,(position2))
                                ecran.blit(de3_c,(position3))
                                ecran.blit(de4_c,(position4))
                                ecran.blit(de5_c,(position5))
                                
                                if z1 == 0:
                                    ecran.blit(valide, (332,yzone_1))
                                else :
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    
                                if z2 == 0:
                                    ecran.blit(valide, (332,yzone_2))
                                else:                            
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    
                                if z3 == 0:
                                    ecran.blit(valide, (332,yzone_3))
                                else:                            
                                    ecran.blit(sz3_c, (xyzone_sz3))
                                    
                                if z4 == 0:
                                    ecran.blit(valide, (332,yzone_4))                            
                                else:                            
                                    ecran.blit(sz4_c, (xyzone_sz4))
                                    
                                if z5 == 0:
                                    ecran.blit(valide, (332,yzone_5))                     
                                else:                            
                                    ecran.blit(sz5_c, (xyzone_sz5))
                                    
                                if z6 == 0:
                                    ecran.blit(valide, (332,yzone_6))                     
                                else:                            
                                    ecran.blit(sz6_c, (xyzone_sz6))
                                    
                                if zbr == 0:
                                    ecran.blit(valide, (332,yzone_br))
                                else :
                                    ecran.blit(szbr_c, (xyzone_szbr))
                                    
                                if zcr == 0:
                                    ecran.blit(valide, (332,yzone_cr))  
                                else :
                                    ecran.blit(szcr_c, (xyzone_szcr))
                                                                
                                if zps == 0:                     
                                    ecran.blit(valide, (332,yzone_ps))   
                                else :
                                    ecran.blit(szps_c, (xyzone_szps))
                                                                 
                                if zgs == 0:                    
                                    ecran.blit(valide, (332,yzone_gs))
                                else :
                                    ecran.blit(szgs_c, (xyzone_szgs))
                                                                 
                                if zfl == 0:
                                    ecran.blit(valide, (332,yzone_fl))
                                else :
                                    ecran.blit(szfl_c, (xyzone_szfl))
                                    
                                if zyam == 0:
                                    ecran.blit(valide, (332,yzone_yam))
                                else :
                                    ecran.blit(szyam_c, (xyzone_szyam))
                                    
                                if zch == 0:
                                    ecran.blit(valide, (332,yzone_ch))
                                else :
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                
                                
                                pg.display.flip()
                                
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                
                                marquer = 1
                                nb_lancer = 4
                                
                                if de1 > 6 :
                                    de1 = de1 - 6
                                if de2 > 6 :
                                    de2 = de2 - 6
                                if de3 > 6 :
                                    de3 = de3 - 6
                                if de4 > 6 :
                                    de4 = de4 - 6
                                if de5 > 6 :
                                    de5 = de5 - 6
                                
                                a = de1
                                if de2 > a:
                                    b = a
                                    a = de2
                                else :
                                    b = de2
                                
                                if de3 > a:
                                    c = b
                                    b = a
                                    a = de3
                                else:
                                    if de3 > b:
                                        c = b
                                        b = de3
                                    else:
                                        c = de3
                                        
                                if de4 > a:
                                    d = c
                                    c = b
                                    b = a
                                    a = de4
                                else:
                                    if de4 > b :
                                        d = c
                                        c = b
                                        b = de4
                                    else:
                                        if de4 >c :
                                            d = c
                                            c = de4
                                        else: 
                                            d = de4
                                
                                if de5 > a :
                                    e = d
                                    d = c
                                    c = b
                                    b = a
                                    a = de5
                                else:
                                    if de5 > b:
                                        e = d
                                        d = c
                                        c = b
                                        b = de5
                                    else:
                                        if de5 > c :
                                            e = d
                                            d = c
                                            c = de5
                                        else:
                                            if de5 > d :
                                                e = d
                                                d = de5
                                            else: 
                                                e = de5
                                            
                                            
                                            
#***********************************          Zone "1"      ******************************************************************************
                        if marquer == 1 :  
                            if (xzone_1 <= pos[0] < (xzone_1 + Lzone)) and (yzone_1 <= pos[1] < (yzone_1 + Hzone)):      
                                if z1 == 0 :
                                    if de1 == 1 :
                                        sz1 = sz1 + 1
                                    if de2 == 1 :
                                        sz1 = sz1 + 1
                                    if de3 == 1 :
                                        sz1 = sz1 + 1
                                    if de4 == 1 :
                                        sz1 = sz1 + 1
                                    if de5 == 1 :
                                        sz1 = sz1 + 1
                                                                
                                        
                                        
                                    z1 = 1
                                    nb_lancer = 0
                                    score = score + sz1
                                    soustotal = soustotal + sz1
                                    droit_marquer = 0
                                    marquer = 0
                                
                                    
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                                               
                                    sz1_display = myfont.render(str(sz1), 1, (0,0,0))
                                    
                                    if sz1 == 0:
                                        sz1_c = croix
                                    else:
                                        sz1_c = sz1_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()
                                    
                                    
        
                                
                                
                                
                                
                                
#***********************************          Zone "2"      ******************************************************************************                        
                            if (xzone_2 <= pos[0] < (xzone_2 + Lzone)) and (yzone_2 <= pos[1] < (yzone_2 + Hzone)):    
                                if z2 == 0 :
                                    if de1 == 2 :
                                        sz2 = sz2 + 2
                                    if de2 == 2 :
                                        sz2 = sz2 + 2
                                    if de3 == 2 :
                                        sz2 = sz2 + 2
                                    if de4 == 2 :
                                        sz2 = sz2 + 2
                                    if de5 == 2 :
                                        sz2 = sz2 + 2
                                        
                                        
                                        
                                    z2 = 1
                                    nb_lancer = 0
                                    score = score + sz2
                                    soustotal = soustotal +sz2
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    sz2_display = myfont.render(str(sz2), 1, (0,0,0))
                                    
                                    if sz2 == 0:
                                        sz2_c = croix
                                    else:
                                        sz2_c = sz2_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()
                                
                                
                                
                                
                                
#***********************************          Zone "3"      ******************************************************************************                       
                            if (xzone_3 <= pos[0] < (xzone_3 + Lzone)) and (yzone_3 <= pos[1] < (yzone_3 + Hzone)):  
                                if z3 == 0 :
                                    if de1 == 3 :
                                        sz3 = sz3 + 3
                                    if de2 == 3 :
                                        sz3 = sz3 + 3
                                    if de3 == 3 :
                                        sz3 = sz3 + 3
                                    if de4 == 3 :
                                        sz3 = sz3 + 3
                                    if de5 == 3 :
                                        sz3 = sz3 + 3
                                        
                                        
                                        
                                    z3 = 1
                                    nb_lancer = 0
                                    score = score + sz3
                                    soustotal = soustotal +sz3
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    sz3_display = myfont.render(str(sz3), 1, (0,0,0))
                                    
                                    if sz3 == 0:
                                        sz3_c = croix
                                    else:
                                        sz3_c = sz3_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()
                                
                                
                                
                                
                                
#***********************************          Zone "4"      ******************************************************************************                       
                            if (xzone_4 <= pos[0] < (xzone_4 + Lzone)) and (yzone_4 <= pos[1] < (yzone_4 + Hzone)):   
                                if z4 == 0 :
                                    if de1 == 4 :
                                        sz4 = sz4 + 4
                                    if de2 == 4 :
                                        sz4 = sz4 + 4
                                    if de3 == 4 :
                                        sz4 = sz4 + 4
                                    if de4 == 4 :
                                        sz4 = sz4 + 4
                                    if de5 == 4 :
                                        sz4 = sz4 + 4
                                        
                                        
                                        
                                    z4 = 1
                                    nb_lancer = 0
                                    score = score + sz4
                                    soustotal = soustotal + sz4
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    sz4_display = myfont.render(str(sz4), 1, (0,0,0))
                                    
                                    if sz4 == 0:
                                        sz4_c = croix
                                    else:
                                        sz4_c = sz4_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()      
                                
                                
                                
                                
                                
#***********************************          Zone "5"      ******************************************************************************                       
                            if (xzone_5 <= pos[0] < (xzone_5 + Lzone)) and (yzone_5 <= pos[1] < (yzone_5 + Hzone)):    
                                if z5 == 0 :
                                    if de1 == 5 :
                                        sz5 = sz5 + 5
                                    if de2 == 5 :
                                        sz5 = sz5 + 5
                                    if de3 == 5 :
                                        sz5 = sz5 + 5
                                    if de4 == 5 :
                                        sz5 = sz5 + 5
                                    if de5 == 5 :
                                        sz5 = sz5 + 5
                                        
                                        
                                        
                                    z5 = 1
                                    nb_lancer = 0
                                    score = score + sz5
                                    soustotal = soustotal + sz5
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    sz5_display = myfont.render(str(sz5), 1, (0,0,0))
                                    
                                    if sz5 == 0:
                                        sz5_c = croix
                                    else:
                                        sz5_c = sz5_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()      
                                
                                
                                
                                
                                
#***********************************          Zone "6"      ******************************************************************************                       
                            if (xzone_6 <= pos[0] < (xzone_6 + Lzone)) and (yzone_6 <= pos[1] < (yzone_6 + Hzone)):   
                                if z6 == 0 :
                                    if de1 == 6 :
                                        sz6 = sz6 + 6
                                    if de2 == 6 :
                                        sz6 = sz6 + 6
                                    if de3 == 6 :
                                        sz6 = sz6 + 6
                                    if de4 == 6 :
                                        sz6 = sz6 + 6
                                    if de5 == 6 :
                                        sz6 = sz6 + 6
                                        
                                        
                                        
                                    z6 = 1
                                    nb_lancer = 0
                                    score = score + sz6
                                    soustotal = soustotal + sz6
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    sz6_display = myfont.render(str(sz6), 1, (0,0,0))
                                    
                                    if sz6 == 0:
                                        sz6_c = croix
                                    else:
                                        sz6_c = sz6_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()    
                                
                                
                                
                                
                                
#***********************************          Zone "Brelan"      ******************************************************************************                       
                            if (xzone_br <= pos[0] < (xzone_br + Lzone)) and (yzone_br <= pos[1] < (yzone_br + Hzone)):    
                                if zbr == 0 :
                                    if a == b and b == c :
                                        szbr = 20
                                    else:
                                        if b == c and c == d :
                                            szbr = 20
                                        else :
                                            if c == d and d == e :
                                                szbr = 20
                                            else :
                                                szbr = 0
                                        
                                        
                                        
                                    zbr = 1
                                    nb_lancer = 0
                                    score = score + szbr
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szbr_display = myfont.render(str(szbr), 1, (0,0,0))
                                    
                                    if szbr == 0:
                                        szbr_c = croix
                                    else:
                                        szbr_c = szbr_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()            
                                
                                
                                
                                
                                
#***********************************          Zone "Carré  "      ******************************************************************************                       
                            if (xzone_cr <= pos[0] < (xzone_cr + Lzone)) and (yzone_cr <= pos[1] < (yzone_cr + Hzone)):    
                                if zcr == 0 :
                                    if a == b and b == c  and c == d:
                                        szcr = 40
                                    else:
                                        if b == c and c == d and d == e :
                                            szcr = 40
                                        else:
                                            szcr = 0
                                        
                                        
                                        
                                    zcr = 1
                                    nb_lancer = 0
                                    score = score + szcr
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szcr_display = myfont.render(str(szcr), 1, (0,0,0))
                                    
                                    if szcr == 0:
                                        szcr_c = croix
                                    else:
                                        szcr_c = szcr_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()             
                                
                                
                                
                                
                        
#***********************************          Zone "Petite suite"      ******************************************************************************                       
                            if (xzone_ps <= pos[0] < (xzone_ps + Lzone)) and (yzone_ps <= pos[1] < (yzone_ps + Hzone)):    
                                if zps == 0 :
                                    if ( a == b or b < a ) and b == c+1 and c == d+1 and d == e+1:
                                        szps = 25
                                    else : 
                                        if b == c and a == b+1 and b == d+1 and d == e+1:
                                            szps = 25
                                        else :
                                            if c == d and a == b+1 and b == c+1 and c == e+1:
                                                szps =25
                                            else:
                                                if (d == e or e < d) and a == b+1 and b == c+1 and c == d+1:
                                                    szps = 25
                                                else: 
                                                    szps = 0
                                         
                                        
                                        
                                    zps = 1
                                    nb_lancer = 0
                                    score = score + szps
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szps_display = myfont.render(str(szps), 1, (0,0,0))
                                    
                                    if szps == 0:
                                        szps_c = croix
                                    else:
                                        szps_c = szps_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()             
                                
                                
                                
                                
                                
#***********************************          Zone "Grande suite"      ******************************************************************************                       
                            if (xzone_gs <= pos[0] < (xzone_gs + Lzone)) and (yzone_gs <= pos[1] < (yzone_gs + Hzone)):    
                                if zgs == 0 :
                                    if a == b+1 and b == c+1 and c == d+1 and d == e+1:
                                        szgs = 35
                                    else:
                                        szgs = 0
                                         
                                        
                                        
                                    zgs = 1
                                    nb_lancer = 0
                                    score = score + szgs
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szgs_display = myfont.render(str(szgs), 1, (0,0,0))
                                    
                                    if szgs == 0:
                                        szgs_c = croix
                                    else:
                                        szgs_c = szgs_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()             
                                
                                
                                
                                
                                
#***********************************          Zone "Full"      ******************************************************************************                       
                            if (xzone_fl <= pos[0] < (xzone_fl + Lzone)) and (yzone_fl <= pos[1] < (yzone_fl + Hzone)):    
                                if zfl == 0 :
                                    if a == b and d == e:
                                        if c == d:
                                            szfl = 30
                                        else :
                                            if b == c :
                                                szfl = 30
                                            else :
                                                szfl = 0
                                        
                                        
                                    zfl = 1
                                    nb_lancer = 0
                                    score = score + szfl
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szfl_display = myfont.render(str(szfl), 1, (0,0,0))
                                    
                                    if szfl == 0:
                                        szfl_c = croix
                                    else:
                                        szfl_c = szfl_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()             
                                
                                
                                
                                

 #***********************************          Zone "Yam"      ******************************************************************************                       
                            if (xzone_yam <= pos[0] < (xzone_yam + Lzone)) and (yzone_yam <= pos[1] < (yzone_yam + Hzone)):    
                                if zyam == 0 :
                                    if a == b and b == c and c == d and d == e:
                                        szyam = 50
                                    else:
                                        szyam = 0
                                        
                                        
                                    zyam = 1
                                    nb_lancer = 0
                                    score = score + szyam
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szyam_display = myfont.render(str(szyam), 1, (0,0,0))
                                    
                                    if szyam == 0:
                                        szyam_c = croix
                                    else:
                                        szyam_c = szyam_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()             
                                
                                
                                
                                

#***********************************          Zone "Chance"      ******************************************************************************                       
                            if (xzone_ch <= pos[0] < (xzone_ch + Lzone)) and (yzone_ch <= pos[1] < (yzone_ch + Hzone)):    
                                if zch == 0 :
                                    szch = a + b + c + d + e
                                        
                                        
                                    zch = 1
                                    nb_lancer = 0
                                    score = score + szch
                                    droit_marquer = 0
                                    marquer = 0
                                    
                                    ecran.blit(background_playyams,(0,0))
                                    ecran.blit(grille, (xyzone_grille))
                                    ecran.blit(bouton_retour,(xyzone_bouton_retour))
                                    ecran.blit(blancer,(xyzone_lancer))
                                    ecran.blit(de1_c,(position1))
                                    ecran.blit(de2_c,(position2))
                                    ecran.blit(de3_c,(position3))
                                    ecran.blit(de4_c,(position4))
                                    ecran.blit(de5_c,(position5))
                                    
                                    szch_display = myfont.render(str(szch), 1, (0,0,0))
                                    
                                    szch_c = szch_display
                                    
                                    ecran.blit(case, (xyzone_1))
                                    ecran.blit(case, (xyzone_2))
                                    ecran.blit(case, (xyzone_3))                            
                                    ecran.blit(case, (xyzone_4))                          
                                    ecran.blit(case, (xyzone_5))                        
                                    ecran.blit(case, (xyzone_6))                      
                                    ecran.blit(case, (xyzone_br))                   
                                    ecran.blit(case, (xyzone_cr))                
                                    ecran.blit(case, (xyzone_ps))              
                                    ecran.blit(case, (xyzone_gs))              
                                    ecran.blit(case, (xyzone_fl))            
                                    ecran.blit(case, (xyzone_yam))         
                                    ecran.blit(case, (xyzone_ch))
                                    
                                    ecran.blit(sz1_c, (xyzone_sz1))
                                    ecran.blit(sz2_c, (xyzone_sz2))
                                    ecran.blit(sz3_c, (xyzone_sz3))                            
                                    ecran.blit(sz4_c, (xyzone_sz4))                          
                                    ecran.blit(sz5_c, (xyzone_sz5))                        
                                    ecran.blit(sz6_c, (xyzone_sz6))                                                   
                                    ecran.blit(szbr_c, (xyzone_szbr))                                               
                                    ecran.blit(szcr_c, (xyzone_szcr))                                              
                                    ecran.blit(szps_c, (xyzone_szps))                                           
                                    ecran.blit(szgs_c, (xyzone_szgs))                                          
                                    ecran.blit(szfl_c, (xyzone_szfl))                                        
                                    ecran.blit(szyam_c, (xyzone_szyam))                                    
                                    ecran.blit(szch_c, (xyzone_szch))
                                    
                                    pg.display.flip()       
                                
                                
                                
#*******************************************     Fin partie   ******************************************************************************************        
                            
            if z1 == 1 and z2 == 1 and z3 == 1 and z4 == 1 and z5 == 1 and z6 == 1 and zbr == 1 and zcr == 1 and zps == 1 and zgs == 1 and zfl == 1 and zyam == 1 and zch == 1  :                     
                ecran.blit(background_playyams,(0,0))                                    
                ecran.blit(bouton_retour,(xyzone_bouton_retour))                
                ecran.blit(bouton_rejouer, (xyzone_rejouer))
                                   
                ecran.blit(phrase_final_1,(105,220))
                ecran.blit(phrase_final_2,(635,220))
                
                score_display = finalfont.render(str(score), 1, (0,0,0))  
                ecran.blit(score_display, (525, 247))
    
                
                pg.display.flip() 
                
                
                
                for event in pg.event.get():    
                    if event.type == QUIT:
                        pg.quit()
                        quit()
                        
                    if event.type == MOUSEBUTTONDOWN:
                        pos = event.pos
                        if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                            Jouer_yams = False
                            accueil_yams = True
                            
                        if (xzone_rejouer <= pos[0] < (xzone_rejouer + Lrejouer)) and (yzone_rejouer <= pos[1] < (yzone_rejouer + Hrejouer)):
                            j = 0
                            
                               
                            
                           
            
                     
                         
#*****************   Boucle regles    *************************************************************************************************************************             
        while regles_yams :                
            ecran.blit(background_rgyams,(0,0))
            ecran.blit(bouton_retour,(xyzone_bouton_retour))
            pg.display.flip()
            
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    quit()
                    
                if event.type == MOUSEBUTTONDOWN:
                    pos = event.pos
                    if (xzone_bouton_retour <= pos[0] < (xzone_bouton_retour + Lbouton_retour)) and (yzone_bouton_retour <= pos[1] < (yzone_bouton_retour + Hbouton_retour)):
                        regles_yams = False
                        accueil_yams = True     
      
        

#Arret du jeu      *****************************************************************************************************************************
    pg.quit()
    quit()