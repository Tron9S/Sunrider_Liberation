image h_shower1:
    "Censored/shower1.jpg"
    subpixel True
image h_shower2:
    "Censored/shower2.jpg"
    subpixel True
image h_shower3:
    "Censored/shower3.jpg"
    subpixel True
image h_shower4:
    "Censored/shower4.jpg"
    subpixel True
image h_shower5:
    "Censored/shower5.jpg"
    subpixel True

image h_chigarah:
    "Censored/chigarah.jpg"
    subpixel True

image h_chigarah2:
    "Censored/chigarah2.jpg"
    subpixel True
image h_chigarah3:
    "Censored/chigarah3.jpg"
    subpixel True

image h_chigaramindstream:
    "Censored/chigaramindstream.jpg"

#REturn    
image asagah1:
    "REturn_censored/asaga_h1.jpg"
    subpixel True
image asagah2:
    "REturn_censored/asaga_h2.jpg"
    subpixel True
image asagah2b:
    "REturn_censored/asaga_h2b.jpg"
    subpixel True
image asagah3:
    "REturn_censored/asaga_h3.jpg"
    subpixel True
image asagah4:
    "REturn_censored/asaga_h4.jpg"
    subpixel True
image avah1:
    "REturn_censored/ava_h1.jpg"
    subpixel True
image avah2:
    "REturn_censored/ava_h2.jpg"
    subpixel True
image avah3:
    "REturn_censored/ava_h3.jpg"
    subpixel True
image avah3b:
    "REturn_censored/ava_h3b.jpg"
    subpixel True
image avah4:
    "REturn_censored/ava_h4.jpg"
    subpixel True
image avah5:
    "REturn_censored/ava_h5.jpg"
    subpixel True
image avah5b:
    "REturn_censored/ava_h5b.jpg"
    subpixel True
image avah5c:
    "REturn_censored/ava_h5c.jpg"
    subpixel True
image avah1_patch:
    "REturn_censored/ava_h1_patch.jpg"
    subpixel True
image avah2_patch:
    "REturn_censored/ava_h2_patch.jpg"
    subpixel True
image avah3_patch:
    "REturn_censored/ava_h3_patch.jpg"
    subpixel True
image avah3b_patch:
    "REturn_censored/ava_h3b_patch.jpg"
    subpixel True
image avah4_patch:
    "REturn_censored/ava_h4_patch.jpg"
    subpixel True
image avah5_patch:
    "REturn_censored/ava_h5_patch.jpg"
    subpixel True
image avah5b_patch:
    "REturn_censored/ava_h5b_patch.jpg"
    subpixel True
image avah5c_patch:
    "REturn_censored/ava_h5c_patch.jpg"
    subpixel True
image claudeh1:
    "REturn_censored/claude_h1.jpg"
    subpixel True
image claudeh2:
    "REturn_censored/claude_h2.jpg"
    subpixel True
image claudeh3:
    "REturn_censored/claude_h3.jpg"
    subpixel True    
image icarih1:
    "REturn_censored/icari_h1.jpg"
    subpixel True
image icarih2:
    "REturn_censored/icari_h2.jpg"
    subpixel True    
image icarih3:
    "REturn_censored/icari_h3.jpg"
    subpixel True
image icarih4:
    "REturn_censored/icari_h4.jpg"
    subpixel True
image icarih5:
    "REturn_censored/icari_h5.jpg"
    subpixel True
image icarih6:
    "REturn_censored/icari_h6.jpg"
    subpixel True
image solah1:
    "REturn_censored/sola_h1.jpg"
    subpixel True
image solah2:
    "REturn_censored/sola_h2.jpg"
    subpixel True
image solah3:
    "REturn_censored/sola_h3.jpg"
    subpixel True
image solah4:
    "REturn_censored/sola_h4.jpg"
    subpixel True
image solah5:
    "REturn_censored/sola_h5.jpg"
    subpixel True
image solah6:
    "REturn_censored/sola_h6.jpg"
    subpixel True    
image solah7:
    "REturn_censored/sola_h7.jpg"
    subpixel True    
    
init 10:
    $ CENSOR = False
    $ CENSOR_ver = 3
    
    $gallery.button("chcg7")
    $gallery.unlock_image("h_shower1")
    $gallery.transform(tr_center)
    $gallery.unlock_image("h_shower2")
    $gallery.transform(tr_center)
    $gallery.unlock_image("h_shower3")
    $gallery.transform(tr_center)
    $gallery.unlock_image("h_shower4")
    $gallery.transform(tr_center)
    $gallery.unlock_image("h_shower5")
    $gallery.transform(tr_center)

    $gallery.button("chcg20")
    $gallery.unlock_image("h_chigarah")

    $gallery.button("chcg22")
    $gallery.unlock_image("h_chigarah2")
    $gallery.unlock_image("h_chigarah3")

    $gallery.button("chcg41")
    $gallery.unlock_image("asagah1")
    $gallery.unlock_image("asagah2")
    $gallery.unlock_image("asagah2b")
    $gallery.unlock_image("asagah3")
    $gallery.unlock_image("asagah4")

    $gallery.button("chcg42")
    $gallery.unlock_image("avah1")
    $gallery.unlock_image("avah2")
    $gallery.unlock_image("avah3")
    $gallery.unlock_image("avah3b")
    $gallery.unlock_image("avah4")
    $gallery.unlock_image("avah5")   
    $gallery.unlock_image("avah5b")   
    $gallery.unlock_image("avah5c")   

    $gallery.button("chcg43")
    $gallery.unlock_image("claudeh1")
    $gallery.unlock_image("claudeh2")
    $gallery.unlock_image("claudeh3")

    $gallery.button("chcg44")
    $gallery.unlock_image("icarih1")
    $gallery.unlock_image("icarih2")
    $gallery.unlock_image("icarih3")
    $gallery.unlock_image("icarih4")
    $gallery.unlock_image("icarih5")
    $gallery.unlock_image("icarih6")
    
    $gallery.button("chcg45")
    $gallery.unlock_image("solah1")
    $gallery.unlock_image("solah2")
    $gallery.unlock_image("solah3")
    $gallery.unlock_image("solah4")
    $gallery.unlock_image("solah5")
    $gallery.unlock_image("solah6")
    $gallery.unlock_image("solah7")

