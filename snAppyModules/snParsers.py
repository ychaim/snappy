#!/usr/bin/python3
# -*- coding: utf-8 -*-

from twisted.python import log
from lxml import etree
from requests import Response


##########################
##########################
##
## each QUERY gets its own little class.
## this is important to keep modularity
##
##########################




class Parser_RPC_Base(object):
    """ this wrapper class can provide generic functionality for the
     individual API Parser classes""" #
    pass

# this is to connect to RPC on another port and parse differently
class Parser_RPC_Start(Parser_RPC_Base):

    def parse(self, data2parse):
        return data2parse



class Parser_RPC(object):
    """ Parser_RPC
    This is for communicating with BITCOINDARKD!!!
    this talks to BTCD via RPC! used for start only atm
    """#

    ql777_RPC_start = Parser_RPC_Start()

    def __init__(self, environ = {}):
        self.environ = environ

    def parse_RPC(self, data2parse, requestType2Parse={'requestType':'start'}):
    #In [7]: isinstance(ss,bytes)#isinstance(ss,str)

        log.msg("----parse_RPC--------->  ", data2parse, "requestType2Parse", requestType2Parse)
        print(type(data2parse),"\n\n\n")
        data = data2parse
        if isinstance(data, bytes):
            data = data2parse.decode()
        try:
            bsload=data.split("\r\n\r\n")[1]
            bsload1=bsload.replace('null','"null"')
        except:
            print(5*"\nOOOOOOOOPS parse_RPC")

            pass # need better parsing- but this is for start and stop ONLY!
        try:
            bsdi=eval(bsload1)
            print(1*"~~~~~~~bsdi~777~~~~~", bsdi, "\n")

        except:
            return data.encode("utf-8")
         # this takes the raw reply, strips it off header and fillers, evals into a dict
        # and hands the dict to the class that is responsible for the particular query
        # keep the try except here, but move the RPC to a different parser.!!!
        try: # this would be the format that is returned by BTCD RPC on eg port 14632
            result=bsdi['result']
            data_result=eval(result)
        except:# this would be the format that is returned by JL777 http on port 7777
            data_result=bsdi
        # there is a generic class for parsing each query

        if requestType2Parse == 'start': #ToDO privateBet
            parsed = self.ql777_RPC_start.parse(data_result)
        else:
            parsed = 'RAISE_ME_error'
        data = str(parsed).encode("utf-8")
        return data




##############

class Parser_JL777_Base(object):
    """ this wrapper class can provide generic functionality for the
     individual API Parser classes

     Most of these responses from the SuperNET server are returned as is.
     Some of them are internal, and have to fetched from the GUIlopp with GUIpoll.
     These need special parsing.
     eg PONG, havenode and some others
     """ #


# 48 api.h xyz_func calls here + 1 pBET unfinished
# This is from api.h in libjl777 111314
# glue

# // GLUE

