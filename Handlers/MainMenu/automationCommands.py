import Handlers.camperHandler
from Handlers.camperHandler import summerCamp

from Objects.values import GLOBAL_VALUES
from Objects.camper import Camper

from random import randint, shuffle

def setEveryBalance():
    global summerCamp

    try:
        amount = amountPrompt()
        mainMenu()
        if not any(elem != "" for elem in summerCamp.getAllCampers()):
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        for camper in summerCamp.getAllCampers():
            if camper:
                camper.setBalance(amount)

        print('| Every balance cleared!                       |')
        print('|  PS: HR would like a word with you!          |')
        print('|----------------------------------------------|')

    except AttributeError:
        pass
    except Exception as e:
        print(e)


def setEveryApplication():
    global summerCamp

    try:
        status = applicationStatusPrompt()
        mainMenu()
        if not any(elem != "" for elem in summerCamp.getAllCampers()):
            print('| There are currently no campers!              |')
            print('|----------------------------------------------|')
            return

        for camper in summerCamp.getAllCampers():
            if camper:
                if camper.getBalance() == 0:
                    camper.setAppStatus(status)

        print('| Every application status changed!            |')
        print('|  PS: Some excellent quality control there...   |')
        print('|----------------------------------------------|')

    except AttributeError:
        pass
    except Exception as e:
        print(e)