label censored_asagahscene:

    play music "Music/Colors_Loop.ogg" fadeout 1.5
    scene asagah1 with dissolve
    
    "Shields pulled Asaga from the bunk and wrapped her legs around his waist as the two of them floated through the room."
    asa "Oo-oaah!!"
    asa "D-doing it for the first time like this... Uwaah, the capt'n's sure bold..."
    kay "Put your arms around behind my neck."
    "He pulled his pants down and raised Asaga up by her plump ass."
    kay "Try to relax yourself... It's gonna be a pretty tight fit..."
    asa "R-roger!"
    "Asaga looked on nervously as the two of them slowly initiated docking procedures."
    "Thanks to her body's overabundant production of lubricant, it seemed as if Asaga's first time would be relatively painless."
    kay "All right, here goes..."
    "He slowly slid her in, her entrance stretching to accommodate his girth."
    asa "U-ugnn..."
    kay "Does it hurt too bad?"
    asa "N-nah... Feels fine..."
    asa "P-pretty... good actually..."
    "His fingers dug into her ample ass and slowly rocked Asaga against his rod."
    asa "M-mgn..."
    asa "Haa... It's... happenin'... Capt'n's dick's inside...!"
    asa "Make me feel real good, 'kay?"
    "Accepting her invitation, he gave her rear a good slap and speared her virgin flesh as deeply as he could reach."
    asa "E-eah!"
    
    scene asagah2 with dissolve
    
    "He stripped off her clothes in a rush. Her twin tails floated about as the two slowly revolved in midair."
    "Asaga's fluid soaked his loins and dripped off, floating in strings around them."
    asa "U-ugn... A-ah...!"
    "He pounded Asaga against him, her entryway slapping against his pelvis. Asaga's fingers dug into his neck as her pussy muscles untensed, sending forth another tidal wave of juice."
    asa "Hiyahh... T-this is totally different... from fapping... M-mou!"
    asa "I-it's totally fillin' me up!"
    asa "The capt'n's Vanguard rod!"
    "Shields punished Asaga's mouth with another firm slap to the ass."
    asa "H-hugu!"
    kay "That's enough outta you..."
    asa "B-but I can't help it...! H-huu!!"
    asa "F-feels so good... m-might pee myself..."
    kay "That's not my fetish."
    asa "Ah mou!"
    "Shields rammed Asaga in, extending her passage, and raised her chin. They locked mouths and madly tried to swallow each other's tongues."
    "Asaga's scent flooded his senses, making Shields feel light headed. He felt pressure surge south."
    kay "(Shit... T-this is actually too good!)"
    kay "(If Asaga doesn't let go... I'm gonna blow too early...!)"
    "Asaga's taste filled his head with warmth, and traveled down his neck, and gathered at the base of his cannon rod, now prepped for imminent action."
    "Her modest but still laudable boobs squeezed against his chest with each pound, her hard little tits tickling him."
    "Their mouths finally separated, temporarily downgrading code red to code orange."
    asa "Haa... haa..."
    asa "G-gugh... A-at this rate..."
    asa "Huu..."
    "Her body flushed red as her thighs quivered."
    asa "H-haa..."
    "Asaga gasped and held Shields close as she unexpectedly came."
    asa "G-gah... Haa..."
    "Despite the aggressive impatience bulging through his veins, Shields held his forces back. This was merely the prelude."
    "Battles were decided by whoever lost their cool first and committed too early. Shields was not about to make such a rookie mistake."
    kay "Can you keep going?"
    asa "M-mou... Do you even have to ask that? Ain't it obvious?"
    asa "T-that was just a 'lil accident anyways... There's still a big one lurking inside... Can feel it..."
    kay "Well then, better go in deep and smoke it out."
    "He rammed her in as deep as he could reach, her ass overflowing between his fingers."
    "He reached for one of her twintails and buried his face in it."
    asa "Eh? Whaddya doin'!?"
    kay "Sorry! But this twin tail man must get his fix!"
    asa "Eh-!? EEHH!? Y-ya mean that's your fetish!? What the hell man!?"
    kay "Twin tails banzai!"
    asa "U-ugh... I... can't look at you any more captain..."
    "Shields delivered another slap to her ass."
    asa "U-ugu!"
    kay "What, then what did you think was your charm point?"
    asa "U-uhh... eehh... M-my... green eyes?"
    kay "... ... ..."
    kay "(I'm sorry Asaga, but I'm pretty sure nobody else in the galaxy even noticed that...)"
    asa "A-ah! What's that face for! A-ah!"
    kay "(Seeing how you're still able to talk... How 'bout this!?)"
    "Shields quickened his pace, slapping himself against her upper thighs."
    asa "Haa... haa..."
    "Asaga's face melted away into a mess of horny ecstasy."
    kay "Repeat after me."
    kay "Twin tails banzai!"
    asa "T-twin tails... BANZAI!!!"
    kay "Twin tails banzai!!"
    asa "Twin tails BANZAI!!!"
    "At this point, Asaga was too messed up to even realize what she was saying."
    asa "H-huu... Ahh...!"
    asa "I... I feel... U-uggnn...!"
    asa "Ah shit! Ah shit! A shit a shit!"
    asa "I..."
    "Power mounted in Shields' cannon. All systems were primed to fire!"

    scene asagah2b with dissolve

    "At that moment, Asaga's eyes lit with bright azure light."
    asa "G-GACKK....!!!!!!"
    "Asaga wrapped herself around Shields so tight he thought he was going to be crushed."
    kay "(Shit! G-guess I'm coming inside!)"
    asa "A-AHH... A-AHH...!!"
    kay "(T-too late!)"
    
    scene white with dissolve
    scene asagah3 with dissolve
    
    "With a final heave, he pushed as deep as he could go, squeezing into her narrow channel."
    "His weapon shot forth, loading Asaga's hole with more cream than it could hold."
    "Great globs of cum spurted from her pussy, and floated in white orbs through the air."
    asa "A-aAHH!!! G-GuGNN...!"
    kay "(S-she's still...!?)"
    "Suddenly, Asaga bit into his shoulder."
    kay "E-eeck!"
    asa "Haa... Haa...."
    "The blue fire faded from her eyes."
    
    scene asagah4 with dissolve
    
    asa "Haa...."
    asa "Aahh... Mou..."
    "Asaga's ass was soaked with her spray and perspiration. Cum, juice, and drops of sweat floated through the room."
    "Her thighs trembled and her asshole twitched with pleasure."
    kay "(This girl... overdid it.)"
    asa "That's... the first time... I actually awakened from cumming... T-thought I was gonna die from pleasure..."
    asa "H-huu... I-I can still..."
    asa "H-hgnn..."
    "Asaga cringed as she came again, just from Shields removing himself."
    "Cum poured out of her entrance and floated away."
    "They were now levitating upside down, their feet against the ceiling, orbs of their body fluids circling them. Truly a surreal scene, to be sure."
    asa "Haa... haaa..."
    asa "Aah... J-just... let me stay like this for a while..."
    asa "Dunno... if that's the end..."
    asa "H-huu.. Ah... Mou.. What if it never stops?"
    kay "Wouldn't that be nice..."
    asa "Aaah!! That's hardly a plus!!"
    asa "I'll hafta fly the Black Jack with muh cum face! Nobody's ever gonna take me seriously again!"
    kay "Crap... Quite a mess down there..."
    "Asaga's hole was caked with an ugly batter of cum, juice, and blood. And that was only the beginning of the huge mess the two found themselves floating through."
    kay "Uhh... I better turn the cleaner drone on before restoring gravity. Or else cum's gonna splatter everywhere."
    "Shields opened a storage locker and withdrew the drone. It buzzed around, dutifully cleaning up their mess."
    asa "Eeeh... You weren't gonna force me to fly around and eat it all up?"
    kay "That's disgusting. Where the hell would you get an idea like that?"
    asa "Huu. Don't deny it. You know where..."
    return
    
