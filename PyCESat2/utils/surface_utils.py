import randomimport numpy as npdef random_hex():    hex_chars = "0123456789abcdef"        return "#"+"".join([random.choice(hex_chars) for i in range(6)])def order_surfaces(dists, surface1, surface2):    """    Determine which surface is the upper surface and which is the lower.    """        #create a dummy list of 1000 photon distances between left/right bounds    test_dists = np.arange(np.min(dists), np.max(dists), 1000)        #if both models are scipy/scikitlearn models    if hasattr(surface1, 'predict') and hasattr(surface2, 'predict'):        #recreate surfaces with dummy array of distances        s1 = np.asarray([surface1.predict(d.reshape(1,-1)) for d in test_dists])        s2 = np.asarray([surface2.predict(d.reshape(1,-1)) for d in test_dists])                #if all the heights in surface1 are greater than all the heights in surfaces 2        if np.all(np.greater(s1,s2)):            #return the upper surfaces first            return surface1, surface2                #else if all heights in surface 2 are greater than all heights in surfaces 1        elif np.all(np.greater(s2,s1)):            #return upper surface first            return surface2, surface1        else:            raise ValueError("Cannot find photons between intersecting surfaces.")                #else if only model 1 is a scipy/scikitlearn model    elif hasattr(surface1, 'predict') and (hasattr(surface2, 'predict') == False):        #see 'if' block for comments on procedure        s1 = np.asarray([surface1.predict(d.reshape(1,-1)) for d in test_dists])        s2 = np.asarray([surface2(d) for d in test_dists])                if np.all(np.greater(s1,s2)):            return surface1, surface2                elif np.all(np.greater(s2,s1)):            return surface2, surface1        else:            raise ValueError("Cannot find photons between intersecting surfaces.")        #else if only model 2 is a scipy/scikitlearn model    elif (hasattr(surface1, 'predict') == False) and hasattr(surface2, 'predict'):        #see 'if' block for comments on procedure        s1 = np.asarray([surface1(d) for d in test_dists])        s2 = np.asarray([surface2.predict(d.reshape(1,-1)) for d in test_dists])                if np.all(np.greater(s1,s2)):            return surface1, surface2                elif np.all(np.greater(s2,s1)):            return surface2, surface1        else:            raise ValueError("Cannot find photons between intersecting surfaces.")        #else neither are scipy/scikitlearn models    else:        #see 'if' block for comments on procedure        s1 = np.asarray([surface1(d) for d in test_dists])        s2 = np.asarray([surface2(d) for d in test_dists])                if np.all(np.greater(s1,s2)):            return surface1, surface2                elif np.all(np.greater(s2,s1)):            return surface2, surface1        else:            raise ValueError("Cannot find photons between intersecting surfaces.")        