#def assignCampersToSessions():
#    try:
#        summerCamp.sortList(parameter="assignmentRequest")
#
#        temporaryList = summerCamp.getAllCampers().copy()
#
#        for camper in summerCamp.getAllCampers():
#            if not isinstance(camper, Camper) or camper.getAssignmentRequest() is False:
#                continue
#
#            camper.setAppStatus(1)
#            camper.setBalance(0)
#
#            index = randint(0, 2)
#            partner = camper.getAssignment()
#
#            camper.setSession(index)
#            partner.setSession(index)
#
#            summerCamp.insertCamperInSession(camper)
#            summerCamp.insertCamperInSession(partner)
#
#            summerCamp.updateCamper(camper)
#            summerCamp.updateCamper(partner)
#
#            try:
#                temporaryList.remove(camper)
#                temporaryList.remove(partner)
#            except ValueError:
#                pass
#
#        maleList = []
#        femaleList = []
#
#        for camper in temporaryList:
#            if not isinstance(camper, Camper):
#                continue
#
#            if camper.getGender() == "M":
#                maleList.append(camper)
#                temporaryList.remove(camper)
#            elif camper.getGender() == "F":
#                femaleList.append(camper)
#                temporaryList.remove(camper)
#
#        shuffle(maleList)
#        shuffle(femaleList)
#
#        for camper in maleList:
#            if not isinstance(camper, Camper):
#                continue
#
#            for i in range(3):
#                if camper.getSession() is not False:
#                    continue
#                elif summerCamp.countGender(session=i)[0] > GLOBAL_VALUES["maxGendersInSession"]:
#                    continue
#
#                camper.setAppStatus(1)
#                camper.setBalance(0)
#
#                camper.setSession(i)
#
#                summerCamp.insertCamperInSession(camper)
#                summerCamp.updateCamper(camper)
#
#                try:
#                    maleList.remove(camper)
#                except ValueError:
#                    pass
#
#
#    except Exception as e:
#        print(e)
#
#    mainMenu()
#    print('| All session filled!                          |')
#    print('|----------------------------------------------|')
#
#
#def assignCampersToBunkhouses():
#    try:
#        for location in locations:
#            if location == "allCampers":
#                continue
#            else:
#                maleCampers = [camper for camper in globals()[location][0] if camper.gender == 'M']
#                femaleCampers = [camper for camper in globals()[location][0] if camper.gender == 'F']
#
#                maleCampers.sort(key=lambda x: x.age)
#                femaleCampers.sort(key=lambda x: x.age)
#
#                genderArray = 'maleCampers'
#
#                for i in range(6):
#                    if i >= 3:
#                        genderArray = 'femaleCampers'
#                    for camper in locals()[genderArray]:
#                        partner = camper.getAssignmentRequest()
#                        if camper.getBunkhouse() is not None:
#                            continue
#                        elif globals()[location][1][i].count(None) == 0:
#                            continue
#
#                        elif partner and partner.getBunkhouse() is not None:
#                            if globals()[location][1][i].count(None) == 1:
#                                continue
#                            elif camper.getAge() < partner.getAge():
#                                continue
#                            elif camper.getAge() > partner.getAge():
#                                camper.setBunkhouse(i)
#                                partner.setBunkhouse(i)
#                                try:
#                                    globals()[location][1][i].remove(None)
#                                    globals()[location][1][i].remove(None)
#                                except ValueError:
#                                    skip
#                                globals()[location][1][i].append(camper)
#                                globals()[location][1][i].append(partner)
#
#                        else:
#                            camper.setBunkhouse(i)
#                            try:
#                                globals()[location][1][i].remove(None)
#                            except ValueError:
#                                skip
#                            globals()[location][1][i].append(camper)
#
#        for location in locations:
#            if location == "allCampers":
#                continue
#            else:
#                for i in range(6):
#                    for j in range(12):
#                        camper = globals()[location][1][i][j]
#
#                        aCIndex = -1
#                        gLIndex = -1
#
#                        try:
#                            aCIndex = allCampers.index(searchCamperFullName(allCampers, camper.getName()))
#                        except ValueError:
#                            pass
#                        except AttributeError:
#                            pass
#                        try:
#                            gLIndex = globals()[location][0].index(searchCamperFullName(globals()[location][0], camper.getName()))
#                        except ValueError:
#                            pass
#                        except AttributeError:
#                            pass
#
#                        if aCIndex != -1:
#                            allCampers.pop(aCIndex)
#                            allCampers.insert(aCIndex, camper)
#                        if gLIndex != -1:
#                            globals()[location][0].pop(gLIndex)
#                            globals()[location][0].insert(gLIndex, camper)
#
#
#    except Exception as e:
#        exc_type, exc_obj, exc_tb = sys.exc_info()
#        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#        print(exc_type, fname, exc_tb.tb_lineno)
#
#    mainMenu()
#    print('| All bunkhouses filled!                       |')
#    print('|----------------------------------------------|')
#
#
#def assignCampersToTribes():
#
#    maxGenderPerTribe = 6
#
#    try:
#        for location in locations:
#            if location == "allCampers":
#                continue
#            else:
#                globals()[location][0].sort(key=lambda x: x.age)
#
#                for i in range(6):
#                    for camper in globals()[location][0]:
#                        numberOfMalesOrFemales = numberOfGender(globals()[location][2][i], camper.getGender())
#                        partner = camper.getAssignment()
#
#                        if camper.getTribe() is not None:
#                            continue
#                        elif globals()[location][2][i].count(None) == 0:
#                            continue
#
#                        if partner:
#                            if partner.getTribe():
#                                continue
#
#                            if camper.getAge() < partner.getAge():
#                                continue
#
#                            elif camper.getGender() == partner.getGender():
#                                camperGender = numberOfGender(globals()[location][2][i], camper.getGender())
#
#                                if camperGender > maxGenderPerTribe:
#                                    continue
#
#                                elif camperGender + 2 > maxGenderPerTribe:
#                                    removedCamper = globals()[location][2][i].pop()
#                                    globals()[location][0].remove(removedCamper)
#                                    globals()[location][0].append(removedCamper)
#                                    globals()[location][0].sort(key=lambda x: x.age)
#
#                            elif camper.getGender() != partner.getGender():
#                                camperGender = numberOfGender(globals()[location][2][i], camper.getGender())
#                                partnerGender = numberOfGender(globals()[location][2][i], partner.getGender())
#
#                                if camperGender + 1 > maxGenderPerTribe:
#                                    removedCamper = globals()[location][2][i].pop()
#                                    globals()[location][0].remove(removedCamper)
#                                    globals()[location][0].append(removedCamper)
#                                    globals()[location][0].sort(key=lambda x: x.age)
#
#                                elif partnerGender + 1 > maxGenderPerTribe:
#                                    removedCamper = globals()[location][2][i].pop()
#                                    globals()[location][0].remove(removedCamper)
#                                    globals()[location][0].append(removedCamper)
#                                    globals()[location][0].sort(key=lambda x: x.age)
#
#                            camper.setTribe(i)
#                            partner.setTribe(i)
#                            try:
#                                globals()[location][2][i].remove(None)
#                                globals()[location][2][i].remove(None)
#                            except ValueError:
#                                pass
#                            globals()[location][2][i].append(camper)
#                            globals()[location][2][i].append(partner)
#
#                        else:
#                            numberOfMalesOrFemales = numberOfGender(globals()[location][2][i], camper.getGender())
#
#                            if numberOfMalesOrFemales + 1 > maxGenderPerTribe:
#                                continue
#                            camper.setTribe(i)
#                            try:
#                                globals()[location][2][i].remove(None)
#                            except ValueError:
#                                pass
#                            globals()[location][2][i].append(camper)
#
#        for location in locations:
#            if location == "allCampers":
#                continue
#            else:
#                for i in range(6):
#                    for j in range(12):
#                        try:
#                            camper = globals()[location][2][i][j]
#                        except Exception as e:
#                            print(e)
#
#                        aCIndex = -1
#                        gLIndex = -1
#
#                        try:
#                            aCIndex = allCampers.index(searchCamperFullName(allCampers, camper.getName()))
#                        except ValueError:
#                            pass
#                        except AttributeError:
#                            pass
#                        try:
#                            gLIndex = globals()[location][0].index(searchCamperFullName(globals()[location][0], camper.getName()))
#                        except ValueError:
#                            pass
#                        except AttributeError:
#                            pass
#
#                        if aCIndex != -1:
#                            allCampers.pop(aCIndex)
#                            allCampers.insert(aCIndex, camper)
#                        if gLIndex != -1:
#                            globals()[location][0].pop(gLIndex)
#                            globals()[location][0].insert(gLIndex, camper)
#
#
#    except Exception as e:
#        exc_type, exc_obj, exc_tb = sys.exc_info()
#        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#        print(exc_type, fname, exc_tb.tb_lineno)