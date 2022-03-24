from Case import Case
case=Case()
case.Select(10)
case.Is(1, command=print,arg=("voce 1",))
case.Is(2, command=print,arg=("voce 2",))
case.Range(3, 12, command=print,arg=("voci da 3 a 12","Ok"))
case.Is(8, cmp=">=", command=print,arg=("voce >= 8",))
case.Else(command=print,arg=("altro",))
case.End

case.Select("8b")
case.Is('1', command=print,arg=("voce 1",))
case.Is('2', command=print,arg=("voce 2",))
case.Range("A", "W", command=print,arg=("Lettera da A a Z",))
case.Is('8b', command=print,arg=("voce = 8b",'Ok'))
case.Else(command=print,arg=("altro",))
case.End


case.Select("8b")
case.Is('1', command=print,arg=("voce 1",))
case.Is('2', command=print,arg=("voce 2",))
case.Range("A", "W", command=print,arg=("Lettera da A a Z",))
case.Is('8b', cmp="!=", command=print,arg=("voce >= 8b",))
case.Else(command=exec,arg=("print('Ciao Ragazzi')",))
case.End


case.Select(5)
case.In((1,2,3,4,5,11,33),command=print,arg=("In Ok",))
case.Is(21, command=print,arg=("voce 1",))
case.Is(33, command=print,arg=("voce 2",))
case.Range(66, 77, command=print,arg=("Lettera da A a Z",))
case.Is(9, cmp="!=", command=print,arg=("voce >= 8b",))
case.Else(command=exec,arg=("print('Ciao Ragazzi')",))
case.End

a="Pluto"
case.Select()
case.Cmp(a == "Pippo", print,arg=("voce 1",))
case.Cmp(a >= "Pippo", print,arg=("voce 2",))
case.Cmp(a == "Ciao", command=print,arg=("voce 3",))
case.Else(command=exec,arg=("print('Ciao Ragazzi')",))
case.End