label censor_avahscene:

    play music "Music/Colors_sad.ogg" fadeout 1.5
    
    if legion_destroyed == True:
        scene avah1_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah1 with dissolvemedium
    
    "Ava wrapped her arms around Shields and brought him down to the floor. Shields raised her head with his arms and locked their mouths together, their tongues tasting each other."
    "His heart pounded, pumping blood between his legs. The more he tasted his childhood friend, the more pleasure surged, daring him to go even further."
    "He unbuttoned her pristine uniform, revealing a pair of truly presidential prizes. He worked his way down, kissing Ava's neck, collarbones, before finally arriving at his destination."
    
    if legion_destroyed == True:
        scene avah2_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah2 with dissolvemedium
    
    "Pushing her bra up, her plentiful bounty spilled forth, a pair of glorious breasts which Shields had longed to see since that day. He wrapped his lips around her tit and suckled on it, drawing out all manner of unspeakable noises."
    ava "U-ugn... Haa..."
    "Her nipple dutifully stood at attention as Shields circled his tongue around it and suctioned it out."
    "With his hand, he reached into her skirt and rubbed her through her panties."
    ava "Ah... Mou... You're... really going all the way..."
    "Her entry hole was so soaked that when he reached in, his finger accidentally slipped inside."
    kay "Doesn't look like you'd want me to stop at this point."
    ava "I can't help it... Even I have urges, you know..."
    kay "Eeh..."
    ava "Idiot... Don't act so surprised. Everyone needs a release every now and then..."
    "With her permission acquired, he eagerly pulled off her tights and soaked his finger in her juices. Peeling the roof of Ava's clit back, he gave her joy button a few presses."
    ava "H-gnn... U-gn..."
    "Hardly able to contain the pleasure, Ava softly moaned on the floor, her thighs tensed."
    "Her clit puffed up like dough, emerging from its hiding spot."
    kay "Damn... Had no idea it could get so big..."
    ava "Why do you have to say stupid things like that...?"
    kay "W-well, I'm just sayin'!"
    ava "Unbelievable... You better stick it in before your stupidity turns me off..."
    kay "Oy..."
    ava "Hurry! Mou!"
    "Ava impatiently kicked her legs."
    kay "All right, all right..."
    "He peeled off Ava's panties while pulling down his trousers."
    ava "Ah... It's..."
    "He soaked his shaft in Ava's juices and ran it against her puffed up clit, once again spilling soft moans from Ava's lips."
    kay "(This woman... She acts all high and mighty, but in reality she's just as much of a horny animal as I am.)"
    "He grabbed her ass, the thought of wrecking his straight laced XO pumping a bulging torrent of excitement through his veins."
    "After thoroughly stimulating her clit, he aligned himself with her gate, and slowly guided himself in."
    ava "U-gnn..."
    kay "Dang... Still tight..."
    
    if legion_destroyed == True:
        scene avah3_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah3 with dissolvemedium
    
    "With more difficulty than he expected, he managed to fit himself completely in."
    ava "Haa..."
    "He gave her ass a good pat and pumped himself into her."
    ava "Uugn..."
    "Shields could hardly contain his wonder. He was inside of her! After all these months of giving him nothing but the cold shoulder, he had finally cracked into the ice queen!"
    ava "Ah, what's with that stupid face? I'm not sure if I'll be able to take you seriously from now on..."
    kay "Shaddup..."
    "He gave her ample ass a good slap and pounded himself into her as punishment."
    ava "U-ugn... A-agh... Ugn..."
    "He reached down and gave her clit another press."

    if legion_destroyed == True:
        scene avah4_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah4 with dissolvemedium

    ava "U-gugn...! Y-you're..."
    ava "C-calm down...!"
    kay "Not this time, Ava..."
    kay "You're not pres any more. Can't boss me around."
    ava "A-ah mou!"
    "He intensified his firepower, splitting her legs apart and assaulting the very end of Ava's passageway with his battering ram."
    
    if legion_destroyed == True:
        scene avah3b_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah3b with dissolvemedium
    
    ava "U-guh... A-ahh! K-Kayto... N-not too much...!"
    "Ava's cries only added more fuel to the fire."
    "Her massive tits swayed with each thrust, her tits bouncing up and down like a ship on rough seas."
    "Poseidon going to wreck the USS Crescentia tonight. All hands aboard may truly be lost."
    "He wrapped both his hands around her chest mounds and molded them like dough. Breast spilled forth between his fingers."
    kay "(So much breast!)"
    ava "W-what are you doing...! A-ah mou...! Y-you gonna make me... M-gmm...!"
    "He gave her teats a good squeeze, making Ava squeeze her eyes shut."
    ava "U-ugn... N-no...! D-don't look... U-gn...."
    kay "Sorry. But Kayto Shields never closes his eyes!"
    ava "I-idiot...! Haa... U-ugn..."
    ava "T-tainting... a proud officer... l-like this... I can't... b-believe...!"
    ava "A-ah... A-ah...!! N-noo!!! I-idiot...!!"
    "Her thighs tensed and her interior stretched out like a balloon as Ava came."
    ava "Haaaaa.......!!!"
    ava "U-ugn....!!"
    "Drool dripped down her mouth as her entire body lost control. She could only lay prone on the floor, asshole twitching, as Shields pounded even harder into her hole."
    ava "U-gn... A-ah...!"
    kay "Sorry Ava... But looks like you only want it harder..."
    ava "U-ugnn...! I-idiot...! A-aahh...!"
    "He intertwined his fingers with Ava and pulled her arms apart, spreading her helplessly against the floor."
    "Ava's face twisted as Shields pounded every shred of composure from her body. She screamed in joy as sweat and juices dripped down her ass."
    kay "(What a slut face she has right now... Can't believe she's been hiding this all this time...)"
    ava "A-ah! Mou! Why're you looking at me like that!?"
    kay "I never knew you had such a wild side..."
    ava "Then don't look at me! Idiot!"
    kay "Sorry, but I like it!"
    "He bent forward and pressed their lips together. Now they were docked in two places at once."
    "Their tongues lapped against each other, sending power surging to Shields' cannon."
    kay "(Shit... This is a little too good!!)"
    "Ava wrapped her legs around his waist, only encouraging him to pound deeper. His gun rod extend beyond maximum capacity, ramming against the very end of Ava's passage."
    kay "U-ugh... Ava..."
    "He opened his mouth, their lips connected. Warm, slippery drool dripped down their mouths as they tied their tongues into knots."
    "Ava's taste and scent overpowered his senses. A tidal wave of juices poured from Ava's insides, drenching them until he had no idea where he ended and where Ava began."
    kay "(Ah...! Shit...! She's...)"
    ava "Haa... haa... Hit me harder...! U-ugn... Everything you've got!"
    "Ava's horny voice sent Shields past the point of no return. His gun rod was primed and ready to fire."
    kay "(Ugn... G-gotta... hold...!)"
    "He grabbed her shoulders and pressed her down, ramming himself as deep as possible."
    ava "U-uggn...!!"
    "Ava exploded into ecstasy for the second time, her eyes shut tight, her lips agape."
    kay "Argh...!"
    "Any further and he was going to blow!"
    "Cum began to ooze out as Shields held back the blast for as long as he could muster."
    kay "(T-too late...!)"
    "The crack in the floodgates was all it took. With one final push, he impaled Ava with his rod, and unleashed."
    
    scene white with dissolve
    if legion_destroyed == True:
        scene avah5_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah5 with dissolvemedium
    
    ava "H-uggnnnh...!!!"
    "Shields' head went white as a blast of white cream erupted into Ava's baby hole, filling her with batter."
    "She overflowed with his cum, sending it dripping it onto the floor."
    "He pounded the rear of her passageway, ejecting a spurt of cum each time."
    ava "Haaa....! Haa...!"
    "Each burst caused white cream to drip from her pussy, down her ass."
    "Finally they both collapsed on top of each other, their chests heaving."
    
    scene white with dissolve
    if legion_destroyed == True:
        scene avah5c_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah5c with dissolvemedium
    
    ava "Haa... haa..."
    ava "So much came out... You filled me up..."
    ava "Idiot."
    "She rested her arm on top of his back."
    kay "Really takes me back... Doing this. Reminds me of that night..."
    kay "Except this time, we're not going to split apart."
    kay "No matter what happens... We'll always be together."
    ava "Idiot. What are you saying..."
    ava "As soon as the timeline resolves itself, we'll just go back to normal. Please do not get too far ahead of yourself."
    kay "Ava..."
    
    scene white with dissolve
    if legion_destroyed == True:
        scene avah5b_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah5b with dissolvemedium
    
    ava "I mean it! This was just a special case. A little... bonus. That's all."
    ava "I expect you to disregard this event and to handle your responsibilities as ship captain dutifully once the timeline is fixed."
    kay "Sigh... I guess it's always like this with you..."
    kay "All right, all right... You are right, in that the Sunrider will always be my ship."
    kay "But I'm not going to forget about you. You're... more than just my XO. You've always been more."
    kay "You're... my partner, Ava. Together as one, we'll fly through the stars... Just like we promised..."
    ava "Heh..."
    "With that, Ava flicked him on the forehead."
    if legion_destroyed == True:
        scene avah5c_patch with dissolvemedium
    if legion_destroyed == False:
        scene avah5c with dissolvemedium
    ava "Idiot."
    
    scene white with dissolvemedium
    return
    
