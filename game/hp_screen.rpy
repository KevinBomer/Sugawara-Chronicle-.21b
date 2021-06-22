################################################################################
#Stats screens creates a character stats bar and places it on the game. 
################################################################################

default hiroya_hp = 50
default hiroya_hp_max = 50
default eileen_hp = 100
default eileen_hp_max = 100

default player_lv = 1
default eileen_lv = 99

# This screen displays a single stat.
screen stats(name, hp, hp_max, lv, xalign, yalign):

    frame:
        xalign xalign
        yalign yalign
        vbox:
            spacing 5

            hbox:
                text "[name!t]" min_width 220
                #text _(" Lv. [lv]")

            hbox:
                text _("HP: "):
                    min_width 40
                    yalign 0.5

                bar:
                    value AnimatedValue(hp, hp_max, 1.0)
                    xmaximum 180
                    ysize 26


                #text " [hp]/[hp_max]":
                    yalign 0.5


# This screen uses "stats" to display two stats at once.
screen everyones_stats():
    use stats(_("Hiroya"), hiroya_hp, hiroya_hp_max, player_lv, 0.11, .7)
    #use stats(_("Eileen"), eileen_hp, eileen_hp_max, eileen_lv, 1.0)
