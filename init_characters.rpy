init -5:
            
    image fontana:
        "Character/Side/Fontana.png"
        yanchor 1.0 ypos 1700
        xanchor 0.5
        zoom 0.85
        subpixel True   

    image fontana neutral:
        "Character/Side/Fontana neutral.png"
        yanchor 1.0 ypos 1700
        xanchor 0.5
        zoom 0.85
        subpixel True   

    image fontana smirk:
        "Character/Side/Fontana smirk.png"
        yanchor 1.0 ypos 1700
        xanchor 0.5
        zoom 0.85
        subpixel True   

    image grey:
        "Character/Side/grey.png"
        yanchor 0.9 ypos 1.0
        xanchor 0.5
        zoom 0.6255
        subpixel True 

    image chigaraplugsuit:
        "Character/Side/chigara_plugsuit.png"
        yanchor 0.91 ypos 1.0
        xanchor 0.5
        zoom 1.0
        subpixel True 

    image arcadius:
        "Character/Side/Arcadius.png"
        yanchor 0.47 ypos 1.0
        xanchor 0.5
        zoom 0.8
        subpixel True 
    image alice:
        "Character/Side/Prototype Alice.png"
        yanchor 0.47 ypos 1.0
        xanchor 0.5
        zoom 0.8
        subpixel True 
    image prototype_alpha:
        "Character/Side/Prototype Alpha.png"
        yanchor 0.45 ypos 1.0
        xanchor 0.5
        zoom 0.8
        subpixel True 
    image alice_mask:
        "Character/Side/PrototypeAliceMask.png"
        yanchor 0.47 ypos 1.0
        xanchor 0.5
        zoom 0.8
        subpixel True 
        
    image chigara blood1:
        "Character/Side/chigara_blood1.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image chigara blood1b:
        "Character/Side/chigara_blood1b.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image chigara blood2:
        "Character/Side/chigara_blood2.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image chigara blood3:
        "Character/Side/chigara_blood3.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image chigara blood4:
        "Character/Side/chigara_blood4.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image kryska gun:
        "Character/Side/kryska_gun.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 1.0
        subpixel True   

    image lynn1:
        "Character/Side/lynn1.png"
        yanchor 1.0 ypos 1100
        xanchor 0.5
        zoom 0.82
        subpixel True   
    image lynn2:
        "Character/Side/lynn2.png"
        yanchor 1.0 ypos 1100
        xanchor 0.5
        zoom 0.82
        subpixel True   
    image kuushana:
        "Character/Side/kuushana.png"
        yanchor 1.0 ypos 1650
        xanchor 0.5
        zoom 0.85
        subpixel True   

    image kayto:
        "REturn/kayto sprite.png"
        xanchor 0.5
        zoom 0.85
        subpixel True   
        
    image kayto yell:
        "REturn/kayto sprite yell.png"
        xanchor 0.5
        zoom 0.85
        subpixel True
        
    image mook:
        "REturn/mook.png"
        zoom 0.85
        subpixel True   
        
    image drone_flames:
        "REturn/drone_burninghallway.png"
        subpixel True   
    image drone_hallway:
        "REturn/drone_hallway.png"
        subpixel True   
    image drone_engineroom:
        "REturn/drone_engineroom.png"
        subpixel True
        
    image maray excited happy:
        "Character/Side/maray_excited_happy.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image maray lean happy:
        "Character/Side/maray_lean_happy.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image maray lean narrowsmileblush:
        "Character/Side/maray_lean_narrowsmileblush.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image maray lean sadhappy:
        "Character/Side/maray_lean_sadhappy.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image maray lean sadsmile:
        "Character/Side/maray_lean_sadsmile.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True   
    image maray lean smileblush:
        "Character/Side/maray_lean_smileblush.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True
    image maray lean sad:
        "Character/Side/maray_lean_sad.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True
    image maray excited angry:
        "Character/Side/maray_excited_angry.png"
        yanchor 0 ypos -150
        xanchor 0.5
        zoom 0.84
        subpixel True        
        
        
        
        
    image dog:
        "REturn/dog.png"
        subpixel True