label censor_icarihscene:
    
    scene icarih1 with dissolve
    
    ica "A-ah..."
    "Icari's entryway was engorged like warm dough. Flesh as pink as her lips lined her gateway, and met at the very top, hiding a small diamond of a clit."
    "Shields ran his fingers along the lips of her opening, wetting it in juices."
    kay "Looks plenty wet to me..."
    ica "T-that's just sweat..."
    "He fit his index finger into her clit's hiding spot and coaxed it out."
    ica "H-hygn...!"
    ica "W-what are you doing...?"
    ica "I-I never said you could touch...!"
    "Her clit slowly ballooned into a fleshy jewel as he rubbed it."
    ica "H-hgn.... A-ah..."
    "Juices oozed from her opening and stringed down below her."
    kay "Heh. See? You're soaking wet..."
    ica "L-like y-you can talk!"
    ica "If you get any harder, your dick's gonna tear straight through your trousers!"
    ica "Ah, stupid!"
    ica "W-what are you doing, making me all hot out here... T-this is all your fault... Stupid unreliable captain..."
    "Icari bent down against a rock and flared her ass to Shields."
    ica "Hurry up... and fix me... C-come on...!"
    "She wiggled her butt in impatience."
    ica "Hurry! B-before someone sees us..."
    "Shields pulled his pants down, his hot rod springing upwards, and grabbed Icari by the hips."
    ica "Y-you better not mess this up... O-or else I'll never forgive you...!"
    kay "Oy... Have some faith in your captain!"
    
    scene icarih2 with dissolve
    
    "Shields got into position behind Icari and jammed himself in."
    kay "(S-shit...! S-she's... so tight...!)"
    ica "Mmygnn...!"
    "Icari accepted Shields into her flesh. The sensation of slippery warmth enveloped him as their bodies became one."
    kay "(So this is the inside of Icari...)"
    "He pulled himself further out, and jammed in once more, Icari's insides molded around him."
    "Her tunnel hugged him from all angles as he pushed himself against her. Juices poured out from the deep end of her passageway, soaking Shields' pelvis with her warmth."
    
    scene icarih3 with dissolve
    
    ica "Haa... Aah..."
    "He had never noticed before how impressive her ass was. He grabbed handfuls with both palms, her bounty overflowing between his fingers. Her asshole flinched with each of his thrusts as pleasure shot up her spine."
    ica "A-ahh...! H-hgn...!"
    
    scene icarih4 with dissolve
    
    ica "I-it's n-not like i-it feels good or anything!! Stupid!! J-jamming your cock into me like this...!!"
    ica "A-ah...! I-I won't forgive this, captain!! M-making me feel like this...! M-mou...!"
    "Shields gave her ass a slap."
    ica "H-huck!"
    "Her pussy twitched."
    kay "Do you like that?"
    
    scene icarih3 with dissolve
    
    ica "S-stupid...! As if I would ever--"
    "He gave her another slap."
    
    scene icarih4 with dissolve
    
    ica "I-iyaah...!"
    "Juice leaked from her opening and dripped down."
    
    scene icarih3 with dissolve
    
    ica "A-ah... A-ah... S-stop it... O-or else I'm gonna..."
    "Icari gyrated her ass, his dick sliding in and out of her."
    kay "(She says stop and yet she's the one moving on her own...)"
    kay "It feels good, doesn't it?"
    ica "S-stupid...! A-as if I w-would ever... cum from your stupid dick...!"
    ica "Heh... heh... Y-you're gonna have to do better i-if you're really gonna...!"
    "Shields slapped her ass a third time, making it thoroughly jiggle."
    ica "H-hiiiee...!!"
    "Liquid poured out of her opening, soaking both of them in fluids."
    kay "D-did you just...?"
    
    scene icarih4 with dissolve
    
    ica "S-shadup!! Shadupshadupshadup!!!"
    ica "A-ah mou!"
    kay "(Looks like our fearless mercenary is quite the masochist...)"
    
    scene icarih3 with dissolve
    
    ica "H-hick...!"
    "Shields grabbed her hips and pounded himself in, clapping against her rear."
    ica "Ah! Ah! Ah! Ah!..."
    "Her insides constricted, so tight that he nearly popped out."
    kay "(So... hot...!)"
    "He felt pressure build up as he approached his burst point."
    "With another firm slap to her ass, Icari finally gave out."
    ica "H-ha... A-ah....!! N-n-n-n-nooo!!!"
    "Her asshole clenched as a tidal wave of fluid poured from her pussy."
    
    scene icarih4 with dissolve
    
    ica "Hiyaahh....!!!"
    ica "Haaa... haaa....!!"
    "He clenched her ass in his hands and intensified his thrusts as waves of blind pleasure shot through his body."
    "Icari's eyes clenched shut and she covered her face in shame as a waterfall of fluid poured from her opening, dripping down into the pool of sea water below them."
    kay "(Shit... I can't take this much longer...!)"
    "He felt his dick elongate as it primed itself for immediate action."
    "Entering the final stages of his launch sequence, he jammed himself as deep as he could push, the head of his rod banging against the roof of Icari's passageway."
    ica "H-hyuggn...!"
    kay "Icari...!!"
    ica "A-ah... C-captain...!!"
    
    scene white with dissolve
    scene icarih5 with dissolve
    
    "He blew everything he had into her, puffing her pussy with cream."
    ica "A-aahhHHH!!"
    "Icari's ass clenched once more as a second orgasm reverberated through her body."
    "He pounded every drop of cum he had deep into her passageway, gasping for air."
    "Sweat was now dripping down her butt despite the cool evening air. Her asshole was still convulsing, soaked with cum and juices."
    "Finally, he finished unloading into her and pulled himself out."
    "Cream spurted out of her hole, and stringed down below."
    
    scene icarih6 with dissolve
    
    ica "Haa... haa..."
    ica "W-well...?"
    ica "W-was it... a-all right...?"
    "Icari looked at him timidly all of a sudden."
    kay "All right? It was great! Truly world class."
    ica "Y-you don't think I'm weird or anything?"
    kay "Nah, it was pretty damned hot!"
    ica "H-huu..."
    "Big tears welled up in Icari's eyes."
    kay "O-oy... w-what's the matter!?"
    ica "'Cause... I was worried... y-you wouldn't like it...!!!"
    kay "N-not like it!? W-why the hell wouldn't I!?"
    ica "Waahhh!!!"
    kay "O-oy, Icari! P-pull yourself together!!!"
    "Shields hugged Icari as she cried into his chest."
    "... ... ..."
    "... ..."
    "..."
    ica "Sniffle..."
    
    return

