label interstitial:
    scene white with Dissolve(.2)
    stop music fadeout 1.0
    scene chapter_screen_1 with Dissolve(.2)
    show logo with Dissolve(.5):
        xalign .5
        yalign .6
        xpos .3
        ypos .5
        zoom .8
    $ renpy.pause(2, hard=True)
    scene bridge sidewalk night with dissolve
    "Darkness makes for good cover. It's easier for me to wander without having to watch my back all the time, in case anyone happens to be watching."
    "Following my usual route, which is starting to feel familar, I make it back to my bridge."
    "???""Who's there?!"
    "I stop in my tracks. There's two guys standing on the opposite sidewalk. Lurking near my spot..."
    "...Cops?"
    "No, No, I recognize those uniforms."
    "These guys are from Sakuranoki."
    "Great. Some thugs from our rival school are here to give me a hard time."
    "I can't make out much. Theres two of them. One is sort of tall. The other, sort of round."
    "The round one takes a step and shouts something in my directiion."
    "The round one" "Hey. He's talking to you!"
    "The other guy follows behind as they both approach, slowly, but with menace."
    "Damn that girl and her stupid rivalry. What has she dragged me into?"
    "The round one" "And whaddya' know. He's from Sugawara too."
    "The tall one" "Our lucky day."
    Hiroya "*sigh* I should have known. Where theres a bridge, there's bound to be trolls."
    "The tall one" "We heard there was some chump settin' up out here."
    "Hiroya" "I don't want any trouble."
    "The tall one" "Well the thing is, we're gonna' have a hard time believing that after that shit you guys just pulled."
    "The round one" "How dare you embarrass us in front of Shizuka!"
    "The round one" "Now she's gonna think we're idiots!"
    "Oh. That's what this is about."
    "What's-his-face and his stupid baseball challenge."
    "Damn both of them."
    "The tall one" "I'd reckon that the whole lot of you deserves some discipline. We can start now."
    Hiroya "Look, if you're here to mug me or whatever, I don't have any money."
    "The round one" "You know what happens to barn animals who step outta line?"
    "The tall one" "They brand 'em, and make an example of them for everyone else."
    Hiroya "Well, I'm glad the boys at Sakuranokoi are learning all about husbandry. Farming's a good vocation."
    "The round one" "...what?"
    "The tall one" "...I'm gettin' sick of seeing your dumb face!"
    "The round one" "Let's Teach 'im a lesson."
    "The taller of the two raises his fists to fight."
    "This isn't good, but I've got nowhere to run."
    "This bridge is my home now. I guess what comes next can't be helped."
    "I raise my fists defensively as the tall guy comes at me with a straight jab. He's slow and poorly balanced. I dodge his fist with ease."
    "I dive in low, aiming for his exposed gut."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "The tall one" "Oof!"
    "He keels forward, wincing and glares at me. I go for another hit while he's flinching."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "The round one" "Let's go!"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "Not to be left out, the round guy throws himself at me from the side, bowling me to the ground."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "I wrestle with him for a short moment. I almost get him in a hold, but he slips out and scuttles away."
    "I bounce back to my feet ready for more."
    "The tall one's still cradling his midsection, not yet recovered from my first hit."
    Hiroya "Oh, did that hurt? I'm sorry. Sommehow I thought one of Shizuka's knights would be able to take a hit. I'll try to go easier on you."
    "The tall one" "Tch. We were only gonna leave you with a few bruises, but now you've really done it!"
    "He reaches into his pocket and removes something."
    "A retractable knife, the kind used for cutting up cardboard boxes..."
    "...or enemies."
    "This is really bad."
    "Maybe I should cut my losses and run."
    "I try to step back a bit, But I feel something hard behind me."
    "The guardrail. And a forty-foot drop into the river below."
    "I could survive that most likely, though it wouldn't be pleasent."
    "The man with the knife takes a step closer."
    "The tall one" "Heheh. Now I got you."
    "The round one" "Squeal all you want! Nobody's comin' to save you."
    "I take a quick glance over the railing, down at the dark rushing water below."
    "It's pitch black. Could I swim to the riverbank in complete darkness?"
    Hiroya "...Huh?"
    "Just for an instant I thought I saw something. A flicker?"
    "No, it has to be a trick of the moonlight."
    "The guy with the knife takes another step forward."
    "The round one" "Hey! Look me in the eye when I'm killing you!"
    "I'm out of options. I prepare to jump. I turn around to the rail."
    "It's no trick of the moonlight."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.25
    "The guy with the knife grabs me by the collar."
    "The tall one" "Where'ddya think you're going?"
    "He turns me around, knife still in hand."
    Hiroya "Something's... There's something in the water."
    "The round one" "Maybe I'll throw you down there too if it's so interestin', huh?"
    Hiroya "No, really. Look. There's some kind of light."
    "The tall one" "Are you screwing with me, punk? You think I'm stupid or something?"
    #sfx
    "Behind me, a splash, as if something had been dropped in the river."
    "Or had come out of it."
    "A tidal wave of white light bursts behind me in an instant."
    "The tall one" "Dude! What the fuck is that?!"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1.25
            linear 0.1 zoom 1.0
    #sfx whoosh
    "Losing his grip on my shirt, the tall one staggers back."
    "The round one" "Shit get away from it!"
    "The tall one" "L-look!"
    "I turn in the direction of the light. But it isn't just light."
    "No, Theres something else to it. A fluidness, like a white mist, twisting and swirling, and coalessing at a single point, hovering at eye level over the water."
    Hiroya "What is that?"
    "The tall one" "It's an alien!"
    "The round one" "...You serious, dude? Let's just-"
    "It rushes forward like a wave, passing over my head and onto the bridge, between me and the two thugs."
    "It hovers there, a ball of white, with more mist swirling into it with each second."
    "Reacting, the Sakuranoki thugs raise their fists."
    "The tall one" "Alright. You grab it, I'll slit it's throat, whatever the hell it is!"
    "The round one" "Shit dude! I'm not touching that!"
    "The tall one" "Just hold it for a second!"
    "Reuluctantly, the round guy rushes forward, his arms reaching out for a bear hug."
    "He tries to grab at it, and misses. It moved out of his way."
    "The tall one" "Huh?"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    #sfx slash
    "In the same swift motion, it rushes behind him and knocks him to the ground."
    "The tall one" "Ah!"
    "He scrambles forward and back to his feet."
    "The round one" "What're you doing!? Just grab it!"
    "The bigger guy went forward again."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    #sfx slash
    "But he stops midpace, a similar look on his face as when I hit him in the gut."
    "He leans forward and takes a swing at the figure."
    "His hand passes right through yet again, but somehow slower this time. With more resistance."
    "It's as if the thing were somehow becoming denser. Taking shape."
    "A {i}human{/i} shape."
    "With a wide fluid movement, the figure circles behind the tall boy yet again. He braces for its attack."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    #sfx slash
    "The round one" "...Got it!"
    "The round boy locks his arms around the creature. The tall one takes the opportunity to strike."
    "The tall one" "DIE DIE DIE DIE DIEEE!"
    "He yells as he charges forward, slashing his knife frantically at the creature."
    "Then all at once, in an instant, I see her."
    "Her shape isn't quite clear, but it's clear enough."
    "She wears a wispy white gown with a light colored ribbon. Her pale hair white like the mist, and her eyes, filled with fear, surrounded by her attackers."
    "I have to stop this."
    Hiroya "Let her go."
    "Girl" "Spectre-"
    scene black with fade
    "A sharp sudden pressure stops me in my tracks."
    "The pain fills my entire body..."
    "It washes over me, taking over."
    "I didn't see her move."
    "She was already on me."
    "Her face is inches from mine. Her sword held with two hands in front of her, its blade buried hilt-deep inside my chest."
    Hiroya "W-What?"
    "Girl" "Divide."
    "And with the slightest nudge, she pushes me, sword and all, over the edge."
    "I can't catch myself. It's already too late."
    "I feel myself falling. I know I'm falling. And yet somehow, it doesn't seem real."
    "It feels...detached, somehow."
    "I feel the water around me too. Guess I didn't notice when I hit the surface."
    "That's weird."
    "Oh. I remember now. I got stabbed."
    "Damn."
    "So this is how I'm going to die..."
    scene black with fade
    $ renpy.pause(3, hard=True)
    show text "Sugawara Chronicle"
    $ renpy.pause(2, hard=True)
    #sfx splash
    #prolly open the next scene with him screaming idk
    return