init python:

    # sanklegion = False
    if not hasattr(store,'sprites'):
        store.sprites = {}
        
    #this list got created with the export_element_lists function. 
    element_lists = [
        ['ava', {'armscrossed': 'Character/Ava/armscrossed/base.png'}, {'blush': 'Character/Ava/armscrossed/blush.png'}, {'smile': 'Character/Ava/armscrossed/mouth/smile.png', 'neutral': 'Character/Ava/armscrossed/mouth/neutral.png', 'shout': 'Character/Ava/armscrossed/mouth/shout.png', 'talk': 'Character/Ava/armscrossed/mouth/talk.png'}, {'neutral': 'Character/Ava/armscrossed/eyes/neutral.png', 'narrow': 'Character/Ava/armscrossed/eyes/narrow.png', 'closed': 'Character/Ava/armscrossed/eyes/closed.png'}, {'angry': 'Character/Ava/armscrossed/eyebrows/angry.png', 'neutral': 'Character/Ava/armscrossed/eyebrows/neutral.png'}, {'patch': ConditionSwitch('legion_destroyed==True','Character/Ava/armscrossed/eyepatch.png','legion_destroyed==False',Null())}],
        ['ava', {'fingerup': 'Character/Ava/fingerup/base.png'}, {'blush': 'Character/Ava/fingerup/blush.png'}, {'smile': 'Character/Ava/fingerup/mouth/smile.png', 'neutral': 'Character/Ava/fingerup/mouth/neutral.png', 'shout': 'Character/Ava/fingerup/mouth/shout.png', 'talk': 'Character/Ava/fingerup/mouth/talk.png'}, {'neutral': 'Character/Ava/fingerup/eyes/neutral.png', 'narrow': 'Character/Ava/fingerup/eyes/narrow.png'}, {'angry': 'Character/Ava/fingerup/eyebrows/angry.png', 'neutral': 'Character/Ava/fingerup/eyebrows/neutral.png'}, {'patch': ConditionSwitch('legion_destroyed==True','Character/Ava/fingerup/eyepatch.png','legion_destroyed==False',Null())}],
        ['ava', {'handonhair': 'Character/Ava/handonhair/base.png'}, {'blush': 'Character/Ava/handonhair/blush.png'}, {'pout': 'Character/Ava/handonhair/mouth/pout.png', 'smirk': 'Character/Ava/handonhair/mouth/smirk.png', 'neutral': 'Character/Ava/handonhair/mouth/neutral.png', 'laugh': 'Character/Ava/handonhair/mouth/laugh.png', 'disgust': 'Character/Ava/handonhair/mouth/disgust.png'}, {'neutral': 'Character/Ava/handonhair/eyes/neutral.png', 'narrow': 'Character/Ava/handonhair/eyes/narrow.png', 'closed': 'Character/Ava/handonhair/eyes/closed.png'}, {'angry2': 'Character/Ava/handonhair/eyebrows/angry2.png', 'angry': 'Character/Ava/handonhair/eyebrows/angry.png', 'neutral': 'Character/Ava/handonhair/eyebrows/neutral.png', 'laugh': 'Character/Ava/handonhair/eyebrows/laugh.png', 'sad': 'Character/Ava/handonhair/eyebrows/sad.png'}, {'patch': ConditionSwitch('legion_destroyed==True','Character/Ava/handonhair/eyepatch.png','legion_destroyed==False',Null())}, {'tears': 'Character/Ava/handonhair/tears.png', 'closedeyestears': 'Character/Ava/handonhair/closedeyestears.png'}],
        ['ava', {'handonhip': 'Character/Ava/handonhip/base.png'}, {'blush': 'Character/Ava/handonhip/blush.png'}, {'smile': 'Character/Ava/handonhip/mouth/smile.png', 'neutral': 'Character/Ava/handonhip/mouth/neutral.png', 'shout': 'Character/Ava/handonhip/mouth/shout.png', 'talk': 'Character/Ava/handonhip/mouth/talk.png'}, {'neutral': 'Character/Ava/handonhip/eyes/neutral.png', 'narrow': 'Character/Ava/handonhip/eyes/narrow.png'}, {'angry': 'Character/Ava/handonhip/eyebrows/angry.png', 'neutral': 'Character/Ava/handonhip/eyebrows/neutral.png'}, {'patch': ConditionSwitch('legion_destroyed==True','Character/Ava/handonhip/eyepatch.png','legion_destroyed==False',Null())}],
        ['ava', {'salute': 'Character/Ava/salute/base.png'}, {'blush': Null()}, {'neutral': 'Character/Ava/salute/mouth/neutral.png', 'shout': 'Character/Ava/salute/mouth/shout.png'}, {'neutral': 'Character/Ava/salute/eyes/neutral.png', 'narrow': 'Character/Ava/salute/eyes/narrow.png'}, {'angry': 'Character/Ava/salute/eyebrows/angry.png', 'neutral': 'Character/Ava/salute/eyebrows/neutral.png'}, {'patch': ConditionSwitch('legion_destroyed==True','Character/Ava/salute/eyepatch.png','legion_destroyed==False',Null())}],
        ['ava', {u'zshot': u'Character/Ava/zshot/base.png'}, {'blush': u'Character/Ava/zshot/blush.png'}, {u'smile': u'Character/Ava/zshot/mouth/smile.png', u'neutral': u'Character/Ava/zshot/mouth/neutral.png', u'shout': u'Character/Ava/zshot/mouth/shout.png', u'talk': u'Character/Ava/zshot/mouth/talk.png'}, {u'neutral': u'Character/Ava/zshot/eyes/neutral.png', u'narrow': u'Character/Ava/zshot/eyes/narrow.png', u'dead': u'Character/Ava/zshot/eyes/dead.png'}, {u'angry': u'Character/Ava/zshot/eyebrows/angry.png', u'neutral': u'Character/Ava/zshot/eyebrows/neutral.png'}, {'patch': ConditionSwitch('legion_destroyed==True','Character/Ava/zshot/eyepatch.png','legion_destroyed==False',Null())}],
        ['asaga', {u'armscrossed': u'Character/Asaga/armscrossed/base.png'}, {'blush': u'Character/Asaga/armscrossed/blush.png'}, {u'frown': u'Character/Asaga/armscrossed/mouth/frown.png', u'uu': u'Character/Asaga/armscrossed/mouth/uu.png', u'kitty': u'Character/Asaga/armscrossed/mouth/kitty.png', u'frown2': u'Character/Asaga/armscrossed/mouth/frown2.png', u'smile': u'Character/Asaga/armscrossed/mouth/smile.png', u'yell': u'Character/Asaga/armscrossed/mouth/yell.png', u'happy': u'Character/Asaga/armscrossed/mouth/happy.png'}, {u'zawakened': u'Character/Asaga/armscrossed/eyes/zawakened.png', u'narrow2': u'Character/Asaga/armscrossed/eyes/narrow2.png', u'arrow': u'Character/Asaga/armscrossed/eyes/arrow.png', u'zawakenednarrow': u'Character/Asaga/armscrossed/eyes/zawakenednarrow.png', u'neutral': u'Character/Asaga/armscrossed/eyes/neutral.png', u'closed': u'Character/Asaga/armscrossed/eyes/closed.png', u'narrow': u'Character/Asaga/armscrossed/eyes/narrow.png', u'closed2': u'Character/Asaga/armscrossed/eyes/closed2.png'}, {u'angry': u'Character/Asaga/armscrossed/eyebrows/angry.png', u'up': u'Character/Asaga/armscrossed/eyebrows/up.png', u'sad': u'Character/Asaga/armscrossed/eyebrows/sad.png', u'down': u'Character/Asaga/armscrossed/eyebrows/down.png', u'sad2': u'Character/Asaga/armscrossed/eyebrows/sad2.png', u'sad3': u'Character/Asaga/armscrossed/eyebrows/sad3.png'}, None, {'comiccry': 'Character/Asaga/armscrossed/comiccry.png', 'tears': 'Character/Asaga/armscrossed/tears.png', 'closeeyetears': 'Character/Asaga/armscrossed/closeeyetears.png'}],
        ['asaga', {u'armsup': u'Character/Asaga/armsup/base.png'}, {'blush': u'Character/Asaga/armsup/blush.png'}, {u'shout': u'Character/Asaga/armsup/mouth/shout.png', u'happy': u'Character/Asaga/armsup/mouth/happy.png'}, {u'closed': u'Character/Asaga/armsup/eyes/closed.png', u'arrow': u'Character/Asaga/armsup/eyes/arrow.png', u'excited': u'Character/Asaga/armsup/eyes/excited.png'}, {u'surprise': u'Character/Asaga/armsup/eyebrows/surprise.png', u'angry': u'Character/Asaga/armsup/eyebrows/angry.png'}, None],
        ['asaga', {u'excited': u'Character/Asaga/excited/base.png'}, {'blush': u'Character/Asaga/excited/blush.png'}, {u'yell': u'Character/Asaga/excited/mouth/yell.png', u'happy': u'Character/Asaga/excited/mouth/happy.png'}, {u'wide': u'Character/Asaga/excited/eyes/wide.png', u'neutral': u'Character/Asaga/excited/eyes/neutral.png', u'narrow': u'Character/Asaga/excited/eyes/narrow.png', u'zawakenednarrow': u'Character/Asaga/excited/eyes/zawakenednarrow.png', u'zawakened': u'Character/Asaga/excited/eyes/zawakened.png'}, {u'angry': u'Character/Asaga/excited/eyebrows/angry.png', u'neutral': u'Character/Asaga/excited/eyebrows/neutral.png'}, None],
        ['asaga', {u'leanforward': u'Character/Asaga/leanforward/base.png'}, {'blush': u'Character/Asaga/leanforward/blush.png'}, {u'yell': u'Character/Asaga/leanforward/mouth/yell.png', u'grin': u'Character/Asaga/leanforward/mouth/grin.png', u'happy': u'Character/Asaga/leanforward/mouth/happy.png'}, {u'neutral': u'Character/Asaga/leanforward/eyes/neutral.png', u'narrow': u'Character/Asaga/leanforward/eyes/narrow.png', u'closed': u'Character/Asaga/leanforward/eyes/closed.png'}, {u'angry': u'Character/Asaga/leanforward/eyebrows/angry.png', u'neutral': u'Character/Asaga/leanforward/eyebrows/neutral.png', u'sad': u'Character/Asaga/leanforward/eyebrows/sad.png'}, None],
        ['asaga', {u'point': u'Character/Asaga/point/base.png'}, {'blush': u'Character/Asaga/point/blush.png'}, {u'happy': u'Character/Asaga/point/mouth/happy.png'}, {u'zawakened': u'Character/Asaga/point/eyes/zawakened.png', u'neutral': u'Character/Asaga/point/eyes/neutral.png', u'zawakenednarrow': u'Character/Asaga/point/eyes/zawakenednarrow.png', u'closed': u'Character/Asaga/point/eyes/closed.png'}, {u'neutral': u'Character/Asaga/point/eyebrows/neutral.png'}, None],
        ['asaga', {u'zarmscrossed_plugsuit': u'Character/Asaga/zarmscrossed_plugsuit/base.png'}, {'blush': u'Character/Asaga/zarmscrossed_plugsuit/blush.png'}, {u'frown': u'Character/Asaga/zarmscrossed_plugsuit/mouth/frown.png', u'uu': u'Character/Asaga/zarmscrossed_plugsuit/mouth/uu.png', u'kitty': u'Character/Asaga/zarmscrossed_plugsuit/mouth/kitty.png', u'frown2': u'Character/Asaga/zarmscrossed_plugsuit/mouth/frown2.png', u'smile': u'Character/Asaga/zarmscrossed_plugsuit/mouth/smile.png', u'yell': u'Character/Asaga/zarmscrossed_plugsuit/mouth/yell.png', u'happy': u'Character/Asaga/zarmscrossed_plugsuit/mouth/happy.png'}, {u'zawakened': u'Character/Asaga/zarmscrossed_plugsuit/eyes/zawakened.png', u'narrow2': u'Character/Asaga/zarmscrossed_plugsuit/eyes/narrow2.png', u'arrow': u'Character/Asaga/zarmscrossed_plugsuit/eyes/arrow.png', u'zawakenednarrow': u'Character/Asaga/zarmscrossed_plugsuit/eyes/zawakenednarrow.png', u'neutral': u'Character/Asaga/zarmscrossed_plugsuit/eyes/neutral.png', u'closed': u'Character/Asaga/zarmscrossed_plugsuit/eyes/closed.png', u'narrow': u'Character/Asaga/zarmscrossed_plugsuit/eyes/narrow.png', u'closed2': u'Character/Asaga/zarmscrossed_plugsuit/eyes/closed2.png'}, {u'angry': u'Character/Asaga/zarmscrossed_plugsuit/eyebrows/angry.png', u'up': u'Character/Asaga/zarmscrossed_plugsuit/eyebrows/up.png', u'sad': u'Character/Asaga/zarmscrossed_plugsuit/eyebrows/sad.png', u'down': u'Character/Asaga/zarmscrossed_plugsuit/eyebrows/down.png', u'sad2': u'Character/Asaga/zarmscrossed_plugsuit/eyebrows/sad2.png', u'sad3': u'Character/Asaga/zarmscrossed_plugsuit/eyebrows/sad3.png'}, None],
        ['asaga', {u'zexcited_plugsuit': u'Character/Asaga/zexcited_plugsuit/base.png'}, {'blush': u'Character/Asaga/zexcited_plugsuit/blush.png'}, {u'yell': u'Character/Asaga/zexcited_plugsuit/mouth/yell.png', u'happy': u'Character/Asaga/zexcited_plugsuit/mouth/happy.png'}, {u'wide': u'Character/Asaga/zexcited_plugsuit/eyes/wide.png', u'neutral': u'Character/Asaga/zexcited_plugsuit/eyes/neutral.png', u'narrow': u'Character/Asaga/zexcited_plugsuit/eyes/narrow.png', u'zawakenednarrow': u'Character/Asaga/zexcited_plugsuit/eyes/zawakenednarrow.png', u'zawakened': u'Character/Asaga/zexcited_plugsuit/eyes/zawakened.png'}, {u'angry': u'Character/Asaga/zexcited_plugsuit/eyebrows/angry.png', u'neutral': u'Character/Asaga/zexcited_plugsuit/eyebrows/neutral.png'}, None],
        ['asaga', {u'zneutral_plugsuit': u'Character/Asaga/zneutral_plugsuit/base.png'}, {'blush': u'Character/Asaga/zneutral_plugsuit/blush.png'}, {u'smile': u'Character/Asaga/zneutral_plugsuit/mouth/smile.png', u'open': u'Character/Asaga/zneutral_plugsuit/mouth/open.png', u'talk': u'Character/Asaga/zneutral_plugsuit/mouth/talk.png', u'closed': u'Character/Asaga/zneutral_plugsuit/mouth/closed.png', u'happy': u'Character/Asaga/zneutral_plugsuit/mouth/happy.png'}, {u'zawakened': u'Character/Asaga/zneutral_plugsuit/eyes/zawakened.png', u'zawakenednarrow': u'Character/Asaga/zneutral_plugsuit/eyes/zawakenednarrow.png', u'dead': u'Character/Asaga/zneutral_plugsuit/eyes/dead.png', u'neutral': u'Character/Asaga/zneutral_plugsuit/eyes/neutral.png', u'closed': u'Character/Asaga/zneutral_plugsuit/eyes/closed.png', u'narrow': u'Character/Asaga/zneutral_plugsuit/eyes/narrow.png'}, {u'down': u'Character/Asaga/zneutral_plugsuit/eyebrows/down.png', u'neutral': u'Character/Asaga/zneutral_plugsuit/eyebrows/neutral.png', u'pain': u'Character/Asaga/zneutral_plugsuit/eyebrows/pain.png', u'up': u'Character/Asaga/zneutral_plugsuit/eyebrows/up.png', u'sad': u'Character/Asaga/zneutral_plugsuit/eyebrows/sad.png'}, None],
        ['asaga', {u'zshot': u'Character/Asaga/zshot/base.png'}, {'blush': u'Character/Asaga/zshot/blush.png'}, {u'smile': u'Character/Asaga/zshot/mouth/smile.png', u'open': u'Character/Asaga/zshot/mouth/open.png', u'talk': u'Character/Asaga/zshot/mouth/talk.png', u'closed': u'Character/Asaga/zshot/mouth/closed.png', u'happy': u'Character/Asaga/zshot/mouth/happy.png'}, {u'neutral': u'Character/Asaga/zshot/eyes/neutral.png', u'narrow': u'Character/Asaga/zshot/eyes/narrow.png', u'dead': u'Character/Asaga/zshot/eyes/dead.png', u'closed': u'Character/Asaga/zshot/eyes/closed.png'}, {u'down': u'Character/Asaga/zshot/eyebrows/down.png', u'neutral': u'Character/Asaga/zshot/eyebrows/neutral.png', u'pain': u'Character/Asaga/zshot/eyebrows/pain.png', u'up': u'Character/Asaga/zshot/eyebrows/up.png', u'sad': u'Character/Asaga/zshot/eyebrows/sad.png'}, None, {'tears': 'Character/Asaga/zshot/tears.png'}],
        ['chigara', {u'armsbehindback': u'Character/Chigara/armsbehindback/base.png'}, {'blush': u'Character/Chigara/armsbehindback/blush.png'}, {u'smile': u'Character/Chigara/armsbehindback/mouth/smile.png', u'frown': u'Character/Chigara/armsbehindback/mouth/frown.png'}, {u'neutral': u'Character/Chigara/armsbehindback/eyes/neutral.png', u'closed': u'Character/Chigara/armsbehindback/eyes/closed.png'}, {u'embarass': u'Character/Chigara/armsbehindback/eyebrows/embarass.png', u'neutral': u'Character/Chigara/armsbehindback/eyebrows/neutral.png', u'sad': u'Character/Chigara/armsbehindback/eyebrows/sad.png'}, None],
        ['chigara', {u'handonchest': u'Character/Chigara/handonchest/base.png'}, {'blush': u'Character/Chigara/handonchest/blush.png'}, {u'smile': u'Character/Chigara/handonchest/mouth/smile.png', u'neutral': u'Character/Chigara/handonchest/mouth/neutral.png', u'cry': u'Character/Chigara/handonchest/mouth/cry.png', u'yell': u'Character/Chigara/handonchest/mouth/yell.png'}, {u'neutral': u'Character/Chigara/handonchest/eyes/neutral.png', u'narrow': u'Character/Chigara/handonchest/eyes/narrow.png', u'closed': u'Character/Chigara/handonchest/eyes/closed.png'}, {u'embarass': u'Character/Chigara/handonchest/eyebrows/embarass.png', u'neutral': u'Character/Chigara/handonchest/eyebrows/neutral.png', u'focus': u'Character/Chigara/handonchest/eyebrows/focus.png', u'sad': u'Character/Chigara/handonchest/eyebrows/sad.png'}, None, {'tears': 'Character/Chigara/handonchest/tears.png', 'closedeyestears': 'Character/Chigara/handonchest/closedeyestears.png'}],
        ['chigara', {u'handonface': u'Character/Chigara/handonface/base.png'}, {'blush': u'Character/Chigara/handonface/blush.png'}, {u'uuu': u'Character/Chigara/handonface/mouth/uuu.png', u'smile': u'Character/Chigara/handonface/mouth/smile.png', u'cry': u'Character/Chigara/handonface/mouth/cry.png', u'frown': u'Character/Chigara/handonface/mouth/frown.png'}, {u'neutral': u'Character/Chigara/handonface/eyes/neutral.png', u'narrow': u'Character/Chigara/handonface/eyes/narrow.png', u'closed': u'Character/Chigara/handonface/eyes/closed.png'}, {u'neutral': u'Character/Chigara/handonface/eyebrows/neutral.png', u'sad2': u'Character/Chigara/handonface/eyebrows/sad2.png', u'sad': u'Character/Chigara/handonface/eyebrows/sad.png'}, None, {'tears': 'Character/Chigara/handonface/tears.png', 'closedeyestears': 'Character/Chigara/handonface/closedeyestears.png'}],
        ['chigara', {u'holdinghands': u'Character/Chigara/holdinghands/base.png'}, {'blush': u'Character/Chigara/holdinghands/blush.png'}, {u'smile': u'Character/Chigara/holdinghands/mouth/smile.png', u'ztalk': u'Character/Chigara/holdinghands/mouth/ztalk.png', u'zfrown': u'Character/Chigara/holdinghands/mouth/zfrown.png', u'frown': u'Character/Chigara/holdinghands/mouth/frown.png', u'zgrin': u'Character/Chigara/holdinghands/mouth/zgrin.png'}, {u'zfunny': u'Character/Chigara/holdinghands/eyes/zfunny.png', u'zwide': u'Character/Chigara/holdinghands/eyes/zwide.png', u'neutral': u'Character/Chigara/holdinghands/eyes/neutral.png', u'znarrow': u'Character/Chigara/holdinghands/eyes/znarrow.png', u'closed': u'Character/Chigara/holdinghands/eyes/closed.png', u'zneutral': u'Character/Chigara/holdinghands/eyes/zneutral.png'}, {u'embarass': u'Character/Chigara/holdinghands/eyebrows/embarass.png', u'zlow': u'Character/Chigara/holdinghands/eyebrows/zlow.png', u'zhigh': u'Character/Chigara/holdinghands/eyebrows/zhigh.png', u'neutral': u'Character/Chigara/holdinghands/eyebrows/neutral.png', u'zangry': u'Character/Chigara/holdinghands/eyebrows/zangry.png', u'zmock': u'Character/Chigara/holdinghands/eyebrows/zmock.png'}, None],
        ['chigara', {u'surprise': u'Character/Chigara/surprise/base.png'}, {'blush': u'Character/Chigara/surprise/blush.png'}, {u'yell': u'Character/Chigara/surprise/mouth/yell.png'}, {u'surprise': u'Character/Chigara/surprise/eyes/surprise.png', u'narrow': u'Character/Chigara/surprise/eyes/narrow.png', u'arrow': u'Character/Chigara/surprise/eyes/arrow.png'}, {u'embarass': u'Character/Chigara/surprise/eyebrows/embarass.png', u'lowfocus': u'Character/Chigara/surprise/eyebrows/lowfocus.png', u'neutral': u'Character/Chigara/surprise/eyebrows/neutral.png', u'focus': u'Character/Chigara/surprise/eyebrows/focus.png'}, None],['claude', {u'boobs': u'Character/Claude/boobs/base.png'}, {'blush': Null()}, {u'happy': u'Character/Claude/boobs/mouth/happy.png'}, {u'neutral': u'Character/Claude/boobs/eyes/neutral.png', u'closed': u'Character/Claude/boobs/eyes/closed.png'}, {u'neutral': u'Character/Claude/boobs/eyebrows/neutral.png'}],
        ['claude', {u'boobsnurse': u'Character/Claude/boobsnurse/base.png'}, {'blush': Null()}, {u'happy': u'Character/Claude/boobsnurse/mouth/happy.png'}, {u'neutral': u'Character/Claude/boobsnurse/eyes/neutral.png', u'closed': u'Character/Claude/boobsnurse/eyes/closed.png'}, {u'neutral': u'Character/Claude/boobsnurse/eyebrows/neutral.png'}],
        ['claude', {u'fingerup': u'Character/Claude/fingerup/base.png'}, {'blush': u'Character/Claude/fingerup/blush.png'}, {u'smile': u'Character/Claude/fingerup/mouth/smile.png', u'neutral': u'Character/Claude/fingerup/mouth/neutral.png', u'talk': u'Character/Claude/fingerup/mouth/talk.png', u'happy': u'Character/Claude/fingerup/mouth/happy.png'}, {u'neutral': u'Character/Claude/fingerup/eyes/neutral.png', u'closed': u'Character/Claude/fingerup/eyes/closed.png'}, {u'neutral': u'Character/Claude/fingerup/eyebrows/neutral.png', u'upset': u'Character/Claude/fingerup/eyebrows/upset.png'}],
        ['claude', {u'fingerupnurse': u'Character/Claude/fingerupnurse/base.png'}, {'blush': u'Character/Claude/fingerupnurse/blush.png'}, {u'smile': u'Character/Claude/fingerupnurse/mouth/smile.png', u'neutral': u'Character/Claude/fingerupnurse/mouth/neutral.png', u'talk': u'Character/Claude/fingerupnurse/mouth/talk.png', u'happy': u'Character/Claude/fingerupnurse/mouth/happy.png'}, {u'neutral': u'Character/Claude/fingerupnurse/eyes/neutral.png', u'closed': u'Character/Claude/fingerupnurse/eyes/closed.png'}, {u'neutral': u'Character/Claude/fingerupnurse/eyebrows/neutral.png', u'upset': u'Character/Claude/fingerupnurse/eyebrows/upset.png'}],
        ['claude', {u'neutral': u'Character/Claude/neutral/base.png'}, {'blush': u'Character/Claude/neutral/blush.png'}, {u'smile': u'Character/Claude/neutral/mouth/smile.png', u'neutral': u'Character/Claude/neutral/mouth/neutral.png', u'talk': u'Character/Claude/neutral/mouth/talk.png', u'happy': u'Character/Claude/neutral/mouth/happy.png'}, {u'neutral': u'Character/Claude/neutral/eyes/neutral.png', u'closed': u'Character/Claude/neutral/eyes/closed.png'}, {u'neutral': u'Character/Claude/neutral/eyebrows/neutral.png', u'upset': u'Character/Claude/neutral/eyebrows/upset.png'}],
        ['claude', {u'neutralnurse': u'Character/Claude/neutralnurse/base.png'}, {'blush': u'Character/Claude/neutralnurse/blush.png'}, {u'smile': u'Character/Claude/neutralnurse/mouth/smile.png', u'neutral': u'Character/Claude/neutralnurse/mouth/neutral.png', u'talk': u'Character/Claude/neutralnurse/mouth/talk.png', u'happy': u'Character/Claude/neutralnurse/mouth/happy.png'}, {u'neutral': u'Character/Claude/neutralnurse/eyes/neutral.png', u'closed': u'Character/Claude/neutralnurse/eyes/closed.png'}, {u'neutral': u'Character/Claude/neutralnurse/eyebrows/neutral.png', u'upset': u'Character/Claude/neutralnurse/eyebrows/upset.png'}],
        ['claude', {u'salute': u'Character/Claude/salute/base.png'}, {'blush': u'Character/Claude/salute/blush.png'}, {u'smile': u'Character/Claude/salute/mouth/smile.png', u'neutral': u'Character/Claude/salute/mouth/neutral.png', u'talk': u'Character/Claude/salute/mouth/talk.png', u'happy': u'Character/Claude/salute/mouth/happy.png'}, {u'neutral': u'Character/Claude/salute/eyes/neutral.png', u'closed': u'Character/Claude/salute/eyes/closed.png'}, {u'neutral': u'Character/Claude/salute/eyebrows/neutral.png', u'upset': u'Character/Claude/salute/eyebrows/upset.png'}],
        ['claude', {u'salutenurse': u'Character/Claude/salutenurse/base.png'}, {'blush': u'Character/Claude/salutenurse/blush.png'}, {u'smile': u'Character/Claude/salutenurse/mouth/smile.png', u'neutral': u'Character/Claude/salutenurse/mouth/neutral.png', u'talk': u'Character/Claude/salutenurse/mouth/talk.png', u'happy': u'Character/Claude/salutenurse/mouth/happy.png'}, {u'neutral': u'Character/Claude/salutenurse/eyes/neutral.png', u'closed': u'Character/Claude/salutenurse/eyes/closed.png'}, {u'neutral': u'Character/Claude/salutenurse/eyebrows/neutral.png', u'upset': u'Character/Claude/salutenurse/eyebrows/upset.png'}],
        ['claude', {u'zboobs_naked': u'Character/Claude/zboobs_naked/base.png'}, {'blush': Null()}, {u'happy': u'Character/Claude/zboobs_naked/mouth/happy.png'}, {u'neutral': u'Character/Claude/zboobs_naked/eyes/neutral.png', u'closed': u'Character/Claude/zboobs_naked/eyes/closed.png'}, {u'neutral': u'Character/Claude/zboobs_naked/eyebrows/neutral.png'}],
        ['claude', {u'zfingerup_naked': u'Character/Claude/zfingerup_naked/base.png'}, {'blush': u'Character/Claude/zfingerup_naked/blush.png'}, {u'smile': u'Character/Claude/zfingerup_naked/mouth/smile.png', u'neutral': u'Character/Claude/zfingerup_naked/mouth/neutral.png', u'talk': u'Character/Claude/zfingerup_naked/mouth/talk.png', u'happy': u'Character/Claude/zfingerup_naked/mouth/happy.png'}, {u'neutral': u'Character/Claude/zfingerup_naked/eyes/neutral.png', u'closed': u'Character/Claude/zfingerup_naked/eyes/closed.png'}, {u'neutral': u'Character/Claude/zfingerup_naked/eyebrows/neutral.png', u'upset': u'Character/Claude/zfingerup_naked/eyebrows/upset.png'}],
        ['claude', {u'zneutral_naked': u'Character/Claude/zneutral_naked/base.png'}, {'blush': u'Character/Claude/zneutral_naked/blush.png'}, {u'smile': u'Character/Claude/zneutral_naked/mouth/smile.png', u'neutral': u'Character/Claude/zneutral_naked/mouth/neutral.png', u'talk': u'Character/Claude/zneutral_naked/mouth/talk.png', u'happy': u'Character/Claude/zneutral_naked/mouth/happy.png'}, {u'neutral': u'Character/Claude/zneutral_naked/eyes/neutral.png', u'closed': u'Character/Claude/zneutral_naked/eyes/closed.png'}, {u'neutral': u'Character/Claude/zneutral_naked/eyebrows/neutral.png', u'upset': u'Character/Claude/zneutral_naked/eyebrows/upset.png'}],
        ['claude', {u'zsalute_naked': u'Character/Claude/zsalute_naked/base.png'}, {'blush': u'Character/Claude/zsalute_naked/blush.png'}, {u'smile': u'Character/Claude/zsalute_naked/mouth/smile.png', u'neutral': u'Character/Claude/zsalute_naked/mouth/neutral.png', u'talk': u'Character/Claude/zsalute_naked/mouth/talk.png', u'happy': u'Character/Claude/zsalute_naked/mouth/happy.png'}, {u'neutral': u'Character/Claude/zsalute_naked/eyes/neutral.png', u'closed': u'Character/Claude/zsalute_naked/eyes/closed.png'}, {u'neutral': u'Character/Claude/zsalute_naked/eyebrows/neutral.png', u'upset': u'Character/Claude/zsalute_naked/eyebrows/upset.png'}],
        ['icari', {u'armscrossed': u'Character/Icari/armscrossed/base.png'}, {'blush': u'Character/Icari/armscrossed/blush.png'}, {u'frown': u'Character/Icari/armscrossed/mouth/frown.png', u'shout': u'Character/Icari/armscrossed/mouth/shout.png', u'neutral': u'Character/Icari/armscrossed/mouth/neutral.png', u'smile': u'Character/Icari/armscrossed/mouth/smile.png', u'talk': u'Character/Icari/armscrossed/mouth/talk.png', u'happy': u'Character/Icari/armscrossed/mouth/happy.png'}, {u'confident': u'Character/Icari/armscrossed/eyes/confident.png', u'neutral': u'Character/Icari/armscrossed/eyes/neutral.png', u'closed': u'Character/Icari/armscrossed/eyes/closed.png'}, {u'embarass': u'Character/Icari/armscrossed/eyebrows/embarass.png', u'confident': u'Character/Icari/armscrossed/eyebrows/confident.png', u'angry': u'Character/Icari/armscrossed/eyebrows/angry.png', u'sad': u'Character/Icari/armscrossed/eyebrows/sad.png'},None,{'tears': 'Character/Icari/armscrossed/tears.png'}],
        ['icari', {u'handonhip': u'Character/Icari/handonhip/base.png'}, {'blush': u'Character/Icari/handonhip/blush.png'}, {u'snide': u'Character/Icari/handonhip/mouth/snide.png', u'smile': u'Character/Icari/handonhip/mouth/smile.png', u'neutral': u'Character/Icari/handonhip/mouth/neutral.png', u'shout': u'Character/Icari/handonhip/mouth/shout.png', u'happy': u'Character/Icari/handonhip/mouth/happy.png'}, {u'neutral': u'Character/Icari/handonhip/eyes/neutral.png', u'closed': u'Character/Icari/handonhip/eyes/closed.png'}, {u'confident': u'Character/Icari/handonhip/eyebrows/confident.png', u'angry': u'Character/Icari/handonhip/eyebrows/angry.png', u'neutral': u'Character/Icari/handonhip/eyebrows/neutral.png'},None,{'tears': 'Character/Icari/handonhip/tears.png'}],
        ['icari', {u'point': u'Character/Icari/point/base.png'}, {'blush': u'Character/Icari/point/blush.png'}, {u'shout': u'Character/Icari/point/mouth/shout.png'}, {u'neutral': u'Character/Icari/point/eyes/neutral.png'}, {u'angry': u'Character/Icari/point/eyebrows/angry.png'},None,{'tears': 'Character/Icari/point/tears.png'}],
        ['icari', {u'zarmscrossed_plugsuit': u'Character/Icari/zarmscrossed_plugsuit/base.png'}, {'blush': u'Character/Icari/zarmscrossed_plugsuit/blush.png'}, {u'frown': u'Character/Icari/zarmscrossed_plugsuit/mouth/frown.png', u'shout': u'Character/Icari/zarmscrossed_plugsuit/mouth/shout.png', u'neutral': u'Character/Icari/zarmscrossed_plugsuit/mouth/neutral.png', u'smile': u'Character/Icari/zarmscrossed_plugsuit/mouth/smile.png', u'talk': u'Character/Icari/zarmscrossed_plugsuit/mouth/talk.png', u'happy': u'Character/Icari/zarmscrossed_plugsuit/mouth/happy.png'}, {u'confident': u'Character/Icari/zarmscrossed_plugsuit/eyes/confident.png', u'neutral': u'Character/Icari/zarmscrossed_plugsuit/eyes/neutral.png', u'closed': u'Character/Icari/zarmscrossed_plugsuit/eyes/closed.png'}, {u'embarass': u'Character/Icari/zarmscrossed_plugsuit/eyebrows/embarass.png', u'confident': u'Character/Icari/zarmscrossed_plugsuit/eyebrows/confident.png', u'angry': u'Character/Icari/zarmscrossed_plugsuit/eyebrows/angry.png', u'sad': u'Character/Icari/zarmscrossed_plugsuit/eyebrows/sad.png'},None,{'tears': 'Character/Icari/zarmscrossed_plugsuit/tears.png'}],
        ['icari', {u'zarmscrossed_swimsuit': u'Character/Icari/zarmscrossed_swimsuit/base.png'}, {'blush': u'Character/Icari/zarmscrossed_swimsuit/blush.png'}, {u'frown': u'Character/Icari/zarmscrossed_swimsuit/mouth/frown.png', u'shout': u'Character/Icari/zarmscrossed_swimsuit/mouth/shout.png', u'neutral': u'Character/Icari/zarmscrossed_swimsuit/mouth/neutral.png', u'smile': u'Character/Icari/zarmscrossed_swimsuit/mouth/smile.png', u'talk': u'Character/Icari/zarmscrossed_swimsuit/mouth/talk.png', u'happy': u'Character/Icari/zarmscrossed_swimsuit/mouth/happy.png'}, {u'confident': u'Character/Icari/zarmscrossed_swimsuit/eyes/confident.png', u'neutral': u'Character/Icari/zarmscrossed_swimsuit/eyes/neutral.png', u'closed': u'Character/Icari/zarmscrossed_swimsuit/eyes/closed.png'}, {u'embarass': u'Character/Icari/zarmscrossed_swimsuit/eyebrows/embarass.png', u'confident': u'Character/Icari/zarmscrossed_swimsuit/eyebrows/confident.png', u'angry': u'Character/Icari/zarmscrossed_swimsuit/eyebrows/angry.png', u'sad': u'Character/Icari/zarmscrossed_swimsuit/eyebrows/sad.png'},None,{'tears': 'Character/Icari/zarmscrossed_plugsuit/tears.png'}],
        ['icari', {u'zhandonhip_plugsuit': u'Character/Icari/zhandonhip_plugsuit/base.png'}, {'blush': Null()}, {u'snide': u'Character/Icari/zhandonhip_plugsuit/mouth/snide.png', u'smile': u'Character/Icari/zhandonhip_plugsuit/mouth/smile.png', u'neutral': u'Character/Icari/zhandonhip_plugsuit/mouth/neutral.png', u'shout': u'Character/Icari/zhandonhip_plugsuit/mouth/shout.png', u'happy': u'Character/Icari/zhandonhip_plugsuit/mouth/happy.png'}, {u'neutral': u'Character/Icari/zhandonhip_plugsuit/eyes/neutral.png', u'closed': u'Character/Icari/zhandonhip_plugsuit/eyes/closed.png'}, {u'confident': u'Character/Icari/zhandonhip_plugsuit/eyebrows/confident.png', u'angry': u'Character/Icari/zhandonhip_plugsuit/eyebrows/angry.png', u'neutral': u'Character/Icari/zhandonhip_plugsuit/eyebrows/neutral.png'},None,{'tears': 'Character/Icari/zhandonhip_plugsuit/tears.png'}],
        ['icari', {u'zhandonhip_swimsuit': u'Character/Icari/zhandonhip_swimsuit/base.png'}, {'blush': Null()}, {u'snide': u'Character/Icari/zhandonhip_swimsuit/mouth/snide.png', u'smile': u'Character/Icari/zhandonhip_swimsuit/mouth/smile.png', u'neutral': u'Character/Icari/zhandonhip_swimsuit/mouth/neutral.png', u'shout': u'Character/Icari/zhandonhip_swimsuit/mouth/shout.png', u'happy': u'Character/Icari/zhandonhip_swimsuit/mouth/happy.png'}, {u'neutral': u'Character/Icari/zhandonhip_swimsuit/eyes/neutral.png', u'closed': u'Character/Icari/zhandonhip_swimsuit/eyes/closed.png'}, {u'confident': u'Character/Icari/zhandonhip_swimsuit/eyebrows/confident.png', u'angry': u'Character/Icari/zhandonhip_swimsuit/eyebrows/angry.png', u'neutral': u'Character/Icari/zhandonhip_swimsuit/eyebrows/neutral.png'},None,{'tears': 'Character/Icari/zhandonhip_plugsuit/tears.png'}],
        ['icari', {u'zpoint_plugsuit': u'Character/Icari/zpoint_plugsuit/base.png'}, {'blush': u'Character/Icari/zpoint_plugsuit/blush.png'}, {u'shout': u'Character/Icari/zpoint_plugsuit/mouth/shout.png'}, {u'neutral': u'Character/Icari/zpoint_plugsuit/eyes/neutral.png'}, {u'angry': u'Character/Icari/zpoint_plugsuit/eyebrows/angry.png'},None,{'tears': 'Character/Icari/zpoint_plugsuit/tears.png'}],
        ['kryska', {u'fistup': u'Character/Kryska/fistup/base.png'}, {'blush': Null()}, {u'smirk': u'Character/Kryska/fistup/mouth/smirk.png', u'happy': u'Character/Kryska/fistup/mouth/happy.png'}, {u'neutral': u'Character/Kryska/fistup/eyes/neutral.png'}, {u'angry': u'Character/Kryska/fistup/eyebrows/angry.png'}],
        ['kryska', {u'neutral': u'Character/Kryska/neutral/base.png'}, {'blush': u'Character/Kryska/neutral/blush.png'}, {u'smile': u'Character/Kryska/neutral/mouth/smile.png', u'neutral': u'Character/Kryska/neutral/mouth/neutral.png', u'surprise': u'Character/Kryska/neutral/mouth/surprise.png', u'smirk': u'Character/Kryska/neutral/mouth/smirk.png'}, {u'surprise': u'Character/Kryska/neutral/eyes/surprise.png', u'neutral': u'Character/Kryska/neutral/eyes/neutral.png', u'zomg': u'Character/Kryska/neutral/eyes/zomg.png'}, {u'surprise': u'Character/Kryska/neutral/eyebrows/surprise.png', u'angry': u'Character/Kryska/neutral/eyebrows/angry.png', u'neutral': u'Character/Kryska/neutral/eyebrows/neutral.png'}],
        ['kryska', {u'salute': u'Character/Kryska/salute/base.png'}, {'blush': Null()}, {u'neutral': u'Character/Kryska/salute/mouth/neutral.png', u'shout': u'Character/Kryska/salute/mouth/shout.png', u'happy': u'Character/Kryska/salute/mouth/happy.png'}, {u'neutral': u'Character/Kryska/salute/eyes/neutral.png'}, {u'angry': u'Character/Kryska/salute/eyebrows/angry.png'}],
        ['sola', {u'armhold': u'Character/Sola/armhold/base.png'}, {'blush': u'Character/Sola/armhold/blush.png'}, {u'smile': u'Character/Sola/armhold/mouth/smile.png', u'neutral': u'Character/Sola/armhold/mouth/neutral.png', u'yell': u'Character/Sola/armhold/mouth/yell.png', u'frown': u'Character/Sola/armhold/mouth/frown.png', u'clench': u'Character/Sola/armhold/mouth/clench.png'}, {u'neutral': u'Character/Sola/armhold/eyes/neutral.png', u'narrow': u'Character/Sola/armhold/eyes/narrow.png', u'zawaken': u'Character/Sola/armhold/eyes/zawaken.png', u'closed': u'Character/Sola/armhold/eyes/closed.png', u'zawakennarrow': u'Character/Sola/armhold/eyes/zawakennarrow.png'}, {u'neutral': u'Character/Sola/armhold/eyebrows/neutral.png', u'mad': u'Character/Sola/armhold/eyebrows/mad.png', u'sad2': u'Character/Sola/armhold/eyebrows/sad2.png', u'sad': u'Character/Sola/armhold/eyebrows/sad.png'}, {'hair': u'Character/Sola/armhold/hair.png'}, {'tears': 'Character/Sola/armhold/tears.png'}],
        ['sola', {u'back': u'Character/Sola/back/base.png'}, {'blush': Null()}, {u'neutral': u'Character/Sola/back/mouth/neutral.png'}, {u'neutral': u'Character/Sola/back/eyes/neutral.png'}, {u'neutral': u'Character/Sola/back/eyebrows/neutral.png'}, {'hair': u'Character/Sola/back/hair.png'}],
        ['sola', {u'zarmhold_plugsuit': u'Character/Sola/zarmhold_plugsuit/base.png'}, {'blush': u'Character/Sola/zarmhold_plugsuit/blush.png'}, {u'smile': u'Character/Sola/zarmhold_plugsuit/mouth/smile.png', u'neutral': u'Character/Sola/zarmhold_plugsuit/mouth/neutral.png', u'yell': u'Character/Sola/zarmhold_plugsuit/mouth/yell.png', u'frown': u'Character/Sola/zarmhold_plugsuit/mouth/frown.png', u'clench': u'Character/Sola/zarmhold_plugsuit/mouth/clench.png'}, {u'neutral': u'Character/Sola/zarmhold_plugsuit/eyes/neutral.png', u'narrow': u'Character/Sola/zarmhold_plugsuit/eyes/narrow.png', u'zawaken': u'Character/Sola/zarmhold_plugsuit/eyes/zawaken.png', u'closed': u'Character/Sola/zarmhold_plugsuit/eyes/closed.png', u'zawakennarrow': u'Character/Sola/zarmhold_plugsuit/eyes/zawakennarrow.png'}, {u'neutral': u'Character/Sola/zarmhold_plugsuit/eyebrows/neutral.png', u'mad': u'Character/Sola/zarmhold_plugsuit/eyebrows/mad.png', u'sad2': u'Character/Sola/zarmhold_plugsuit/eyebrows/sad2.png', u'sad': u'Character/Sola/zarmhold_plugsuit/eyebrows/sad.png'}, {'hair': u'Character/Sola/zarmhold_plugsuit/hair.png'}],
        ['sola', {u'zback_plugsuit': u'Character/Sola/zback_plugsuit/base.png'}, {'blush': Null()}, {u'neutral': u'Character/Sola/zback_plugsuit/mouth/neutral.png'}, {u'neutral': u'Character/Sola/zback_plugsuit/eyes/neutral.png'}, {u'neutral': u'Character/Sola/zback_plugsuit/eyebrows/neutral.png'}, {'hair': u'Character/Sola/zback_plugsuit/hair.png'}],
        ['sola', {u'zshot': u'Character/Sola/zshot/base.png'}, {'blush': u'Character/Sola/zshot/blush.png'}, {u'smile': u'Character/Sola/zshot/mouth/smile.png', u'neutral': u'Character/Sola/zshot/mouth/neutral.png', u'yell': u'Character/Sola/zshot/mouth/yell.png', u'frown': u'Character/Sola/zshot/mouth/frown.png', u'clench': u'Character/Sola/zshot/mouth/clench.png'}, {u'neutral': u'Character/Sola/zshot/eyes/neutral.png', u'narrow': u'Character/Sola/zshot/eyes/narrow.png', u'dead': u'Character/Sola/zshot/eyes/dead.png', u'closed': u'Character/Sola/zshot/eyes/closed.png'}, {u'neutral': u'Character/Sola/zshot/eyebrows/neutral.png', u'mad': u'Character/Sola/zshot/eyebrows/mad.png', u'sad2': u'Character/Sola/zshot/eyebrows/sad2.png', u'sad': u'Character/Sola/zshot/eyebrows/sad.png'}, {'hair': u'Character/Sola/zshot/hair.png'}, {'tears': 'Character/Sola/zshot/tears.png'}],
        ['zalice', {u'plugsuit': u'Character/zAlice/plugsuit/base.png'}, {'blush': Null()}, {u'smirk': u'Character/zAlice/plugsuit/mouth/smirk.png', u'shout': u'Character/zAlice/plugsuit/mouth/shout.png', u'neutral': u'Character/zAlice/plugsuit/mouth/neutral.png', u'talk': u'Character/zAlice/plugsuit/mouth/talk.png', u'laugh': u'Character/zAlice/plugsuit/mouth/laugh.png', u'clench': u'Character/zAlice/plugsuit/mouth/clench.png', u'grin': u'Character/zAlice/plugsuit/mouth/grin.png'}, {u'wide': u'Character/zAlice/plugsuit/eyes/wide.png', u'neutral': u'Character/zAlice/plugsuit/eyes/neutral.png', u'narrow': u'Character/zAlice/plugsuit/eyes/narrow.png'}, {u'serious': u'Character/zAlice/plugsuit/eyebrows/serious.png', u'angry': u'Character/zAlice/plugsuit/eyebrows/angry.png', u'neutral': u'Character/zAlice/plugsuit/eyebrows/neutral.png'}],
        ['zalice', {u'uniform': u'Character/zAlice/uniform/base.png'}, {'blush': Null()}, {u'smirk': u'Character/zAlice/uniform/mouth/smirk.png', u'shout': u'Character/zAlice/uniform/mouth/shout.png', u'neutral': u'Character/zAlice/uniform/mouth/neutral.png', u'talk': u'Character/zAlice/uniform/mouth/talk.png', u'laugh': u'Character/zAlice/uniform/mouth/laugh.png', u'clench': u'Character/zAlice/uniform/mouth/clench.png', u'grin': u'Character/zAlice/uniform/mouth/grin.png'}, {u'wide': u'Character/zAlice/uniform/eyes/wide.png', u'neutral': u'Character/zAlice/uniform/eyes/neutral.png', u'narrow': u'Character/zAlice/uniform/eyes/narrow.png'}, {u'serious': u'Character/zAlice/uniform/eyebrows/serious.png', u'angry': u'Character/zAlice/uniform/eyebrows/angry.png', u'neutral': u'Character/zAlice/uniform/eyebrows/neutral.png'}],
        ]


        
    #actually build the store.sprites dict which dshow relies upon.
    for element_list in element_lists:
        CharacterSprite(*element_list).init_images()
    
    def export_element_lists():
        FULL_PATH = os.path.join(config.basedir,"game/")
        export_dir_path = os.path.abspath(os.path.join(config.basedir, "exports"))
        try:
            os.makedirs(export_dir_path, 0777)
        except:
            pass
        export_file_path = os.path.join(export_dir_path, 'element list export.txt')
        
        with open(export_file_path,'w') as f:
            
            #Ava
            #all your base!
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Ava/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Ava',b)
                element_list.append({"patch":"ConditionSwitch('legion_destroyed==True','Character/Ava/'"+b+"/eyepatch.png','legion_destroyed==False','Null())'"})
                #adding tear files manually because they don't have their own folder :/
                if b == 'handonhair':
                    element_list.append(
                        {'closedeyestears':'Character/Ava/handonhair/closedeyestears.png',                
                        'tears':'Character/Ava/handonhair/tears.png',})
                f.write( str(element_list) + ',\n')
                
            #Asaga
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Asaga/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Asaga',b)
                element_list.append(None) #skip extras
                if b == 'armscrossed':
                    element_list.append(
                        {'closeeyetears':'Character/Asaga/armscrossed/closeeyetears.png',
                        'comiccry':'Character/Asaga/armscrossed/comiccry.png',
                        'tears':'Character/Asaga/armscrossed/tears.png',})
                if b == 'zshot':
                    element_list.append({'tears':'Character/Asaga/zshot/tears.png',})
                f.write( str(element_list) + ',\n')

            #Chigara
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Chigara/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Chigara',b)
                element_list.append(None) #skip extras
                #omg so much crying going on
                if b == 'handonchest':
                    element_list.append(
                        {'closedeyestears':'Character/Chigara/handonchest/closedeyestears.png',
                        'tears':'Character/Chigara/handonchest/tears.png',})
                if b == 'handonface':
                    element_list.append(
                        {'closedeyestears':'Character/Chigara/handonface/closedeyestears.png',
                        'tears':'Character/Chigara/handonface/tears.png',})                
                f.write( str(element_list) + ',\n')

            #Claude
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Claude/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Claude',b)
                f.write( str(element_list) + ',\n')

            #Icari
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Icari/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Icari',b)
                f.write( str(element_list) + ',\n') 

            #Kryska
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Kryska/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Kryska',b)
                f.write( str(element_list) + ',\n')  

            #Sola
            all_bases = [c for c in os.listdir(FULL_PATH+'Character/Sola/') if '.' not in c]
            for b in all_bases:
                element_list = get_elementlist('Sola',b)
                element_list.append({'hair':'Character/Sola/'+b+'/hair.png'})
                if b == 'armhold':
                    element_list.append({'tears':'Character/Sola/armhold/tears.png',})
                if b == 'zshot':
                    element_list.append({'tears':'Character/Sola/zshot/tears.png',})
                f.write( str(element_list) + ',\n')          