label censor_solahscene:
    
    scene solah1 with dissolve
    
    "Sola gasped when he hoisted her up by the butt and carried her onto the bed, wrapped around him."
    sol "E-ah..."
    "He put her on top of him and began to unwrap her."
    sol "H-ha..."
    sol "S-such e-embarrassment..."
    
    scene solah2 with dissolve
    
    "Sola trembled and shyly wrapped her arms around her breasts as Shields pulled off her clothes, exposing her underwear."
    kay "Did you change your mind? It's all right to stop..."
    sol "N-no!"
    sol "I-I did not mean... A-ah, do what y-you wish of me!"
    kay "Sola... There's no reason to be ashamed..."
    "Shields unclipped her bra. Sola whimpered as her bare boobs spilled out into her arms."
    kay "After all, you look great. Best body I could ask for! Hah! Wonderful boobs, wonderful ass!"
    "Shields laughed to himself, mostly for Sola's sake."
    sol "S-saying such unspeakable things... Truly, I shall walk out of this room forever shamed..."
    sol "Ah! Do as you will! Mark me with your taint so that I may forever become yours!"
    kay "(S-she's... making fun of me... isn't she?)"
    kay "(Yep, she's definitely making fun of me now...)"
    "He marveled her perfect architecture, running his palms against her sleek back, and coming to a rest on her Imperial-tier ass."
    "He pulled down his trousers."
    sol "A-ah... T-that big thing... i-is supposed to go inside me...?"
    "Sola's eyes widened with equal parts disbelief and fear."
    sol "W-well...? S-shall w-we b-begin...?"
    "Sola tried her best to force a smile, but it was clear she was nearly chattering her teeth in terror."
    kay "All right... As long as we do it slowly, it shouldn't hurt too much..."
    sol "F-fear not... I am used to pain... Surely this will be a simple matter next to the other trials I have endured..."
    sol "A-a-a... s-s-simple matter! Y-yes... A cake run, a turkey shoot... a-a...."
    "Shields patted her ass up, and slipped off her panties. Nothing but Sola sat before him."
    sol "H-ha..."
    
    scene solah3 with dissolve
    
    "He spread her entrance open with his fingers and slowly guided her in. He stared in wonder as he slowly vanished inside of her."
    sol "Hhhyggnn........!!"
    "The pressure around him was incredible as he jammed himself in. Every nook and cranny of Sola hugged him, threatening to drown him in her warmth."
    "Finally, Sola accepted the entire length of Shields' scepter."
    sol "Haa..."
    
    scene solah4 with dissolve
    
    sol "I-it is not too bad... P-perhaps my body is accustomed to physical stress..."
    "Sola's eyes shut and her lips parted as Shields grabbed her hips and slowly raised her up."
    sol "A-ah...!"
    "Her insides melded around him as she slowly eased herself back and forth, his rod attached to her ass like a thick fleshy cord."
    "She gasped, her mouth agape, as she rode on top of him."
    sol "Aa-h...."
    sol "T-this sensation... is indescribable..."
    sol "T-the captain's warmth is... filling up... my whole body..."
    kay "Sola..."
    "Unable to hold back, Shields grabbed Sola by the ass and ran her against him, slamming against the roof of her passageway with each thrust."
    sol "A-ah! A-ah!! A-ah!"
    sol "C-captain...! A-ah...!"
    "Her magnificent behind melded around his fingers. There was so much of it that he didn't even know where to begin."
    "Everywhere his hands went, there was ass. More ass than he could ever have asked for."
    "Her small asshole flared with each pound, now soaking wet with juices. Staring at it cocked his gun barrel, putting it into ready position."
    sol "A-ah! C-captain! A-ah... D-defiling t-the Sharr... A-ah!!"
    sol "A-ah...! I am... t-tainted...! S-such s-shame...!"
    "But her words only made more juices flow down from the roof of her vagina, soaking Shields in sloppy warmth."
    "Her insides churned and tensed, popping Shields out."
    sol "A-ah...! Haa... haa..."
    "Sola panted, gasping for air. She turned and faced him with an enormously slutty expression, begging him to put it back in."
    sol "Haa..."
    "Shields rubbed his dick against her entryway but did not put it in yet, deciding to tease Sola a bit."
    sol "H-huu..."
    sol "C-captain...!"
    kay "Are you enjoying it?"
    sol "F-foul man... M-making the Sharr of Ryuvia speak such shameful words... and do such shameful deeds..."
    sol "Now come! D-do not... falter at this hour..."
    "Shields reached up and soaked his hands in Sola's cream."
    "He ran his fingers across the lips of her south entrance, and came to rest at when the lips met to form her clit."
    "Sola shivered as he coaxed her activation button open and gave it a few presses."
    sol "H-haa..."
    sol "H-hurry...."
    sol "R-resume... O-or else..."
    kay "What do you want me to do, Sola?"
    sol "A-ah! T-troublesome man..."
    sol "I..."
    sol "I..."
    sol "I desire your... penis... in my vagina! D-do it now!"
    "With the magic words spoken, Shields slipped himself back into her. Her passageway was now soaked with lubrication and more relaxed than before. Sola's face melted with pleasure as she dug into him, her ass bouncing with each thrust."
    sol "A-ah! A-ah!"
    "Shields rhythmically tensed his hips as Sola did her work, jamming himself so deep that he felt as if they would meld into one and never again separate."
    sol "A-ah... A-ahh...! I-I can f-feel it... T-the captain's..."
    sol "Haa... Haa..."
    "Her walls constricted, as if intent to crush his dick. But that only intensified Shields' pleasure."
    "With all his strength, he forced her walls open with each thrust, impaling Sola with his sword, as far as he could hit."
    "Sweat dripped down her back as her buttocks clapped against him. Shields felt pressure mount in his rod, elongating it to its maximum safe setting."
    "The walls of Sola's pussy suddenly loosened all at once, and she collapsed forwards."
    sol "H-haaa....!!!!"
    "Sola covered her face in shame as she climaxed. But her attempts at modesty at futile, as her cute little asshole clenched and flared with each wave of pleasure that shot through her body."
    "Her eyes rolled into her skull and drool dripped down the corner of her lips as Shields pounded himself in harder as she was still coming."
    sol "AH!! A-AH!! HAA...!!!"
    "He pounded her until her slender body was near breaking point."
    "Seeing the taciturn Sola devolved into the very image of lewdness brought Shields past the point of no return."
    kay "(This is it...!)"
    "He felt all of his life energy drain from his body and focus at his center. His cannon rod extended to maximum length and primed itself for immediate action."
    
    scene white with dissolve
    
    kay "SOLA!!!"
    
    scene solah5 with dissolve
    
    "He gasped as he erupted into her, instantly filling her opening with his white life fluid."
    "Great flashes of agonizing pleasure burned into his mind, overloading any other sense."
    "His hips thrusted into her and slammed against the rear of her passageway as he shot forth again. His cum spurted from her opening and dripped down onto him."
    "He emptied every last drop of his essence deep into her, his thoughts flooded with horny aggression."
    "Finally, he shot his last. His body relaxed and his arms flopped to the bed. The two of them panted in exhaustion, sweat dripping down their bodies."
    
    scene solah6 with dissolve
    
    sol "Haa... haa..."
    sol "Ah..."
    "Sola poked at the waves of cum dripping down her opening in disbelief."
    sol "T-the captain's..."
    sol "Haaa...."
    "She finally collapsed onto the bed."
    sol "The virgin winter snow has been tainted with the red smear of my blood... Ah... S-such disgrace..."
    sol "Now... my only option as the Sharr is to either live out the rest of my life as your wife... or disembowel myself immediately."
    kay "S-Sola...!?"
    sol "Ah, I cannot force myself upon you like this! I shall take the well-treaded path of sorrow and cut my belly open upon this very bed!"
    kay "Wait, wait! Y-you don't have to do that!! N-nobody believes that stuff anymore!!!"
    
    scene solah7 with dissolve
    
    sol "Heh..." 
    sol "Heheh... Hahaha...!"
    kay "S-Sola?"
    sol "Captain, did you truly believe the ancient Ryuvians believed in such foolhardy traditions?"
    kay "W-well... Y-you're always so... into your Ryuvian rules... that I thought..."
    sol "The Ryuvian Empire was one based on reason and science. Our rules, while appearing backwards to outsiders, were all made for a reason."
    sol "And we would not be so foolish as to require girls to disembowel themselves upon losing their virginity outside of marriage..."
    kay "A-ah! R-right! H-hah! You had me scared there for a moment!"
    kay "Hah! Hah! Hah!"
    sol "Captain..."
    sol "Regardless... Please take your promise seriously..."
    sol "I know not what grim trials await... but know that they will test you to the utmost of your abilities..."
    sol "Please... be ready... when the time comes... So that... we will not be separated..."
    kay "Yeah! Of course, Sola! I promise!"
    return
    