class Parser_jl777_gotjson(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_gotpacket(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_gotnewpeer(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_BTCDpoll(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse
class Parser_jl777_GUIpoll(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_stop(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_settings(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


# // passthru


class Parser_jl777_passthru(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_remote(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


# multisig MGW



class Parser_jl777_genmultisig(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_getmsigpubkey(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_MGWaddr(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_setmsigpubkey(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_MGWdeposits(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_cosign(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_cosigned(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


# Kademlia DHT


class Parser_jl777_ping(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_pong(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_store(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_findvalue(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_findnode(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_havenode(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_havenodeB(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_findaddress(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


# // MofNfs


class Parser_jl777_savefile(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_restorefile(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_publish(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


#    // Telepathy


class Parser_jl777_getpeers(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_addcontact(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_removecontact(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_dispcontact(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_telepathy(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_getdb(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_sendmessage(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_sendbinary(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_checkmsg(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse



#  // Teleport


class Parser_jl777_maketelepods(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_telepodacct(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

class Parser_jl777_teleport(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


#InstantDEX


class Parser_jl777_orderbook(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_placebid(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_placeask(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_makeoffer(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_respondtx(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_processutx(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


#Tradebot

class Parser_jl777_pricedb(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_getquotes(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_jl777_tradebot(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

# privatebet

## unfinisihed       pBET
class Parser_jl777_placeLay(Parser_JL777_Base):

    def parse(self, data2parse):
        return data2parse

  
##########################
##########################
##
## The Parser_777 Container and Admin class
##
##########################
##########################

class Parser_777(object):
    """ Parser_777
    // glue
    // multisig
    // Kademlia DHT
    // MofNfs
    // Telepathy
    // Teleport
    // InstantDEX
    // Tradebot
    // # privatebet
    """#

    # // glue
    ql777_gotjson = Parser_jl777_gotjson()
    ql777_gotpacket = Parser_jl777_gotpacket()
    ql777_gotnewpeer = Parser_jl777_gotnewpeer()
    ql777_BTCDpoll = Parser_jl777_BTCDpoll()
    ql777_GUIpoll = Parser_jl777_GUIpoll()
    ql777_settings = Parser_jl777_settings()
    ql777_stop = Parser_jl777_stop()
    ql777_settings = Parser_jl777_settings()

    #// passthru
    ql777_passthru = Parser_jl777_passthru()
    ql777_remote = Parser_jl777_remote()

    # // multisig
    ql777_genmultisig = Parser_jl777_genmultisig()
    ql777_getmsigpubkey = Parser_jl777_getmsigpubkey()
    ql777_MGWaddr = Parser_jl777_MGWaddr()
    ql777_setmsigpubkey = Parser_jl777_setmsigpubkey()
    ql777_MGWdeposits = Parser_jl777_MGWdeposits()
    ql777_cosign = Parser_jl777_cosign()
    ql777_cosigned = Parser_jl777_cosigned()

    # // Kademlia DHT
    ql777_ping = Parser_jl777_ping()
    ql777_pong = Parser_jl777_pong()
    ql777_store = Parser_jl777_store()
    ql777_findvalue = Parser_jl777_findvalue()
    ql777_findnode = Parser_jl777_findnode()
    ql777_havenode = Parser_jl777_havenode()
    ql777_havenodeB = Parser_jl777_havenodeB()
    ql777_findaddress = Parser_jl777_findaddress()

    # // MofNfs
    ql777_savefile = Parser_jl777_savefile()
    ql777_restorefile = Parser_jl777_restorefile()
    ql777_sendfile = Parser_jl777_publish()

    # // Telepathy
    ql777_getpeers = Parser_jl777_getpeers()
    ql777_addcontact = Parser_jl777_addcontact()
    ql777_removecontact = Parser_jl777_removecontact()
    ql777_dispcontact = Parser_jl777_dispcontact()
    ql777_telepathy = Parser_jl777_telepathy()
    ql777_getdb = Parser_jl777_getdb()
    ql777_sendmessage = Parser_jl777_sendmessage()
    ql777_sendbinary = Parser_jl777_sendbinary()
    ql777_checkmsg = Parser_jl777_checkmsg()

    # // Teleport
    ql777_maketelepods = Parser_jl777_maketelepods()
    ql777_telepodacct = Parser_jl777_telepodacct()
    ql777_teleport = Parser_jl777_teleport()

    # // InstantDEX
    ql777_orderbook = Parser_jl777_orderbook()
    ql777_placebid = Parser_jl777_placebid()
    ql777_placeask = Parser_jl777_placeask()
    ql777_makeoffer = Parser_jl777_makeoffer()
    ql777_respondtx = Parser_jl777_respondtx()
    ql777_processutx = Parser_jl777_processutx()

    # // Tradebot
    ql777_pricedb = Parser_jl777_pricedb()
    ql777_getquotes = Parser_jl777_getquotes()
    ql777_tradebot = Parser_jl777_tradebot()

    # // # privatebet
    ql777_placeLay = Parser_jl777_placeLay()



    def __init__(self, environ = {}):
        self.environ = environ


    def parse_777(self, data2parse, requestType2Parse):
        """ here we should be flexible as to the data type we get and parse.
         so we need some type checking and hand always the same data type to the actual parse functions."""#
        log.msg("def parse_777()--------->  ", data2parse, "requestType2Parse is: ", requestType2Parse)
        print(type(data2parse))

        if isinstance(data2parse, Response):
            data2parse = data2parse.json()
            parsed_777= self.parseReturnedDict(data2parse, requestType2Parse)
            return str(parsed_777).encode("utf-8")

        elif isinstance(data2parse, dict):
            parsed_777 = self.parseReturnedDict(data2parse, requestType2Parse)
            return str(parsed_777).encode("utf-8")

        elif isinstance(data2parse, bytes):
            data = data2parse.decode()
            bsload=data.split("\r\n\r\n")[1]
            bsload1=bsload.replace('null','"null"')
            try:
                bsdi=eval(bsload1)
            except:
                return data.encode("utf-8")
            try: # this would be the format that is returned by BTCD RPC on eg port 14632
                result=bsdi['result']
                data2parse=eval(result)
            except:# this would be the format that is returned by JL777 http on port 7777
                data2parse=bsdi
            parsed_777=self.parseReturnedDict(data2parse, requestType2Parse)
            return str(parsed_777).encode("utf-8")


    def parseReturnedDict(self,data2parse, requestType2Parse):

        #print("parseReturnedDict",type(data2parse),"\n\n\n")
        # there is a generic class for parsing each query
        if requestType2Parse == 'placeLay': #ToDO privateBet
        # // # privatebet 1
            parsed = self.ql777_placeLay.parse(data2parse)

        # // glue 7              ql777_

        elif requestType2Parse == 'gotjson':
            parsed = self.ql777_gotjson.parse(data2parse)

        elif requestType2Parse == 'gotpacket':
            parsed = self.ql777_gotpacket.parse(data2parse)

        elif requestType2Parse == 'gotnewpeer':
            parsed = self.ql777_gotnewpeer.parse(data2parse)

        elif requestType2Parse == 'BTCDpoll':
            parsed = self.ql777_BTCDpoll.parse(data2parse)

        elif requestType2Parse == 'GUIpoll':
            parsed = self.ql777_GUIpoll.parse(data2parse)

        elif requestType2Parse == 'stop':
            parsed = self.ql777_stop.parse(data2parse)

        elif requestType2Parse == 'settings':
            parsed = self.ql777_settings.parse(data2parse)

    # // passthru 2


        elif requestType2Parse == 'passthru':
            parsed = self.ql777_passthru.parse(data2parse)

        elif requestType2Parse == 'remote':
            parsed = self.ql777_remote.parse(data2parse)


    # // multisig 6 MGW

        elif requestType2Parse == 'genmultisig':
            parsed = self.ql777_genmultisig.parse(data2parse)

        elif requestType2Parse == 'getmsigpubkey':
            parsed = self.ql777_getmsigpubkey.parse(data2parse)

        elif requestType2Parse == 'MGWaddr':
            parsed = self.ql777_MGWaddr.parse(data2parse)

        elif requestType2Parse == 'setmsigpubkey':
            parsed = self.ql777_setmsigpubkey.parse(data2parse)

        elif requestType2Parse == 'MGWdeposits':
            parsed = self.ql777_MGWdeposits.parse(data2parse)

        elif requestType2Parse == 'cosign':
            parsed = self.ql777_cosign.parse(data2parse)

        elif requestType2Parse == 'cosigned':
            parsed = self.ql777_cosigned.parse(data2parse)



    # // Kademlia DHT 8

        elif requestType2Parse == 'ping':
            parsed = self.ql777_ping.parse(data2parse)

        elif requestType2Parse == 'pong':
            parsed = self.ql777_pong.parse(data2parse)

        elif requestType2Parse == 'store':
            parsed = self.ql777_store.parse(data2parse)

        elif requestType2Parse == 'findvalue':
            parsed = self.ql777_findvalue.parse(data2parse)

        elif requestType2Parse == 'findnode':
            parsed = self.ql777_findnode.parse(data2parse)

        elif requestType2Parse == 'havenode':
            parsed = self.ql777_havenode.parse(data2parse)

        elif requestType2Parse == 'havenodeB':
            parsed = self.ql777_havenodeB.parse(data2parse)

        elif requestType2Parse == 'findaddress':
            parsed = self.ql777_findaddress.parse(data2parse)

    # // MofNfs 3

        elif requestType2Parse == 'savefile':
            parsed = self.ql777_savefile.parse(data2parse)

        elif requestType2Parse == 'restorefile':
            parsed = self.ql777_restorefile.parse(data2parse)

        elif requestType2Parse == 'publish':
            parsed = self.ql777_publish.parse(data2parse)

    # // Telepathy 9

        elif requestType2Parse == 'getpeers':
            parsed = self.ql777_getpeers.parse(data2parse)

        elif requestType2Parse == 'addcontact':
            parsed = self.ql777_addcontact.parse(data2parse)

        elif requestType2Parse == 'removecontact':
            parsed = self.ql777_removecontact.parse(data2parse)

        elif requestType2Parse == 'dispcontact':
            parsed = self.ql777_dispcontact.parse(data2parse)

        elif requestType2Parse == 'telepathy':
            parsed = self.ql777_telepathy.parse(data2parse)

        elif requestType2Parse == 'getdb':
            parsed = self.ql777_getdb.parse(data2parse)

        elif requestType2Parse == 'sendmessage':
            parsed = self.ql777_sendmessage.parse(data2parse)

        elif requestType2Parse == 'sendbinary':
            parsed = self.ql777_sendbinary.parse(data2parse)

        elif requestType2Parse == 'checkmsg':
            parsed = self.ql777_checkmsg.parse(data2parse)

    # // Teleport 3

        elif requestType2Parse == 'maketelepods':
            parsed = self.ql777_maketelepods.parse(data2parse)

        elif requestType2Parse == 'telepodacct':
            parsed = self.ql777_telepodacct.parse(data2parse)

        elif requestType2Parse == 'teleport':
            parsed = self.ql777_teleport.parse(data2parse)

    # // InstantDEX 6

        elif requestType2Parse == 'orderbook':
            parsed = self.ql777_orderbook.parse(data2parse)

        elif requestType2Parse == 'placebid':
            parsed = self.ql777_placebid.parse(data2parse)

        elif requestType2Parse == 'placeask':
            parsed = self.ql777_placeask.parse(data2parse)

        elif requestType2Parse == 'makeoffer':
            parsed = self.ql777_makeoffer.parse(data2parse)

        elif requestType2Parse == 'respondtx':
            parsed = self.ql777_respondtx.parse(data2parse)

        elif requestType2Parse == 'processutx':
            parsed = self.ql777_processutx.parse(data2parse)

    # // Tradebot 3

        elif requestType2Parse == 'pricedb':
            parsed = self.ql777_pricedb.parse(data2parse)

        elif requestType2Parse == 'getquotes':
            parsed = self.ql777_getquotes.parse(data2parse)

        elif requestType2Parse == 'tradebot':
            parsed = self.ql777_tradebot.parse(data2parse)

        else:
            parsed = {'RAISE_ME_error':'RAISE_ME_error'}

        return parsed




##########################
##########################
##########################
##########################



class Parser_XML_Base(object):
    """ this wrapper class can provide generic functionality for the
     individual API Parser classes""" #
    pass


class Parser_XML_SoccerSchedule(Parser_XML_Base):

    def parse(self, data2parse):

        log.msg("XmlParser STARTPARSE!!",  self)
        daily_summary = etree.fromstring(data2parse) #parse(url)
        daily_summaryIter = daily_summary.iter()
        returnThis = ''#'<html>'
        limi=0

        for elem in daily_summaryIter:
            returnThis += (str(elem.attrib) + "\r\n")
            #print(elem.tag, " - " , str(elem.attrib)) # <--------------------
            #limi+=1
            #if limi > 20:
            #    break

        #returnThis += "</html>"
        returnThis = returnThis.encode("utf-8")
        return returnThis


class Parser_XML_MatchBoxScore(Parser_XML_Base):

    def parse(self, data2parse):
        return data2parse


class Parser_XML_GetNewsFeed(Parser_XML_Base):

    def parse(self, data2parse):

        log.msg("XmlParser STARTPARSE!!",  self)
        daily_summary = etree.fromstring(data2parse) #parse(url)
        daily_summaryIter = daily_summary.iter()
        returnThis = ''#'<html>'
        limi=0

        for elem in daily_summaryIter:
            returnThis += (str(elem.attrib) + "\r\n")
            #print(elem.tag, " - " , str(elem.attrib)) # <--------------------
            #limi+=1
            #if limi > 20:
            #    break

        #returnThis += "</html>"
        returnThis = returnThis.encode("utf-8")
        return returnThis


class Parser_XML_DailySummary(Parser_XML_Base):

    def parse(self, data2parse):
        log.msg(" Parser_LOC XmlParser STARTPARSE!!", self)

        daily_summary = etree.fromstring(data2parse) 

        daily_summaryIter = daily_summary.iter()

        returnThis = ''
        limi=0

        for elem in daily_summaryIter:
            returnThis += (str(elem.attrib) + "\r\n")
            #print(elem.tag, " - " , str(elem.attrib)) # <--------------------
            #limi+=1
            #if limi > 20:
            #    break

        #returnThis += "</html>"
        returnThis = returnThis.encode("utf-8")
        return returnThis





# one data processor class
class Parser_XML(object):
    """- this parses the xml that is received from the remote data provider"""  # customize info from fetched xml

    parser_XML_MatchBoxScore = Parser_XML_MatchBoxScore()
    parser_XML_GetNewsFeed = Parser_XML_GetNewsFeed()
    parser_XML_DailySummary = Parser_XML_DailySummary()


    def __init__(self, environ = {}):
        self.environ = environ

    def ack(self):
        log.msg("XmlParser HERE!")

    def parse_XML(self, data2parse, requestType2Parse ):

        print(1*"\n++++++++++++",requestType2Parse, data2parse )
        if requestType2Parse == 'getNewsFeed':
            parsed = self.parser_XML_GetNewsFeed.parse(data2parse)

        elif requestType2Parse == 'MatchBoxScore':
            parsed = self.parser_XML_MatchBoxScore.parse(data2parse)

        elif requestType2Parse == 'DailySummary':
            parsed = self.parser_XML_DailySummary.parse(data2parse)

        else:
            parsed = 'RAISE ME error'

        data = str(parsed).encode("utf-8")

        return data







##########################
##########################
##########################
##########################


##########################
##########################
##
## each QUERY gets its own little class.
## this is important to keep modularity
##
##########################

### Here we mostly just MIRROR what is happening in the XML PARSERS!
### using these here is allowing for variations other than xml feed reading!

class Parser_Loc_Base(object):
    """ this wrapper class can provide generic functionality for the
     individual API Parser classes""" #
    pass

class Parse_Loc_Season(Parser_Loc_Base):
    pass # mabye not needed do locally in parser

    def parse(self, data2parse):
        return data2parse



class Parser_LOC(object):
    """- this parses the data that is retrieved from a local cache
    This is the local Parser wrapper class. When we need to parse local XML, we can just use an xml Parser class
    Or other parser classes for other file formats
    This can access XML parsers as well as any other Parsers
    """#

    qLOC_Season = Parse_Loc_Season()
    parser_XML_DailySummary = Parser_XML_DailySummary()
    parser_XML_SoccerSchedule = Parser_XML_SoccerSchedule()



    def __init__(self, environ = {}):
        self.environ = environ

    def parse_File(selfdata2parse, requestType2Parse ):
        pass
    def parse_Message(selfdata2parse, requestType2Parse ):
        pass

    def parse_XML(self, data2parse, reqDict ):
        #print(13*"\n\n\n***********", reqDict)

        if reqDict['requestType'] == 'DailySummary':
            parsed = self.parser_XML_DailySummary.parse(data2parse)

        elif reqDict['requestType'] == 'soccer_schedule':
            parsed = self.parser_XML_SoccerSchedule.parse(data2parse)

        else:
            parsed = 'RAISE ME error'

        data = str(parsed).encode("utf-8")

        return data


#        log.msg(" Parser_LOC XmlParser STARTPARSE!!", self)


# THE LOCALS HAVE TO USE THE XML PARSERS TOO!!!!!!!! AT LEAST THE XML ONES, BECAUSE THEY LOAD A CACHED XML FILE