##DEFUNCT##  but maybe useful later
        
    # store.sprites.ava_armscrossed = CharacterSprite(
        # 'ava',
        # {'armscross':'Character/Ava/armscrossed/base.png'}, #,'handonhair':'Character/Ava/handonhair/base.png','handonhip':'Character/Ava/handonhip/base.png'},
        # {'blush':'Character/Ava/armscrossed/blush.png'},
        # {'neutral':'Character/Ava/armscrossed/mouth/neutral.png','shout':'Character/Ava/armscrossed/mouth/shout.png','smile':'Character/Ava/armscrossed/mouth/smile.png','talk':'Character/Ava/armscrossed/mouth/talk.png'},
        # {'closed':'Character/Ava/armscrossed/eyes/closed.png','narrow':'Character/Ava/armscrossed/eyes/narrow.png','neutral':'Character/Ava/armscrossed/eyes/neutral.png'},
        # {'angry':'Character/Ava/armscrossed/eyebrows/angry.png','neutral':'Character/Ava/armscrossed/eyebrows/neutral.png'},
        # extras={'patch':ConditionSwitch('sanklegion==True','Character/Ava/armscrossed/eyepatch.png','sanklegion==False',Null())})
    # store.sprites.ava_armscrossed.init_images()
    
    # store.sprites.ava_fingerup = CharacterSprite(
        # 'ava',
        # {'fingerup':'Character/Ava/fingerup/base.png'},
        # {'blush':'Character/Ava/fingerup/blush.png'},
        # {'neutral':'Character/Ava/fingerup/mouth/neutral.png','shout':'Character/Ava/fingerup/mouth/shout.png','smile':'Character/Ava/fingerup/mouth/smile.png','talk':'Character/Ava/fingerup/mouth/talk.png'},
        # {'narrow':'Character/Ava/fingerup/eyes/narrow.png','neutral':'Character/Ava/fingerup/eyes/neutral.png'},
        # {'angry':'Character/Ava/fingerup/eyebrows/angry.png','neutral':'Character/Ava/fingerup/eyebrows/neutral.png'},
        # extras={'patch':ConditionSwitch('sanklegion==True','Character/Ava/fingerup/eyepatch.png','sanklegion==False',Null())})
    # store.sprites.ava_fingerup.init_images()
    
    # store.sprites.ava_handonhair = CharacterSprite(
        # 'ava',
        # {'handonhair':'Character/Ava/handonhair/base.png'},
        # {'blush':'Character/Ava/handonhair/blush.png'},
        # {'default':'Character/Ava/handonhair/mouth/default.png','disgust':'Character/Ava/handonhair/mouth/disgust.png','laugh':'Character/Ava/handonhair/mouth/laugh.png','pout':'Character/Ava/handonhair/mouth/pout.png','smirk':'Character/Ava/handonhair/mouth/smirk.png'},
        # {'narrow':'Character/Ava/handonhair/eyes/narrow.png','default':'Character/Ava/handonhair/eyes/default.png','neutral':'Character/Ava/handonhair/eyes/neutral.png'},
        # {'angry':'Character/Ava/handonhair/eyebrows/angry.png','neutral':'Character/Ava/handonhair/eyebrows/neutral.png'},
        # extras={'patch':ConditionSwitch('sanklegion==True','Character/Ava/handonhair/eyepatch.png','sanklegion==False',Null())})
    # store.sprites.ava_handonhair.init_images()




    def test_ava():
        
        if not hasattr(store,'sprites'):
            store.sprites = store.object()
        store.sprites.avatest = CharacterSprite(
            'ava',
            ['Character/Ava/armscrossed/base.png','Character/Ava/fingerup/base.png','Character/Ava/handonhair/base.png','Character/Ava/handonhip/base.png'],
            ['Character/Ava/armscrossed/blush.png','Character/Ava/fingerup/blush.png'],
            ['Character/Ava/armscrossed/mouth/neutral.png','Character/Ava/armscrossed/mouth/shout.png','Character/Ava/armscrossed/mouth/smile.png','Character/Ava/armscrossed/mouth/talk.png'],
            ['Character/Ava/armscrossed/eyes/closed.png','Character/Ava/armscrossed/eyes/narrow.png','Character/Ava/armscrossed/eyes/neutral.png'],
            ['Character/Ava/armscrossed/eyebrows/angry.png','Character/Ava/armscrossed/eyebrows/neutral.png'])
            
        # store.avasprite = store.sprites.ava.get_sprite()
        # store.avasprite = Transform(store.avasprite)
        # store.avasprite.zoom = 0.9
        # store.avasprite.xanchor = 0.5
        # store.avasprite.yanchor = 0.0
        # store.avasprite.ypos = -80
        
        renpy.display.image.register_image( ('ava','armscross','eyesclosed') ,store.sprites.ava.get_sprite())
        store.sprites.ava.eyes = store.sprites.ava._list_eyes[1]
        renpy.display.image.register_image( ('ava','armscross','narrow') ,store.sprites.ava.get_sprite())
        
        
        # renpy.show('avasprite',what=avasprite) #at_list=[Dissolve])
        # renpy.with_statement(dissolve)
        
    # test_ava()
    # renpy.image( ('ava','armscross','eyesclosed') ,store.avasprite)