label censor_claudehscene:
    
    play music "Music/Colors_Chigara.ogg" fadeout 1.5
    scene claudeh1 with dissolve
    
    "With a snap of Claude's fingers, the scenery morphed into Shields' cabin. She clambered on top of him on all fours, and put her god-tier ass to his face."
    cla "Impress your goddess! Then she shall consider letting you go!"
    kay "(Once again, it looks like I've fallen for one of her tricks... Although this time, I have mostly myself to blame for that...)"
    kay "... ... ..."
    kay "(Oh well.)"
    kay "(I did promise to do anything. Besides, I need Claude's help to get us out of this spectacular mess!)"
    "Claude put his hard rod between her massive boobs and commenced sliding it in and out of her mouth."
    "Despite the surreal situation, he felt comfortable, as if he was floating on a pile of feathers."
    kay "(Is this a part of Claude's powers too...?)"
    "He reached up and split apart Claude's entryway. Juices were already dripping from her hole, stringing down and swaying as she moved her head."
    "He soaked his finger in her warm fluids and rubbed the fleshy hood on top of her entryway."
    cla "O-oah... T-that's my..."
    cla "Teehee... Attacking me there... You naughty captain..."
    kay "If we're doing this, I'm not going down without a fight!"
    "Claude's clit gorged with energy as he gave it a vigorous rub over."
    cla "Eah~ Captain~"
    "He felt warmth slop down his rod as Claude went down deeper."
    "She went back up and sucked his mushroom top like candy, overloading his head with sensations."
    "By now, he had completely chucked his concerns for the space time continuum out the proverbial window. He had far more pressing concerns, such as Claude's massive ass hovering centimeters from his face."
    "He grabbed her ass by the hips and pushed her pussy into his mouth. He wrapped his lips around her clit and shoved his tongue up into its protective cover."
    cla "H-HIIYYAAAHH!!"
    "Claude's thighs involuntarily twitched. She spat his dick out and gasped for air."
    cla "N-gnn..."
    cla "M-mou! Making your goddess come already...!"
    kay "I had no idea that would work so well!"
    kay "Heh..."
    cla "Hmph! You're thinking that Claude is an easy girl, aren't you!? You are, aren't you!?"
    cla "Mou, I'm not helping you anymore! You'll just have to figure out how to fix the universe by yourself!"
    kay "Oh really?"
    "He resumed his attack, peeling back her clit's cover with his tongue and sucking it like a lollipop."
    cla "H-heeee...!"
    "Hearing Claude's cries only fueled his desire to hear her scream harder. He wanted to suck her until she broke."
    cla "Mm... Ahh...! Mou... captain..."
    "Claude wrapped her tits around him and tickled his shaft with her chest."
    cla "This is Claude's... special move!"
    "She pressed her tits together and went down on Shields again. He felt pressure rush down his body as her boobs rubbed against the base of his shaft while her warm mouth attacked the top."
    "Claude ran her tongue down the base of his rod, sending ripples of electricity."
    "He intensified his attack, her juices pouring down his face. Claude's ass once again clenched as she came again."
    cla "H-hggnnnghh..."
    "That was only his signal to attack harder!"
    cla "E-EAAHH!!!"
    "Claude's offensive faltered as pleasure gripped her chest."
    "For a moment, Shields felt immense annoyance that she could come as many times as she wanted and for such long durations."
    "That annoyance only strengthened his resolve to leave her completely defeated."
    "Immediately after her high subsided, he dug deeper into Claude's joy nerves. He gave her ass a slap."
    kay "Aren't you forgetting something?"
    cla "Y-yes captain!"
    "She stuck his joystick back in, giving it a good rub down with her mammies."
    "She barely made it in before she gasped again."
    cla "M-mmgghh..."
    kay "(This woman... Cumming so much...!)"
    kay "(As expected of the ship's perv doc...)"
    kay "(My face is going to be a flood plain by the time she's through...!)"
    "Claude counterattacked, going down deep, her chest balloons squeezed up against his pelvis."
    "She reached the base of his dick, the cannon rod ramming against her throat."
    "Her eyes are glazed over with stupid pleasure as she came continually."
    
    scene claudeh2 with dissolve
    
    "Shields felt pressure mount. He was going to blow up, right into her mouth."
    "Her heavy boobs bounced against him as Claude sucked him up, trying to draw out his hot white cream from his dick."
    kay "(Shit... Claude...!)"
    "He held back, unwilling to surrender."
    "Claude split his opening with her tongue. He felt liquid slowly ooze out against the warm spongy texture."
    "Any more, and he was going to be past the point of no return."
    "She gripped him with her tongue and went down, her tongue running against the base."
    kay "(I can't... hold it...!!)"
    
    scene white with dissolve
    scene claudeh3 with dissolve
    
    "A spurt of cream shot out, sending the entire dam holding back the flood tumbling down."
    kay "G-ggngh...!"
    "He erupted, filling her mouth to the brim with white cream. She gasped in surprise and pulled out, sending the second volley splattering against her face."
    cla "E-eeah!"
    "A third shot erupted, no smaller than the first, drenching Claude's face in as much juice as his own face."
    "Finally, the remaining convulsions oozed out and ran down her tits."
    cla "S-so much came out... Wooww~"
    cla "The cannon has fired! Salute!"
    "Shields gasped for air."
    kay "Haa... haa..."
    cla "Teehee~"
    cla "Mah, I guess it's not bad for now. But let's do it for real tonight, okay?"
    cla "Claude wants to be puffed full of the captain's batter!"
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    