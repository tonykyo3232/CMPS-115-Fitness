def getExerList():
    exerciseList = list()
    exercrseDisc0 = dict()
    exercrseDisc1 = dict()
    exercrseDisc2 = dict()
    exercrseDisc3 = dict()
        
    exercrseDisc0 = {"exercise": "close grip", "equ":"Barbell",
                     "desc": "Lay flat on bench / For the duration of movement, arch lower back slightly, Retract shoulder blades back and down, and plant feet flat on the floor or stay on toes / Grip barbell in the racked position at shoulder width / Unrack barbell and bring to starting position directly in front of the center of the chest / Elbow should be facing 45 degrees away from the body at starting position / Take a deep breath / Hold breath and lower barbell to touch the center of chest in a linear motion / As barbell is descending, keep elbows no more than 45 degrees away from the body but tuck the elbows towards the body as much possible / When barbell touches chest, press barbell upward in a linear motion back to the starting position / As barbel is ascending, breathe out"
                    ,"URL":"https://www.youtube.com/embed/wxVRe9pmJdk"}

    exercrseDisc1 = {"Exercise": "Skull Crushers", "equ": "Barbell", "desc": "Lay flat on bench / For the duration of movement, arch lower back slightly and plant feet flat on the floor / Grip barbell in the racked position at shoulder width / Unrack barbell and bring to starting position directly in front of the collarbone or upper chest / Elbow should be facing 45 degrees away from the body at starting position / Keep elbow at this fixed position for the duration of the movement / Take a deep breath / Hold breath and lower barbell to the top of the head / Do this by bending at the elbows, but the elbows can not descend / When barbell is at the top of the head, bring the barbell back to the starting position by extending the arms / As arms are extending, breathe out / Elbow is still fixed when extending the arms ", "URL":"https://www.youtube.com/embed/trVzEReByPg"}

    exercrseDisc2 = {"Exercise": "Curls", "equ": "Barbell", "desc": "Stand up straight, feet at shoulder width / Grip the barbell at shoulder width where palms are facing up / Bring the barbell to the starting position where arms are fully straight at the sides of the body / For the duration of the movement, keep shoulders retracted, chest up, and elbows close to the body / Take a deep breath / Keep elbows at a fixed position and curl the barbell up by bending the elbows, bringing the barbell to the front of mid chest / Lower the barbell in a controlled manner to the starting position by extending the arms, all while keeping elbow at a fixed position / As barbell is being lowered, breathe out", "URL": "https://www.youtube.com/embed/FAEWpmb9YQs"}

    exerciseDisc3 = {"Exercise": "Close Grip Push Ups", "equ": "n/a", "desc": "Lay flat on your stomach with all body parts close to the body / Plant hands underneath the shoulders / Extend the arms to lift yourself off the floor into the starting position / Stay on your toes and hands / Hands should be pointed straight ahead / For the duration of this movement, keep the back flat and abdominals tight / Take a deep breath / Bend arms to 90 degrees and keep the elbows back and close to the body at all times / Press the floor away by extending the arms back into the starting position, all while breathing out", "URL": "https://www.youtube.com/embed/G2mlaEfpEIM"}

    exerciseList.append(exercrseDisc0)
    exerciseList.append(exercrseDisc1)
    exerciseList.append(exercrseDisc2)
    exerciseList.append(exercrseDisc3)

    return exerciseList

def main():
    exerList = getExerList()
    for i in range(len(exerList)):
        print(exerList[i])


main()
print("done")

