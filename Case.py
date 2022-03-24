####################################################
# Classe    : Case                                 #  
# Scopo     : simula la struttura case del basic   #
# Autore    : Marco Salvati                        #
# Email     : salvatimarco61@gmail.com             #
# Licenza   : GPL 3                                #
# Data      : 2019-11-04                           #
####################################################

class Case:
    """
    Classe    : Case
    Scopo     : simula la struttura case del basic
    Autore    : Marco Salvati
    Email     : salvatimarco61@gmail.com
    Licenza   : GPL 3
    Data      : 2019-11-04
    """
    def __init__(self):
        self.__case=[]
        self.__else_case=None
        self.__else_arg=()
        self.__label=None
        
    def Select(self,label=None):
        """inilizza il costrutto"""
        self.__label=label

    def __op(self,Is,label):
        d={"==":self.__label==label,"<=":self.__label<=label,\
           ">=":self.__label>=label,"!=":self.__label!=label}
        return d[Is]
    def Range(self,start,stop, command=None, arg=()):
        if self.__label is not None: # se è presente la label
            cond=self.__label >=start and self.__label  <= stop
            self.__case.append((cond, command, arg))
        else: raise('label not present in Select')
    def In(self,tupla, command=None, arg=()):
        cond=self.__label in tupla
        self.__case.append((cond, command, arg))
    def Is(self,label,cmp='==', command=None, arg=()):
        if self.__label is not None: # se è presente la label
            cond=self.__op(cmp, label)
            self.__case.append((cond, command, arg))
        else: raise('label not present in Select')
    def Cmp(self,cond, command=None, arg=()):
        self.__case.append((cond, command, arg))
    def Else(self, command, arg=()):
        """viene eseguito se nessun caso è verificato"""
        self.__else_case=command
        self.__else_arg=arg
    @property    
    def End(self):
        """Chiude la struttura ed esegue l'azione"""
        eseguito=False
        for i in range(len(self.__case)):
            t=self.__case[i]
            cond,command,arg=t
            if cond: # la clausola è vera
                if command : # il commando è abilitato
                    command(*arg) # eseguilo
                eseguito=True    
                break # esci dal ciclo
            
        if eseguito==False and self.__else_case!=None: # se esiste else case
            self.__else_case(*self.__else_arg) # esegui 
        self.__init__() # ripristina i default per una nuova selezione
