from Case import Case
sx=Case()
sx.select_case(10)
sx.case(1, command=print,arg=("voce 1",))
sx.case(2, command=print,arg=("voce 2",))
sx.case(3, TO=12, command=print,arg=("voci da 3 a 5","Ok"))
sx.case(8, IS=">=", command=print,arg=("voce >= 8",))
sx.case_else(command=print,arg=("altro",))
sx.end_select

sx.select_case("8b")
sx.case('1', command=print,arg=("voce 1",))
sx.case('2', command=print,arg=("voce 2",))
sx.case("A", TO="W", command=print,arg=("Lettera da A a Z",))
sx.case('8b', IS="!=", command=print,arg=("voce >= 8b",))
sx.case_else(command=print,arg=("altro",))
sx.end_select



sx.select_case("8b")
sx.case('1', command=print,arg=("voce 1",))
sx.case('2', command=print,arg=("voce 2",))
sx.case("A", TO="W", command=print,arg=("Lettera da A a Z",))
sx.case('8b', IS="!=", command=print,arg=("voce >= 8b",))
sx.case_else(command=exec,arg=("print('Ciao Ragazzi')",))
sx.end_select

a="Ciao"
sx.select_case()
sx.case(a == "Pippo", print,arg=("voce 1",))
sx.case(a >= "Pippo", print,arg=("voce 2",))
sx.case(a == "Ciao", command=print,arg=("voce 3",))
sx.end_select
