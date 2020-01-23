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
    def select_case(self,label=None):
        """inilizza il costrutto"""
        self.__label=label
    def case(self, label, TO=None, IS="==", command=None, arg=()):
        """predispone condizione e azione"""
        if self.__label is not None: # se è presente la label
            if TO : # clausola TO presente
                cond=self.__label >=label and self.__label  <= TO
                self.__case.append((cond, command, arg))
            else:
                d=self.__op(IS, label)
                cond=d[IS]
                self.__case.append((cond, command, arg))
        else: # case(condizione,command,arg)
            self.__case.append((label, command, arg))
        #print("#"*10,self.__case,"#" *10)   
    def __op(self,IS,label):
        d={"==":self.__label==label,"<=":self.__label<=label,\
           ">=":self.__label>=label,"!=":self.__label!=label}
        return d
    def case_else(self, command, arg=()):
        """viene eseguito se nessun caso è verificato"""
        self.__else_case=command
        self.__else_arg=arg
    @property    
    def end_select(self):
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
